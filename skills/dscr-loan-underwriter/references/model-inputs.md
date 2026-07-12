# DSCR model inputs

Provide a JSON object to `scripts/dscr_model.py`.

## Required

- `purchase_price`
- `annual_interest_rate` as decimal
- `term_years`
- `target_dscr`
- At least one of `loan_amount`, `down_payment_amount`, or `ltv`
- At least one rent scenario: `rent_low`, `rent_base`, or `rent_high`

## Monthly housing costs

- `property_tax`
- `hazard_insurance`
- `flood_insurance`
- `hoa`
- `mortgage_insurance`
- `other_housing_costs`

Do not duplicate escrowed taxes or insurance.

## Property economics

- `vacancy_rate`
- `monthly_other_income`
- `monthly_management`
- `monthly_maintenance`
- `monthly_capex`
- `monthly_leasing`
- `monthly_owner_utilities`
- `monthly_other_operating_expenses`

Taxes, insurance, flood and HOA are treated as operating expenses for property-level NOI and as housing costs for modeled lender DSCR. P&I is debt service, not an operating expense.

## Interpretation

The calculator models arithmetic only. It does not decide which rent or expense a lender accepts. Record the product matrix and source separately.
