# Integrations And Research Patterns

## Public Data Sources

Use available browsing/search tools or user-provided exports to inspect:

- Zillow property page
- Redfin property page
- Realtor.com property page
- county property appraiser or assessor
- county recorder
- public tax records
- MLS exports, only if provided or accessible
- local Realtor association reports
- housing market reports by city, ZIP, subdivision, or county

## Search Patterns

Use targeted searches such as:

```text
"<address>" Zillow
"<address>" Redfin sold
"<address>" county property appraiser
"<ZIP>" housing market median days on market
"<city> <state>" real estate market report inventory DOM price per square foot
"<subdivision/neighborhood>" recent sold homes
```

## Data Capture

Track source, date accessed, and confidence for:

- sale price
- sale date
- listing price
- DOM
- sqft
- lot size
- tax assessment
- active/pending status
- prior sale records
- market trend statistics

## MLS Data

If the user provides MLS data:

- treat MLS as high-priority for sold, active, pending, DOM, and price changes
- still cross-check public records for property facts and last sale
- do not claim MLS access unless it exists in the current context

