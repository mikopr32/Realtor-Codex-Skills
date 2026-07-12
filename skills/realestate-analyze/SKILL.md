---
name: realestate-analyze
description: Ejecuta un análisis integral de una propiedad mediante especialistas de comparables, renta, vecindario, mercado e inversión organizados en oleadas dependientes; reconcilia un Property Profile y Source Ledger antes de calcular un Property Score y una recomendación. Usar para `/realestate analyze`, full property analysis, property report o evaluación multidimensional de compra e inversión.
---

# Full Property Analysis Orchestrator

Act as the flagship property analysis engine. Orchestrate specialists in dependency-aware waves, reconcile their evidence and calculations, compute a composite Property Score without concealing uncertainty, and assemble a unified report.

**DISCLAIMER: For educational/research purposes only. Not financial or investment advice. Always consult licensed real estate professionals.**

---

## Execution Flow

This skill runs in **three sequential phases**:

### Phase 1: Property Discovery

Before launching any agents, gather the foundational property data that every subagent needs.

**Step 1.1 — Primary Property Search**

Use available browsing or connected data tools to locate current listing and public-record evidence. Record source, effective date, consulted date and confidence; do not assume a specific tool exists.

**Step 1.2 — Extract Core Property Profile**

From the search results, extract and confirm these data points:

| Field | Description | Example |
|-------|-------------|---------|
| Full Address | Street, City, State, ZIP | 123 Oak St, Austin, TX 78701 |
| List Price / Last Sale Price | Current asking or most recent sale | $425,000 |
| Bedrooms | Number of bedrooms | 3 |
| Bathrooms | Full and half baths | 2 full, 1 half |
| Square Footage | Living area in sq ft | 1,850 sq ft |
| Lot Size | Land area | 0.18 acres / 7,841 sq ft |
| Year Built | Original construction year | 1998 |
| Property Type | SFR, Condo, Multi-family, etc. | Single Family Residence |
| Stories | Number of levels | 2 |
| Garage | Type and capacity | 2-car attached |
| HOA | Monthly HOA fees if applicable | $0 / $150/mo |
| Zoning | Residential, commercial, mixed | R-1 Residential |
| Tax Assessment | County assessed value | $385,000 |
| Annual Property Tax | Current year taxes | $7,200 |

**Step 1.3 — Property Type Detection**

Classify the property to tailor the analysis:

- **Single Family Residence** — Focus on comps, rental yield, appreciation, school district, flip potential
- **Multi-Family (2-4 units)** — Focus on gross rent multiplier, unit mix, per-unit value, house hacking
- **Multi-Family (5+ units)** — Focus on NOI, cap rate, expense ratio, value-add opportunity
- **Condo/Townhouse** — Focus on HOA impact on cash flow, special assessments, rental restrictions
- **Land** — Focus on zoning, buildability, utilities access, entitlements
- **Short-Term Rental** — Focus on ADR, occupancy rate, seasonality, local regulations

If any critical data point is missing after discovery, note it as "Not Available" and instruct subagents to work with what is known.

---

### Phase 2: Launch dependency-aware specialist waves

After discovery, use subagents only when available and permitted. Otherwise perform the same roles sequentially and do not claim delegation.

**Wave 1 — independent evidence:** launch comps, rental, neighborhood and market specialists in parallel. Give each the same immutable Property Profile, effective date and authorization boundary.

**Reconciliation barrier:** centralize address/specs, asking price, taxes, HOA, market value/ARV, rent low/base/high, market geography and source conflicts. No downstream investment calculation may start before this barrier.

**Wave 2 — dependent analysis:** launch the investment specialist with reconciled values and rent assumptions. It must consume those inputs rather than researching replacements.

**Wave 3 — validation and synthesis:** verify units, formulas, dates, definitions and conflicts. Weighted scoring is allowed only after reconciliation.

Require every specialist to return `VERIFIED_FACTS`, `CALCULATIONS`, `ASSUMPTIONS`, `METHOD`, `SOURCES`, `EFFECTIVE_DATE`, `CONFIDENCE`, `RISKS` and `UNKNOWNS`.

The orchestrator owns a reconciliation payload:

```text
SELECTED_VALUE:
VALUE_TYPE:
SOURCE_IDS:
EFFECTIVE_DATE:
METHOD:
OWNER:
CONFIDENCE:
CONFLICT_STATUS:
REJECTED_ALTERNATIVES:
RESOLUTION_REASON:
```

