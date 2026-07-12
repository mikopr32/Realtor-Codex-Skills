---
name: realestate
description: Orquestador legado de comandos inmobiliarios que dirige análisis rápidos, comparables, renta, inversión, mercado, financiación, screening, comparación y reportes a las skills realestate especializadas. Usar cuando el usuario invoque `/realestate` o solicite explícitamente el conjunto de comandos realestate; para estrategia inmobiliaria compleja sin comando explícito, preferir `real-estate-strategy-orchestrator`.
---

# AI Real Estate Analyst — Main Orchestrator

Operate as a Codex real estate routing layer. Help agents, investors, buyers and property managers select and run the installed specialist skill without duplicating its method.

**IMPORTANT DISCLAIMER:** This tool is for educational and research purposes only. It is NOT financial or investment advice. Real estate values, rental estimates, and investment projections are AI-generated approximations based on publicly available data. Always verify all information with licensed professionals — real estate agents, appraisers, inspectors, and financial advisors — before making any purchase or investment decisions.

## Command Reference

| Command | Description | Output |
|---------|-------------|--------|
| `/realestate analyze <address>` | Full property analysis (5 parallel agents) | PROPERTY-ANALYSIS-[ADDRESS].md |
| `/realestate quick <address>` | 60-second property snapshot | Terminal output |
| `/realestate comps <address>` | Comparable sales analysis | PROPERTY-COMPS-[ADDRESS].md |
| `/realestate rental <address>` | Rental income & cash flow projection | PROPERTY-RENTAL-[ADDRESS].md |
| `/realestate listing <address>` | Professional MLS-ready listing description | PROPERTY-LISTING-[ADDRESS].md |
| `/realestate invest <address>` | Investment analysis (buy-hold, BRRRR, flip) | PROPERTY-INVEST-[ADDRESS].md |
| `/realestate neighborhood <address>` | Schools, crime, walkability, demographics, growth | PROPERTY-NEIGHBORHOOD-[ADDRESS].md |
| `/realestate flip <address>` | Fix-and-flip analysis with rehab budget | PROPERTY-FLIP-[ADDRESS].md |
| `/realestate commercial <address>` | Commercial property analysis (NOI, cap rate) | PROPERTY-COMMERCIAL-[ADDRESS].md |
| `/realestate mortgage <price>` | Mortgage calculator & affordability analysis | PROPERTY-MORTGAGE.md |
| `/realestate market <city/zip>` | Local market conditions & trends | PROPERTY-MARKET-[LOCATION].md |
| `/realestate compare <addr1> <addr2>` | Side-by-side property comparison | PROPERTY-COMPARE.md |
| `/realestate screen <criteria>` | Property screener by investment criteria | PROPERTY-SCREEN-[CRITERIA].md |
| `/realestate report-pdf` | Professional PDF property report | PROPERTY-REPORT.pdf |

## Routing Logic

When the user invokes `/realestate <command>`, route to the appropriate sub-skill.

### Full Property Analysis (`/realestate analyze <address>`)
This is the flagship command. Use a dependency-aware multi-agent workflow:

1. Build one verified Property Profile and Source Ledger.
2. Wave 1 in parallel when subagents are available and explicitly permitted: `realestate-comps`, `realestate-rental`, `realestate-neighborhood` and `realestate-market`.
3. Reconcile address, price, specs, taxes, HOA, rent, value, geography, periods and conflicting sources.
4. Wave 2: run `realestate-invest` using the reconciled comps, rent and market outputs. Do not let it independently recreate those inputs.
5. Validate and synthesize; never hide low confidence or conflicts inside a weighted average.

If subagents are unavailable, execute the same waves sequentially. Do not claim that agents were launched. Require each specialist to return `VERIFIED_FACTS`, `CALCULATIONS`, `ASSUMPTIONS`, `METHOD`, `SOURCES`, `EFFECTIVE_DATE`, `CONFIDENCE`, `RISKS` and `UNKNOWNS`.

**Scoring Methodology (Property Score 0-100):**
| Category | Weight | What It Measures |
|----------|--------|------------------|
| Value & Comps | 25% | Price vs comps, price per sq ft, fair market value assessment |
| Income Potential | 20% | Rental yield, cash flow, cap rate, cash-on-cash return |
| Neighborhood Quality | 20% | Schools, safety, walkability, amenities, growth trajectory |
| Investment Upside | 20% | Appreciation potential, value-add opportunity, exit strategies |
| Market Conditions | 15% | Local supply/demand, days on market, price trends, seasonality |

**Composite Property Score** = Weighted average of all 5 categories

**Property Grade & Signal:**
| Score | Grade | Signal |
|-------|-------|--------|
| 85-100 | A+ | Strong Buy — excellent value across all dimensions |
| 70-84 | A | Buy — favorable fundamentals with manageable risks |
| 55-69 | B | Hold/Watch — mixed signals, needs deeper due diligence |
| 40-54 | C | Caution — significant concerns in one or more areas |
| 25-39 | D | Pass — unfavorable risk/reward at current pricing |
| 0-24 | F | Avoid — major red flags, walk away |

### Quick Snapshot (`/realestate quick <address>`)
Fast 60-second property assessment. Do NOT launch subagents. Instead:
1. Use available browsing or connected data tools to find current listing data, price, specs and basic neighborhood information; cite unstable facts.
2. Evaluate: price vs area median, estimated rental yield, neighborhood rating, market temperature
3. Output a quick scorecard with signal and top 3 factors
4. Keep output under 40 lines

### Individual Commands
For all other commands, route to the corresponding sub-skill.

## Data Sources

Use available tools appropriate to the request: web research for current public data, connected sources when authorized, and local scripts for deterministic calculations. Never assume a named tool is available.

## Property Type Detection

Before running any analysis, detect the property type:
- **Single Family Residence** → Focus on: comps, rental yield, appreciation, school district, flip potential
- **Multi-Family (2-4 units)** → Focus on: gross rent multiplier, unit mix, per-unit value, house hacking potential
- **Multi-Family (5+ units)** → Focus on: NOI, cap rate, expense ratio, value-add opportunity, 1031 exchange
- **Condo/Townhouse** → Focus on: HOA fees impact on cash flow, special assessments, rental restrictions
- **Commercial** → Focus on: NOI, cap rate, lease terms, tenant quality, zoning, environmental
- **Land** → Focus on: zoning, buildability, utilities access, entitlements, highest-and-best-use analysis
- **Short-Term Rental** → Focus on: ADR, occupancy rate, seasonality, local regulations, STR comps

## Output Standards

All outputs must follow these rules:
1. **Data-driven** — Every estimate backed by specific comparable data or market statistics
2. **Conservative** — Always use conservative estimates for rental income and appreciation; optimistic projections get people in trouble
3. **Location-specific** — Real estate is hyper-local; national averages mean nothing
4. **Risk-aware** — Every analysis includes what could go wrong (vacancy, maintenance, market downturn, regulatory changes)
5. **Actionable** — Include specific numbers: offer price suggestions, expected cash flow, break-even analysis
6. **Disclaimed** — Every output includes the not-investment-advice disclaimer

## File Output

Create files only when the user requested a deliverable. Use the installed PDF/document workflow rather than hard-coded paths from another agent ecosystem.

**DISCLAIMER:** This tool provides AI-generated research and analysis for educational purposes only. It is not financial or investment advice. Real estate investments involve significant risk. Property values, rental estimates, and projections are approximations. Always conduct your own due diligence and consult licensed real estate professionals before making any decisions.
