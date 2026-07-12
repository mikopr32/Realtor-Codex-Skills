---
name: realtor-buyer-follow-up
description: Create personalized buyer-lead follow-up for Realtors across SMS, email, WhatsApp, and calls, including first response, consultation booking, pre-approval guidance, showing feedback, offer-stage communication, relocation follow-up, cold-lead reactivation, and nurture sequences. Use when the goal is to move a buyer toward a clear next step without pressure, invented facts, or mishandling financial or personal information.
---

# Realtor Skill: Buyer Follow-Up

## Mission
Move buyer leads from interest to conversation, consultation, pre-approval, showing, offer, and closing through timely, human, non-pushy follow-up.

## Codex execution workflow
1. Classify the lead by source, consent status, stage, urgency, last interaction, market, property, and desired next step.
2. Select the smallest useful message: one relevant value point, one question, and one low-friction CTA.
3. Use only known personalization. Do not infer motivation, finances, household composition, immigration status, or protected characteristics.
4. For sequences, vary the value and purpose of each touch; do not send repeated “checking in” messages.
5. State cadence as a recommendation, not proof of legal permission to contact.
6. Provide CRM-ready fields or branching responses when the user requests an operational sequence.

## Implicit assumptions to check
- Most buyer leads are not ready immediately; the goal is to create a reply and identify readiness.
- The follow-up should reduce friction and ask one clear question at a time.
- Buyer financial details must be handled carefully and referred to lending professionals when needed.

## Critical context to look for
Ask for missing context only when it is impossible to produce a useful answer. Otherwise, make a best-effort version and mark missing items as placeholders.
- Lead source
- Buyer stage
- Market/city
- Budget
- Timeline
- Financing status
- Property viewed
- Preferred channel: text/email/call
- Language

## Default voice and style
- Default language: Spanish, unless the user asks for English or bilingual output.
- Tone: professional, clear, consultative, and conversion-focused. Avoid generic motivational filler.
- Write for real estate consumers, not for other marketers, unless the task is agent recruiting or business content.
- Prefer simple structure: hook, value, credibility, next step.
- Use emojis only when requested or when the channel is social/WhatsApp and emojis fit the brand.
- For every deliverable, make the next step obvious: reply, call, schedule, DM keyword, register, view property, or request valuation.

## Realtor compliance guardrails
- Do not make legal, tax, lending, appraisal, or investment guarantees. Use client-safe wording such as "confirm with your lender," "based on available comps," and "subject to market conditions."
- Avoid Fair Housing risk: do not target, exclude, describe, or imply protected classes. Do not say a property or neighborhood is "perfect for families," "ideal for young professionals," or similar protected-class proxies. Describe property features, lifestyle conveniences, commute, amenities, and objective data instead.
- Do not promise appreciation, approval, rates, payments, or timelines. Present assumptions clearly.
- For schools, crime, HOA/CDD, zoning, insurance, permits, and taxes, recommend verification with official sources instead of making unsupported claims.
- Keep brokerage, MLS, Equal Housing, and local advertising disclosure requirements in mind. If required data is missing, include placeholders instead of inventing facts.
- Respect platform rules for ads and outreach. Avoid spammy language, misleading urgency, or deceptive lead magnets.
- Honor opt-outs and do-not-contact instructions. Do not treat a public phone number, portal inquiry, prior conversation, or purchased lead as proof of consent for every channel or automated cadence.
- Avoid requesting sensitive financial information over insecure channels. Route qualification, lending, tax, and legal questions to the appropriate licensed professional.
- Draft only; do not send messages or update a CRM without explicit authorization.

## Specific tasks this skill covers
- First-touch buyer text
- Showing follow-up email
- Budget check-in message
- Re-engage cold buyer

## Output protocol
When invoked, produce the requested message/script. If the user asks for a sequence, include:
1. First-touch SMS.
2. Same-day follow-up.
3. Day 2 value message.
4. Day 5 check-in.
5. Day 14 re-engagement.
6. Exit/long-term nurture message.

## Built-in deliverables
### First-touch buyer text
Goal: get a reply, not close the deal in one message.
Structure:
- Personalized reason for contact
- One helpful value statement
- One simple question

### Showing follow-up email
Structure:
- Reference the property shown
- Ask for feedback
- Compare fit against their priorities
- Suggest next step: see similar homes, adjust criteria, or review numbers

### Budget check-in message
Use tactful language:
- Confirm comfort range, not just max approval
- Ask about monthly payment comfort
- Recommend lender confirmation if needed

### Re-engage cold buyer
Use curiosity and market value:
- New inventory
- Price reductions
- Programs/incentives
- Updated strategy based on current market

## Conversation principles
- Keep texts short: one idea, one question.
- Avoid pressure language like "I need an answer today" unless a real deadline exists.
- Do not shame the lead for not replying.
- Always create a low-friction next step.

## Sequence logic
Segment buyers by:
- New lead, no response
- Pre-approved and active
- Not pre-approved
- Viewed property
- Submitted offer
- Cold 30+ days
- Relocation buyer
- First-time buyer

## Metrics to include when strategic
- Speed to lead
- Reply rate
- Consultation booking rate
- Pre-approval conversion rate
- Showing-to-offer rate
- Reactivation rate

## Failure modes to flag
- Too many questions in one message
- No clear CTA
- Overly long text
- Generic "checking in" with no value
- Asking for sensitive financial details before trust exists

## Final response checklist
Before finalizing, verify:
- The copy is specific to the audience, market, and objective.
- The next step is clear.
- The wording avoids unsupported guarantees or protected-class targeting.
- The output is ready to paste, publish, send, or adapt.
- Any missing facts are identified as placeholders, not invented.
- The sequence reflects lead stage, prior contact, consent assumptions, and a stop/opt-out path.
- Each touch adds distinct value and asks no more than one primary question.