Maintain a Source Ledger with `CLAIM_ID`, claim, value, unit, geography, source URL, effective date, consulted date, method, specialist owner, confidence and conflict status. Resolve conflicts by identity, definition, geography, period, authority and method; preserve unresolved alternatives and lower confidence.

---

#### Agent 1: Comparable Sales Analysis (realestate-comps)

```
Specialist handoff example (adapt to the available subagent mechanism):
  description: "Run comparable sales analysis for [ADDRESS]",
  prompt: "You are a real estate comps analyst. Analyze comparable sales for this property:

PROPERTY PROFILE:
- Address: [ADDRESS]
- Price: [PRICE]
- Beds/Baths: [BEDS]/[BATHS]
- Sq Ft: [SQFT]
- Lot Size: [LOT]
- Year Built: [YEAR]
- Property Type: [TYPE]

INSTRUCTIONS:
1. Use available research tools to find 5-10 recent comparable sales within an appropriate market radius
2. Filter for similar sqft (within 20%), similar bed/bath count, sold within last 6 months
3. Calculate median price per sq ft from comps
4. Apply adjustments for: sqft difference, age, condition, lot size, garage, pool, renovations
5. Determine estimated fair market value
6. Assess whether property is overpriced, fairly priced, or underpriced
7. Calculate a Comps Score (0-100) across 5 sub-dimensions:
   - Data Quality (0-20): How many quality comps found, recency, proximity
   - Price Alignment (0-20): How close listing price is to comp-adjusted value
   - Comp Relevance (0-20): How similar the comps are to subject property
   - Market Trend (0-20): Whether recent sales show rising, flat, or falling prices
   - Value Assessment (0-20): Overall value proposition at current price

Output your findings in a structured format with all comps listed in a table, adjustments shown, and final Comps Score with breakdown.

DISCLAIMER: For educational/research purposes only. Not financial or investment advice."
)
```

---

#### Agent 2: Rental Income & Cash Flow (realestate-rental)

```
Specialist handoff example (adapt to the available subagent mechanism):
  description: "Run rental income analysis for [ADDRESS]",
  prompt: "You are a rental income analyst. Project rental income and cash flow for this property:

PROPERTY PROFILE:
- Address: [ADDRESS]
- Price: [PRICE]
- Beds/Baths: [BEDS]/[BATHS]
- Sq Ft: [SQFT]
- Property Type: [TYPE]
- Annual Property Tax: [TAX]
- HOA: [HOA]

INSTRUCTIONS:
1. Use available research tools to find comparable rental listings within an appropriate market radius
2. Estimate monthly rent based on rental comps
3. Calculate vacancy rate (use local market data, default 5-8% if unavailable)
4. Build a full expense model:
   - Property management: 8-10% of gross rent
   - Maintenance reserve: 5-10% of gross rent
   - Insurance: estimate based on property value and location
   - Property taxes: use actual tax amount
   - HOA fees: if applicable
   - CapEx reserve: 5% of gross rent for major repairs
5. Calculate key metrics:
   - Gross Rental Income (annual)
   - Net Operating Income (NOI)
   - Monthly Cash Flow (with and without mortgage at current rates)
   - Cap Rate (NOI / Purchase Price)
   - Cash-on-Cash Return (annual cash flow / cash invested with 20% down)
   - Gross Rent Multiplier (Purchase Price / Annual Gross Rent)
   - DSCR (NOI / Annual Debt Service)
6. Run 3 scenarios: Conservative, Moderate, Optimistic
7. Calculate Rental Score (0-100)

Output all calculations with clear tables and scenario comparison.

DISCLAIMER: For educational/research purposes only. Not financial or investment advice."
)
```

---

#### Agent 3: Neighborhood Analysis (realestate-neighborhood)

