#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EPISODE = os.getenv("EPISODE_NUMBER", "84")
VOICE_ID = os.environ["ELEVENLABS_VOICE_ID"]
API_KEY = os.environ["ELEVENLABS_API_KEY"]
EP_DIR = ROOT / "episodes" / EPISODE.zfill(3)
SCRIPT = EP_DIR / "script.txt"
META = EP_DIR / "metadata.json"
MUSIC = ROOT / "assets" / "El_Diario_de_AMI.mp3"
MUSIC_MANIFEST = ROOT / "assets" / "music-manifest.json"
OUTPUT = ROOT / "output" / f"Episodio_{EPISODE}.mp3"


def run(*args: str, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=capture)


def duration(path: Path) -> float:
    result = run(
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=nk=1:nw=1", str(path), capture=True,
    )
    return float(result.stdout.strip())


def loudness(path: Path) -> tuple[float, float, float]:
    result = subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
            "-f", "null", "-",
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    match = re.search(r"\{\s*\"input_i\".*?\}", result.stderr, re.DOTALL)
    if not match:
        raise RuntimeError("No se pudo medir loudness del master.")
    measured = json.loads(match.group(0))
    return (
        float(measured["input_i"]),
        float(measured["input_tp"]),
        float(measured["input_lra"]),
    )


def chunks(text: str, limit: int = 4200) -> list[str]:
    sentences = re.split(r"(?<=[.!?…])\s+", text.strip())
    result: list[str] = []
    current = ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip()
        if len(candidate) > limit and current:
            result.append(current)
            current = sentence
        else:
            current = candidate
    if current:
        result.append(current)
    return result


