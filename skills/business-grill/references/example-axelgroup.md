# Example: AxelGroup analytics offer

This is an illustrative application, not a current factual assessment of AxelGroup.

## Initial hypothesis

> AxelGroup should build a custom analytics platform for small B2B websites and sell revenue-attribution insights.

## Reframed decision

> Should the owner fund a custom platform now, or first validate a delegated monthly service that turns existing Plerdy/PostHog evidence into prioritized website decisions?

## Claim map

| Claim | Type | Evidence interpretation |
|---|---|---|
| Existing tools can collect pageviews, autocapture, heatmaps, scroll depth, and sometimes session replay | Observed fact if verified in the prototype/tools | Evidence of available inputs, not demand for a new platform |
| Clients will pay for prioritized recommendations | Assumption | Requires buyer behavior, not a feature demo |
| Revenue attribution is possible | Assumption | Unsupported when there is no real CRM/lead receiver or reconciled sales data |
| A human analyst can produce a useful monthly decision brief | Testable inference | Can be tested manually before software is built |
| The owner wants leverage rather than becoming the permanent analyst/developer | Decision constraint | Must shape the operating model |

## Frontier round

1. **Question:** Is the first paid outcome a software product or a decision service?
   **Recommendation:** Start as a tightly scoped decision service using existing tools. Yes means accepting this recommendation.
   **Why:** It tests willingness to pay and delivery effort without funding a platform.

2. **Question:** What owner load is acceptable after three months?
   **Recommendation:** Cap the steady-state owner role at pricing, monthly quality review, and exception handling, with a target below 4 hours per week. Yes accepts this target.
   **Why:** Without a cap, the offer can become a consultancy job disguised as a product.

3. **Question:** What proof is enough to justify software?
   **Recommendation:** Require at least 3 paying design partners, two repeat cycles each, a stable analyst workflow, and one repeated manual step consuming at least 30% of delivery time. Yes accepts this gate.
   **Why:** Software should remove proven friction, not anticipate it.

## Provisional score

| Dimension | Score (0–4) | Weighted points | Reason |
|---|---:|---:|---|
| Problem severity | 2 | 7.50 | Plausible but not yet shown as urgent |
| Customer evidence | 1 | 3.75 | Prototype interaction is not buyer evidence |
| Willingness to pay/value | 0 | 0 | No paid commitment supplied |
| Unit economics | 1 | 3.75 | Analyst time and support load unknown |
| Delegability | 2 | 7.50 | A role/SOP is plausible but unproven |
| Distribution | 1 | 2.50 | No repeatable acquisition route supplied |
| Delivery/time-to-learning | 4 | 10 | Manual service can be tested quickly |
| Risk/reversibility | 4 | 5 | A capped manual pilot is reversible |
| **Total** |  | **40/100** | Score for building the platform now |

## Decision

**VALIDATE — medium confidence.** Do not build the platform. Validate the service hypothesis first.

### Bounded test

- Offer: one monthly evidence review with 3 prioritized website decisions.
- Sample: 3 qualified B2B design partners.
- Cap: 30 total delivery hours and no custom backend/CRM.
- Pass: at least 2 partners pay for a second cycle, median delivery time is 6 hours or less, and an analyst other than the owner can follow the checklist.
- Fail/stop: no repeat payment, delivery remains owner-dependent, or clients value raw dashboards more than decisions.
- Next decision: GO to a delegated service; PIVOT the offer/segment; or STOP. Build software only for a repeated measured bottleneck.

## Delegation design

- **Owner-only:** segment, promise, price, risk cap, final quality standard.
- **Delegable:** data extraction, evidence ledger, first-pass diagnosis, report assembly, routine client follow-up.
- **Control:** analyst checklist, evidence citations, three-priority limit, delivery-time metric, monthly exception review.
- **Do not build yet:** CRM, custom event collector, revenue attribution, multi-tenant dashboard, automated recommendation engine.
