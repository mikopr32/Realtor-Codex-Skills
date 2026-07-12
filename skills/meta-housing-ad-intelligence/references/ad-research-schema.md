# Ad research schema

Prepare a JSON array with one object per public ad observation.

## Required

- `advertiser`
- `ad_library_url`
- `visible_start_date` in `YYYY-MM-DD` or null
- `last_verified_date` in `YYYY-MM-DD`
- `status`

## Recommended

- `ad_id`, `format`, `offer`, `hook_type`, `cta`, `funnel`
- `primary_text`, `headline`, `description`
- `visual_patterns`: list of abstract attributes
- `message_patterns`: list
- `disclosures`: list
- `variants_observed`: nonnegative integer
- `limitations`: list

Do not store downloaded competitor assets. Link to the public Ad Library observation.

## Pattern discipline

A pattern appearing once is an isolated observation. Aggregate frequency across ads and advertisers. Longevity is an observation, not proof of performance.

## Originality

Do not pass competitor copy or imagery into generation as material to imitate. Build a new brief from aggregated, abstract patterns and the user's own brand, offer and authorized assets.
