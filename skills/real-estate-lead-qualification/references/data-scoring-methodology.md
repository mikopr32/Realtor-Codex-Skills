# Data and scoring methodology

## Confidence

- **High:** current value and debt are verified and dated.
- **Moderate:** current value is sourced but debt is modeled, or vice versa.
- **Low:** value and debt are both scenario estimates from historical sale data.
- **Not evaluable:** sale price/date or other required inputs are missing.

## Scenario defaults

When no better inputs exist:

| Scenario | Appreciation | Original LTV | Mortgage rate | Term |
|---|---:|---:|---:|---:|
| Low equity | 2% | 90% | 7.0% | 30 years |
| Base | 4% | 80% | 6.5% | 30 years |
| High equity | 6% | 70% | 6.0% | 30 years |

These are modeling assumptions, not facts about the owner. Replace them whenever reliable property-specific inputs exist.

## Remaining balance

For original principal `P`, monthly rate `r`, total payments `n`, and elapsed payments `k`:

`balance = P × ((1+r)^n - (1+r)^k) / ((1+r)^n - 1)`

Use zero after the modeled term. If the rate is zero, amortize principal linearly across the term. Do not account for refinances, HELOCs, second mortgages, prepayments or delinquencies without evidence.

## Absentee indicator

Normalize case, punctuation, whitespace and common street suffixes. Preserve apartment/unit identifiers. A mismatch is an indicator, not proof of owner occupancy status.

## Data minimization

Retain only fields needed for the authorized purpose. Do not expose raw PII in chat summaries. Keep exports private and apply the user's retention and deletion requirements.

## Score interpretation

- 75–100: high review priority.
- 50–74: medium review priority.
- 25–49: low review priority.
- 0–24: nurture, enrich or exclude according to the authorized workflow.

The score ranks records under the configured rules. It is not a probability, appraisal, credit score or indication that the owner wants to sell.
