# FSBO research schema

Prepare one JSON object per observed listing. Use `null` for unknown values; do not invent them.

## Required keys

- `source`
- `source_url`
- `consulted_at` in `YYYY-MM-DD`
- `listing_status`
- `representation_type`

## Recommended keys

- `address`, `city`, `state`, `zip`
- `price`, `property_type`, `beds`, `baths`, `sqft`, `lot_size`
- `posted_date`, `last_updated`, `visible_dom`, `cumulative_market_time`, `dom_confidence`
- `public_contact_type`, `public_contact_value`
- `buyer_fit`: `strong`, `partial`, `unknown`, or `none`
- `positioning_signals`: list of verified signals
- `data_quality_flags`: list
- `evidence`: list of objects with `field`, `value`, `source_url`, `effective_date`, `confidence`

## Representation types

Use only `Verified_FSBO`, `Probable_FSBO`, `Flat_Fee_MLS_FSBO`, `Agent_Represented`, or `Representation_Unknown`.

## Active statuses

Use `Active`, `Pending`, `Sold`, `Removed`, `Rental`, `Auction`, or `Unknown`. The compiler includes only `Active` listings with FSBO-compatible representation in the verified file.

## Contact handling

Store contact only when expressly published in the listing for transaction communication. Use `Internal_Messaging_Only` when the site exposes messaging but no contact value. Do not add reverse-lookup or enriched personal data.
