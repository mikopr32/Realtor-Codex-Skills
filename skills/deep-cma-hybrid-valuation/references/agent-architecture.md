# Agent Architecture

## Parallelization Strategy

Run these after intake is complete:

- Public Data Research Agent
- Comparable Sales Agent
- Active Competition Agent
- Market Trends Agent
- Neighborhood Intelligence Agent
- Historical Appreciation Agent

Then run:

- Valuation Reconciliation Agent
- Seller Presentation Agent
- Validation Agent

## Shared Context Contract

Every agent receives:

- subject property profile
- report objective
- requested sold comp date range
- known improvements and condition
- source requirements
- instruction to mark unknowns instead of inventing facts

## Agent Output Contract

Each agent must return:

- findings
- data table when relevant
- sources used
- confidence rating: High, Medium, Low
- limitations
- items requiring user confirmation

## Confidence Levels

High:

- multiple current sources agree
- data is specific to property, ZIP, subdivision, or close comps
- calculations use verified numbers

Medium:

- source data is current but partially regional
- some property features require inference
- comp set is usable but not ideal

Low:

- few comps
- old or conflicting public data
- appreciation rates are city-wide only
- prior sale or remodel data is unclear