```
Specialist handoff example (adapt to the available subagent mechanism):
  description: "Run neighborhood analysis for [ADDRESS]",
  prompt: "You are a neighborhood research analyst. Evaluate the neighborhood and surroundings for this property:

PROPERTY PROFILE:
- Address: [ADDRESS]
- City/State: [CITY], [STATE]
- ZIP Code: [ZIP]

INSTRUCTIONS:
1. Use available research tools to investigate the following for this specific neighborhood:
   a. SCHOOLS: Find nearby schools (elementary, middle, high), their ratings (GreatSchools or similar), distance from property
   b. SAFETY: Crime statistics, crime trends, safety ratings for the area
   c. WALKABILITY: Walk Score, Transit Score, Bike Score, nearby amenities (grocery, restaurants, parks, gyms)
   d. DEMOGRAPHICS: Median household income, population growth, age distribution, owner-occupied vs renter ratio
   e. GROWTH: New development projects, infrastructure improvements, employer expansions, rezoning activity
   f. AMENITIES: Proximity to major employers, hospitals, shopping centers, highways, airports, public transit

2. Score each dimension (0-20 points each):
   - School Quality (0-20)
   - Safety & Crime (0-20)
   - Walkability & Amenities (0-20)
   - Demographics & Economy (0-20)
   - Growth Trajectory (0-20)

3. Calculate overall Neighborhood Score (0-100)

4. Identify the top 3 neighborhood strengths and top 3 concerns

DISCLAIMER: For educational/research purposes only. Not financial or investment advice."
)
```

---

#### Agent 4: Investment Analysis (realestate-invest)

```
Specialist handoff example (adapt to the available subagent mechanism):
  description: "Run investment analysis for [ADDRESS]",
  prompt: "You are a real estate investment analyst. Evaluate this property across three investment strategies:

PROPERTY PROFILE:
- Address: [ADDRESS]
- Price: [PRICE]
- Beds/Baths: [BEDS]/[BATHS]
- Sq Ft: [SQFT]
- Year Built: [YEAR]
- Property Type: [TYPE]
- Reconciled Market Value Range: [VALUE_LOW / BASE / HIGH + SOURCE_IDS]
- Reconciled ARV Range: [ARV_LOW / BASE / HIGH + SOURCE_IDS]
- Reconciled Monthly Rent: [RENT_LOW / BASE / HIGH + SOURCE_IDS]
- Reconciled Operating Costs: [TAX / INSURANCE / HOA / OTHER]
- Financing Assumptions: [DOWN PAYMENT / RATE / TERM / COSTS]
- Reconciled Market Assumptions: [APPRECIATION_LOW / BASE / HIGH + EFFECTIVE_DATE + CONFIDENCE]

INSTRUCTIONS:
Analyze the property under 3 strategies:

STRATEGY 1 — BUY & HOLD:
- 5-year and 10-year projections using only the reconciled appreciation assumptions
- Equity buildup through mortgage paydown
- Total return: cash flow + appreciation + equity buildup + tax benefits
- Tax benefits: depreciation (cost basis / 27.5 years for residential)

STRATEGY 2 — BRRRR (Buy, Rehab, Rent, Refinance, Repeat):
- Use the reconciled ARV range; flag a challenge to the orchestrator instead of replacing it
- Estimate rehab costs by category (kitchen, bath, flooring, paint, exterior, systems)
- Calculate refinance amount (75% of ARV)
- Determine cash left in deal after refinance
- Calculate infinite return potential (cash out >= cash in)

STRATEGY 3 — FIX & FLIP:
- Use the reconciled ARV range for a fully renovated property
- Estimate total rehab budget by category
- Holding costs: mortgage, insurance, taxes, utilities during rehab (assume 4-6 months)
- Selling costs: agent commissions (5-6%), closing costs (1-2%)
- Calculate net profit and profit margin
- Determine if the deal meets the 70% rule (Purchase + Rehab <= 70% of ARV)

For each strategy, provide a feasibility score (0-100).
Calculate overall Investment Score (0-100) as weighted average of strategy scores.

Include break-even timeline for Buy & Hold.

Do not independently research replacement rent, ARV, market value or appreciation. If an input appears inconsistent, return `INPUT_CHALLENGE` with evidence and stop the affected calculation until the orchestrator resolves it.

DISCLAIMER: For educational/research purposes only. Not financial or investment advice."
)
```

---

#### Agent 5: Market Conditions (realestate-market)

