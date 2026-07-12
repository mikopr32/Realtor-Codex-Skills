---
name: realtor-listings-property-copy
description: Turn verified property facts into polished, channel-ready real estate marketing copy, including MLS remarks, luxury descriptions, just-listed announcements, feature highlights, headlines, brochures, portal copy, and Spanish, English, or bilingual variants. Use when the user supplies a listing sheet, property details, photos, URL, or draft and needs factual, differentiated copy that respects Fair Housing, MLS, brokerage, advertising, and platform constraints.
---

# Realtor Skill: Listings & Property Copy

## Mission
Transform raw listing data into polished, compliant, emotionally engaging property copy that sells the property benefits without exaggerating or inventing facts.

## Codex execution workflow
1. Build a fact ledger from user-provided materials: verified fact, source, uncertainty, and whether it may be published.
2. Identify the strongest defensible differentiators for the property, location, condition, and intended channel.
3. Separate objective features from inferred benefits. Describe lifestyle through the property and amenities, never through protected-class targeting.
4. Draft to the requested channel and any supplied character limit, MLS rule, brokerage standard, or required disclosure.
5. Flag contradictory or missing facts instead of resolving them by guessing. If browsing current listing data, cite the source and observation date.
6. Run a line-by-line factual and compliance check before delivery.

## Implicit assumptions to check
- The property facts provided by the user are the source of truth.
- If square footage, bedrooms, HOA, taxes, school zones, or upgrades are missing, use placeholders or omit them.
- The copy must attract attention while staying MLS-safe and compliant.

## Critical context to look for
Ask for missing context only when it is impossible to produce a useful answer. Otherwise, make a best-effort version and mark missing items as placeholders.
- Address or area
- Beds/baths/sqft
- Price
- Property type
- Top features
- Upgrades
- Community/HOA/CDD
- Target buyer
- Tone: luxury, family-friendly alternative, investor, first-time buyer, relocation

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
- Do not infer property condition, finishes, views, distances, permits, rental eligibility, accessibility, school assignment, flood zone, or included items from photos alone.
- Do not reproduce copyrighted listing remarks from another agent. Extract facts and write original language.
- Treat public remarks, confidential agent remarks, showing instructions, access codes, occupancy details, and seller information as different disclosure classes.

## Specific tasks this skill covers
- MLS listing description
- Luxury listing copy
- Just-listed announcement
- Feature highlight bullets

## Output protocol
When invoked, return the most relevant property marketing asset. If the user gives raw details and does not specify format, produce:
1. MLS-ready description.
2. Short social version.
3. Feature highlight bullets.
4. 3 headline options.
5. Missing information checklist.

## Built-in deliverables
### MLS listing description
- Opening sentence with the strongest property benefit.
- Interior highlights.
- Exterior/community/location highlights.
- Practical details and CTA.
- Keep it polished but not exaggerated.

### Luxury listing copy
- Elevated language, sensory detail, lifestyle positioning, architectural flow.
- Avoid cliché luxury words unless supported by facts.
- Emphasize privacy, design, craftsmanship, finishes, views, entertaining, and location.

### Just-listed announcement
- Social-ready hook.
- Property snapshot.
- Top 3–5 benefits.
- CTA to schedule a showing, DM, or view full details.

### Feature highlight bullets
Group features by:
- Interior
- Kitchen
- Primary suite
- Outdoor/lifestyle
- Community/location
- Financial/practical details

## Rewrite rules
- Never invent: upgrades, views, appliances, lot size, HOA/CDD, schools, or distances.
- Replace weak facts with benefit-driven wording.
- Remove risky claims like "safe neighborhood," "best schools," "guaranteed equity," or "perfect for families."
- Avoid overusing adjectives. Specific details create trust.

## Quality bar
A strong property description should make the reader understand: what makes this home different, why it matters, and what to do next.

## Metrics to consider
- Listing views
- Saves/favorites
- Showing requests
- Open house attendance
- Days on market versus comparable listings
- Feedback themes from buyers/agents

## Failure modes to flag
- Copy sounds generic and could fit any house
- The strongest feature is buried
- Too much agent language, not enough buyer benefit
- MLS compliance risk
- Missing required property details

## Final response checklist
Before finalizing, verify:
- The copy is specific to the audience, market, and objective.
- The next step is clear.
- The wording avoids unsupported guarantees or protected-class targeting.
- The output is ready to paste, publish, send, or adapt.
- Any missing facts are identified as placeholders, not invented.
- Every material claim is traceable to the user's facts or a dated source.
- Confidential remarks and access or occupancy information are excluded from public copy.