def generate_voice(text: str, target: Path) -> None:
    url = (
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        "?output_format=mp3_44100_128"
    )
    payload = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }).encode()
    for attempt in range(5):
        request = urllib.request.Request(
            url,
            data=payload,
            headers={
                "xi-api-key": API_KEY,
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                target.write_bytes(response.read())
                return
        except urllib.error.HTTPError as exc:
            if exc.code not in {408, 429, 500, 502, 503, 504}:
                raise
            delay = int(exc.headers.get("Retry-After", 0)) or 2**attempt
            time.sleep(min(delay, 30))
    raise RuntimeError("ElevenLabs no respondió después de cinco intentos.")


def validate_music() -> None:
    expected = json.loads(MUSIC_MANIFEST.read_text())
    digest = hashlib.sha256(MUSIC.read_bytes()).hexdigest()
    if digest != expected["sha256"] or MUSIC.stat().st_size != expected["size_bytes"]:
        raise RuntimeError("La canción oficial no coincide con su manifiesto.")
    if duration(MUSIC) < 53:
        raise RuntimeError("La canción oficial es demasiado corta.")


def main() -> None:
    metadata = json.loads(META.read_text(encoding="utf-8"))
    if metadata["episode"] != int(EPISODE):
        raise RuntimeError("El número solicitado no coincide con metadata.json.")
    validate_music()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ami-") as temp_name:
        temp = Path(temp_name)
        voice_parts: list[Path] = []
        for index, part in enumerate(chunks(SCRIPT.read_text(encoding="utf-8")), 1):
            target = temp / f"voice-{index:03d}.mp3"
            generate_voice(part, target)
            voice_parts.append(target)
        concat = temp / "concat.txt"
        concat.write_text("".join(f"file '{p}'\n" for p in voice_parts))
        voice = temp / "voice.mp3"
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-f", "concat", "-safe", "0", "-i", str(concat),
            "-ar", "44100", "-b:a", "192k", str(voice),
        )
        voice_seconds = duration(voice)
        mix = temp / "mix.wav"
        background_end = 15 + voice_seconds
        filters = (
            "[1:a]atrim=0:15,asetpts=PTS-STARTPTS[intro];"
            f"[1:a]atrim=15:{background_end:.3f},asetpts=PTS-STARTPTS,volume=-35dB[bg];"
            "[0:a]aresample=44100,asetpts=PTS-STARTPTS[voice];"
            "[bg][voice]amix=inputs=2:duration=first:dropout_transition=0[body];"
            "[1:a]atrim=38:53,asetpts=PTS-STARTPTS,afade=t=out:st=12:d=3[outro];"
            "[intro][body][outro]concat=n=3:v=0:a=1[mix]"
        )
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(voice), "-stream_loop", "-1", "-i", str(MUSIC),
            "-filter_complex", filters, "-map", "[mix]",
            "-t", f"{voice_seconds + 30:.3f}", "-c:a", "pcm_s24le", str(mix),
        )
        first_pass = subprocess.run(
            [
                "ffmpeg", "-hide_banner", "-nostats", "-i", str(mix),
                "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
                "-f", "null", "-",
            ],
            check=True,
            text=True,
            capture_output=True,
        )
        match = re.search(r"\{\s*\"input_i\".*?\}", first_pass.stderr, re.DOTALL)
        if not match:
            raise RuntimeError("No se pudo analizar la primera pasada de masterización.")
        measured = json.loads(match.group(0))
        loudnorm_filter = (
            "loudnorm=I=-16:TP=-1.5:LRA=11:"
            f"measured_I={measured['input_i']}:"
            f"measured_LRA={measured['input_lra']}:"
            f"measured_TP={measured['input_tp']}:"
            f"measured_thresh={measured['input_thresh']}:"
            f"offset={measured['target_offset']}:linear=true"
        )
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(mix), "-af", loudnorm_filter,
            "-ar", "44100", "-ac", "2", "-c:a", "libmp3lame",
            "-b:a", "192k", str(OUTPUT),
        )
    output_duration = duration(OUTPUT)
    integrated_lufs, true_peak_dbtp, loudness_range_lu = loudness(OUTPUT)
    if not (-16.6 <= integrated_lufs <= -15.4):
        corrected = OUTPUT.with_name(f"{OUTPUT.stem}_corrected.mp3")
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(OUTPUT),
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-ar", "44100", "-ac", "2", "-c:a", "libmp3lame",
            "-b:a", "192k", str(corrected),
        )
        corrected.replace(OUTPUT)
        output_duration = duration(OUTPUT)
        integrated_lufs, true_peak_dbtp, loudness_range_lu = loudness(OUTPUT)
    if true_peak_dbtp > -1.45:
        peak_corrected = OUTPUT.with_name(f"{OUTPUT.stem}_peak_corrected.mp3")
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(OUTPUT),
            "-af", "loudnorm=I=-16:TP=-1.8:LRA=11",
            "-ar", "44100", "-ac", "2", "-c:a", "libmp3lame",
            "-b:a", "192k", str(peak_corrected),
        )
        peak_corrected.replace(OUTPUT)
        output_duration = duration(OUTPUT)
        integrated_lufs, true_peak_dbtp, loudness_range_lu = loudness(OUTPUT)
    if not (-16.6 <= integrated_lufs <= -15.4):
        final_corrected = OUTPUT.with_name(f"{OUTPUT.stem}_final_corrected.mp3")
        adjusted_target = max(-18.0, min(-14.0, -16.0 + (-16.0 - integrated_lufs)))
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(OUTPUT),
            "-af", f"loudnorm=I={adjusted_target:.2f}:TP=-1.8:LRA=11",
            "-ar", "44100", "-ac", "2", "-c:a", "libmp3lame",
            "-b:a", "192k", str(final_corrected),
        )
        final_corrected.replace(OUTPUT)
        output_duration = duration(OUTPUT)
        integrated_lufs, true_peak_dbtp, loudness_range_lu = loudness(OUTPUT)
    duration_delta = abs(output_duration - (voice_seconds + 30))
    if not (-16.6 <= integrated_lufs <= -15.4):
        raise RuntimeError(f"Master fuera del objetivo: {integrated_lufs:.2f} LUFS.")
    if true_peak_dbtp > -1.45:
        raise RuntimeError(f"Pico verdadero demasiado alto: {true_peak_dbtp:.2f} dBTP.")
    if duration_delta > 1.0:
        raise RuntimeError(f"Duración incompatible con voz + intro/outro: {duration_delta:.3f}s.")
    qa = {
        "episode": int(EPISODE),
        "title": metadata["title"],
        "duration_seconds": round(output_duration, 3),
        "voice_duration_seconds": round(voice_seconds, 3),
        "duration_delta_seconds": round(duration_delta, 3),
        "integrated_lufs": round(integrated_lufs, 2),
        "true_peak_dbtp": round(true_peak_dbtp, 2),
        "loudness_range_lu": round(loudness_range_lu, 2),
        "minimum_duration": output_duration > 30,
        "technical_qa_passed": True,
        "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
        "human_listen_required": True,
        "spotify_published": False,
    }
    (OUTPUT.parent / f"Episodio_{EPISODE}_QA.json").write_text(
        json.dumps(qa, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(qa, ensure_ascii=False))


if __name__ == "__main__":
    main()