```
Specialist handoff example (adapt to the available subagent mechanism):
  description: "Run local market analysis for [ADDRESS]",
  prompt: "You are a real estate market analyst. Evaluate the local market conditions for this property's area:

PROPERTY PROFILE:
- Address: [ADDRESS]
- City/State: [CITY], [STATE]
- ZIP Code: [ZIP]
- Property Type: [TYPE]

INSTRUCTIONS:
1. Use available research tools to investigate current market conditions for this specific area:
   a. INVENTORY: Active listings count, months of supply, new listings trend
   b. PRICING: Median home price, price trends (3-month, 6-month, 12-month), price per sq ft trends
   c. DEMAND: Average days on market, list-to-sale price ratio, multiple offer frequency
   d. ECONOMIC: Local employment trends, major employers, job growth, population growth
   e. INTEREST RATES: Current mortgage rates, rate trend direction, impact on buying power
   f. SEASONALITY: Current market season, best/worst times to buy or sell in this market

2. Determine market classification:
   - Strong Seller's Market (< 2 months supply, prices rising, < 14 days on market)
   - Seller's Market (2-3 months supply, prices stable/rising)
   - Balanced Market (4-6 months supply)
   - Buyer's Market (6-8 months supply, prices flat/falling)
   - Strong Buyer's Market (> 8 months supply, prices falling)

3. Score each dimension (0-20 points each):
   - Supply & Demand Balance (0-20)
   - Price Trend Strength (0-20)
   - Economic Fundamentals (0-20)
   - Market Momentum (0-20)
   - Buyer/Investor Favorability (0-20)

4. Calculate overall Market Score (0-100)

5. Provide 6-month and 12-month market outlook

DISCLAIMER: For educational/research purposes only. Not financial or investment advice."
)
```

---

### Phase 3: Synthesis & Report Assembly

After Wave 1 is reconciled and the dependent investment analysis returns, validate and synthesize the unified report.

**Step 3.1 — Collect Scores**

Extract the score from each agent:

| Agent | Score | Weight |
|-------|-------|--------|
| Comps (Value & Comps) | [0-100] | 25% |
| Rental (Income Potential) | [0-100] | 20% |
| Neighborhood (Quality) | [0-100] | 20% |
| Investment (Upside) | [0-100] | 20% |
| Market (Conditions) | [0-100] | 15% |

**Step 3.2 — Calculate Composite Property Score**

```
Composite Score = (Comps Score x 0.25) + (Rental Score x 0.20) + (Neighborhood Score x 0.20) + (Investment Score x 0.20) + (Market Score x 0.15)
```

**Step 3.3 — Assign Property Grade**

| Score | Grade | Signal |
|-------|-------|--------|
| 85-100 | A+ | Strong Buy — excellent value across all dimensions |
| 70-84 | A | Buy — favorable fundamentals with manageable risks |
| 55-69 | B | Hold/Watch — mixed signals, needs deeper due diligence |
| 40-54 | C | Caution — significant concerns in one or more areas |
| 25-39 | D | Pass — unfavorable risk/reward at current pricing |
| 0-24 | F | Avoid — major red flags, walk away |

**Step 3.4 — Risk Assessment**

Compile risks identified by all agents into a unified risk matrix:

| Risk | Severity | Likelihood | Impact | Mitigation |
|------|----------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Description] | [Action] |
| [Risk 2] | ... | ... | ... | ... |

**Step 3.5 — Generate Final Recommendation**

Based on the composite score, grade, and risk assessment, write:
- A clear BUY / WATCH / PASS recommendation
- Top 3 reasons supporting the recommendation
- Suggested offer price (if Buy) based on comps analysis
- Key conditions or contingencies to include
- Next steps for the buyer/investor

---

## Output Template

Save the final report to `PROPERTY-ANALYSIS-[ADDRESS].md` where `[ADDRESS]` is the street address with spaces replaced by hyphens and special characters removed (e.g., `PROPERTY-ANALYSIS-123-Oak-St-Austin-TX.md`).

