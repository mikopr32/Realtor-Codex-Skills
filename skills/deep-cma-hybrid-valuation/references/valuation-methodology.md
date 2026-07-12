# Valuation Methodology

## Sold Comparable Scoring

Score each comp from 0 to 100:

- Distance: 20 points
- Recency: 20 points
- Sqft similarity: 15 points
- Bed/bath similarity: 10 points
- Year built similarity: 10 points
- Lot/location similarity: 10 points
- Condition/upgrades similarity: 10 points
- Pool/garage/features similarity: 5 points

Comp tiers:

- Tier 1: 80-100
- Tier 2: 65-79
- Tier 3: 50-64
- Exclude or heavily discount below 50 unless the market is thin

## Adjustment Guidelines

Use local market evidence when available. If unavailable, state that adjustment values are estimates.

Common adjustment categories:

- size
- condition
- upgrades
- pool
- lot
- garage
- location
- amenities
- sale date/time

Adjustment direction:

- If comp is superior to subject, subtract from comp sale price.
- If comp is inferior to subject, add to comp sale price.

Risk rules:

- flag any individual adjustment above 10 percent of comp sale price
- flag any net adjustment above 25 percent of comp sale price
- reduce weight for heavily adjusted comps

## CMA Value

Recommended calculation:

1. calculate adjusted value for each comp
2. assign comp weight based on score
3. calculate weighted adjusted value
4. compare against median adjusted price per sqft x subject sqft
5. reconcile into a CMA range

## Historical Appreciation Value

Use the last recorded sale as the base.

Compound method:

```text
value = last_sale_price * ((1 + annual_rate) ** years_elapsed)
```

Simple cumulative method:

```text
value = last_sale_price * (1 + cumulative_rate)
```

Use compound when the source provides annualized appreciation. Use cumulative only when the source provides cumulative appreciation for the exact period.

## Dynamic Reconciliation

Start at:

```text
final_value = (CMA value * 0.70) + (historical appreciation value * 0.30)
```

Increase CMA weight when:

- 5 or more strong recent comps exist
- active and pending data align with sold comps
- last sale is old
- subject condition changed materially since last sale
- market is shifting quickly

Increase historical weight when:

- last sale is recent and verified
- comp set is thin
- subject is unusual
- appreciation data is hyperlocal and reliable

Suggested confidence ranges:

- High confidence: +/- 2-4 percent
- Medium confidence: +/- 4-7 percent
- Low confidence: +/- 7-12 percent or wider

