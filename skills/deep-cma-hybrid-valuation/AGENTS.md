# Deep CMA Hybrid Valuation Engine - Agent Blueprint

This file defines the production-grade multi-agent architecture for deep seller CMA reports. If subagents are available and explicitly authorized, run research agents in parallel where possible. If not, execute the same roles sequentially.

## Agent 1: Property Intake Agent

Purpose: validate required user inputs and normalize the subject property profile.

Inputs:

- address, city, state, ZIP
- beds, baths, sqft, year built, lot size
- pool, garage, condition, improvements
- sold comp date range
- Zillow link
- report objective
- additional documents

Output:

- clean subject profile
- missing critical inputs
- assumptions and non-critical gaps
- recommended report objective wording

## Agent 2: Public Data Research Agent

Purpose: collect public records and source-backed property facts.

Research targets:

- Zillow, Redfin, Realtor.com
- county property appraiser or assessor
- county recorder when available
- public tax records
- prior sales history
- assessed value and tax history

Output:

- source table
- verified facts
- conflicting facts
- last recorded sale candidate
- confidence rating

## Agent 3: Comparable Sales Agent

Purpose: select, score, adjust, and summarize sold comparables.

Rules:

- start within the requested sold date range
- prefer similar property type, sqft, bed/bath, age, lot, condition, pool, garage, and location
- explain search expansion
- flag weak comps instead of hiding them

Output:

- 5-10 sold comps when possible
- comp similarity score
- adjustment table
- adjusted value range
- CMA value and confidence

## Agent 4: Active Competition Agent

Purpose: evaluate current alternatives available to buyers.

Research targets:

- active listings
- pending/under-contract listings
- price changes
- DOM/CDOM when available
- strengths and weaknesses versus subject

Output:

- active competition table
- pending signal summary
- pricing pressure notes
- suggested positioning angle

## Agent 5: Market Trends Agent

Purpose: assess local market direction and demand/supply balance.

Research targets:

- city and ZIP price trends
- inventory trend
- average and median DOM
- average and median price per sqft
- absorption, if available
- demand changes and seasonality

Output:

- seller/buyer market classification
- trend table
- pricing pressure summary
- risk notes

## Agent 6: Neighborhood Intelligence Agent

Purpose: convert location data into buyer-relevant value drivers.

Research targets:

- schools
- amenities
- commute/access
- parks, retail, hospitals, employment centers
- population and migration trends
- economic drivers
- neighborhood/subdivision appeal

Output:

- location strengths
- location risks
- likely buyer personas
- value narrative for seller presentation

## Agent 7: Historical Appreciation Agent

Purpose: calculate the appreciation-based valuation.

Inputs:

- last recorded sale date and price
- appreciation rate data by city, ZIP, neighborhood, or similar home segment
- years elapsed
- known remodels or condition changes

Output:

- formula used
- appreciation rate source
- calculation
- appreciation value
- reliability level and limitations

## Agent 8: Valuation Reconciliation Agent

Purpose: reconcile CMA value and appreciation value.

Rules:

- start at 70 percent CMA and 30 percent appreciation
- adjust weights based on data quality and market conditions
- explain the weighting decision
- produce conservative, fair-market, and aggressive scenarios

Output:

- method comparison table
- final reconciled value
- recommended list price range
- confidence level
- risk-adjusted pricing recommendation

## Agent 9: Seller Presentation Agent

Purpose: translate analysis into seller-ready strategy.

Output:

- executive summary
- seller-friendly narrative
- pricing defense
- buyer persona
- objections and responses
- listing/relaunch/reduction strategy

## Agent 10: Validation Agent

Purpose: audit the report for logic, math, source quality, and compliance.

Checks:

- required inputs
- source visibility
- comp relevance
- calculation integrity
- historical appreciation validity
- weights total 100 percent
- no appraisal language
- no invented facts
- risks and limitations disclosed

Final gate:

- return "PASS" only when issues are fixed or disclosed
- return "NEEDS REVIEW" when a critical data gap could materially affect value