```markdown
# Property Analysis Report: [FULL ADDRESS]

> **Generated:** [DATE] | **Property Score:** [SCORE]/100 or `INCOMPLETE` | **Grade:** [GRADE or NOT ASSIGNED] | **Signal:** [SIGNAL or EVIDENCE INCOMPLETE]

**DISCLAIMER: For educational/research purposes only. Not financial or investment advice. Always consult licensed real estate professionals.**

---

## Executive Summary

[2-3 paragraph narrative summary covering:
- What this property is (type, size, location, price)
- The overall assessment (strengths, concerns, opportunity)
- The bottom-line recommendation and why]

---

## Property Profile

| Detail | Value |
|--------|-------|
| Address | [Full address] |
| List Price | [Price] |
| Beds / Baths | [Beds] / [Baths] |
| Square Footage | [Sq ft] |
| Lot Size | [Lot size] |
| Year Built | [Year] |
| Property Type | [Type] |
| Stories | [Stories] |
| Garage | [Garage] |
| HOA | [HOA or N/A] |
| Annual Taxes | [Tax amount] |
| Price per Sq Ft | [Calculated] |

---

## Score Dashboard

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Value & Comps | [X]/100 | 25% | [X x 0.25] |
| Income Potential | [X]/100 | 20% | [X x 0.20] |
| Neighborhood Quality | [X]/100 | 20% | [X x 0.20] |
| Investment Upside | [X]/100 | 20% | [X x 0.20] |
| Market Conditions | [X]/100 | 15% | [X x 0.15] |
| **Composite Score** | | | **[TOTAL]/100** |

**Property Grade: [GRADE]** — [SIGNAL DESCRIPTION]

---

## Comparable Sales Analysis

[Full comps findings from Agent 1]

### Comparable Sales Table

| # | Address | Price | Sq Ft | $/Sq Ft | Beds | Baths | Sold Date | Distance |
|---|---------|-------|-------|---------|------|-------|-----------|----------|
| 1 | ... | ... | ... | ... | ... | ... | ... | ... |

### Adjustment Analysis
[Price adjustments and fair market value estimate]

### Comps Score Breakdown
[5 sub-dimension scores]

---

## Rental Analysis

[Full rental findings from Agent 2]

### Rental Comps
[Comparable rental listings]

### Cash Flow Projection

| Metric | Conservative | Moderate | Optimistic |
|--------|-------------|----------|------------|
| Monthly Rent | ... | ... | ... |
| Vacancy | ... | ... | ... |
| Gross Income | ... | ... | ... |
| Total Expenses | ... | ... | ... |
| NOI | ... | ... | ... |
| Monthly Cash Flow | ... | ... | ... |
| Cap Rate | ... | ... | ... |
| Cash-on-Cash | ... | ... | ... |
| GRM | ... | ... | ... |
| DSCR | ... | ... | ... |

---

## Neighborhood Report

[Full neighborhood findings from Agent 3]

### Scores
[School, safety, walkability, demographics, growth scores]

### Strengths & Concerns
[Top 3 of each]

---

## Investment Analysis

[Full investment findings from Agent 4]

### Strategy Comparison

| Metric | Buy & Hold | BRRRR | Fix & Flip |
|--------|-----------|-------|------------|
| Feasibility Score | .../100 | .../100 | .../100 |
| Total Investment | ... | ... | ... |
| Projected Return | ... | ... | ... |
| Timeline | ... | ... | ... |
| Risk Level | ... | ... | ... |

### 5-Year & 10-Year Projections
[Tables with year-by-year projections]

---

## Market Conditions

[Full market findings from Agent 5]

### Market Classification
[Seller's/Buyer's/Balanced with supporting data]

### Market Outlook
[6-month and 12-month projections]

---

## Risk Assessment

| # | Risk | Severity | Likelihood | Impact | Mitigation |
|---|------|----------|------------|--------|------------|
| 1 | ... | ... | ... | ... | ... |

---

## Recommendation

### Signal: [BUY / WATCH / PASS]

[Clear recommendation narrative with:
- Top 3 supporting reasons
- Suggested offer price (if Buy)
- Key contingencies
- Next steps]

---

*Report generated by AI Real Estate Analyst. This analysis is for educational and research purposes only. Not financial or investment advice. Always verify all data and consult licensed real estate professionals before making any decisions.*
```

---

## Error Handling

- If available research tools return no listing data, ask the user for the minimum property details required
- If a specialist fails, mark the composite score `INCOMPLETE`. Do not renormalize weights. Do not issue a final grade or Buy/Strong Buy signal when any dimension is missing; use conditional language, show the partial weighted contribution separately and explain what is required to complete the grade.
- If fewer than 3 comps are found, flag the Comps Score as "Low Confidence" and note in the Executive Summary
- Always disclose data limitations in the report

## Performance Notes

- Phase 1 duration depends on source access and verification depth; do not promise a fixed time.
- Wave 1 may run in parallel; Wave 2 waits for reconciled comps, rent and market inputs. Do not promise a fixed duration.
- Synthesis duration depends on conflicts, missing data and validation iterations; do not promise a fixed runtime.

**DISCLAIMER: For educational/research purposes only. Not financial or investment advice. Always consult licensed real estate professionals.**
