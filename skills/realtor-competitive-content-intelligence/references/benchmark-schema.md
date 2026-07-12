# Benchmark data schema

## Profile table

Required fields:

`competitor_id, competitor_name, platform, handle, profile_url, observed_at, florida_market, followers_visible, profile_access, sample_start, sample_end, sample_size, limitations`

## Content table

Required:

`competitor_id, platform, post_url, published_at, format, topic, pillar, duration_seconds, hook_type, hook_summary, visual_hook, spoken_hook, text_hook, structure, cta_type, funnel_stage, views_visible, likes_visible, comments_visible, followers_observed, pinned, notes`

Optional only when public or authorized:

`shares, saves, average_watch_time, completion_rate, leads, appointments`

Use null for unavailable values; do not use zero unless the measured value is genuinely zero.

## Pattern table

`pattern_id, pattern, platforms, accounts, post_count, sample_share, evidence_urls, associated_public_signal, alternative_explanation, confidence, opportunity, originality_requirement`

## Sampling rules

1. Prefer a consecutive date window over hand-picking only strong posts.
2. Record pinned content and analyze it separately if it distorts recency.
3. Include low- and median-response posts, not only outliers.
4. Compare like formats where possible.
5. Use the same period across accounts when visibility permits.
6. State when deleted, hidden, boosted or collaborative content cannot be identified.
