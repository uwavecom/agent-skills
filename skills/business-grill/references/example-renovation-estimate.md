# Example: checking a renovation estimate

This fictional example demonstrates method. It is not a benchmark for real Ukrainian prices and not a technical safety certification.

## Initial hypothesis

> Approve a contractor's 480,000 UAH apartment-renovation estimate because the total looks plausible.

## Reframed decision

> Should the owner accept this exact scope, price, payment schedule, and risk allocation now, given the available evidence?

## Read-only extraction

First normalize the estimate without changing it:

| Line | Quantity × rate | Included specification | Evidence status | Question |
|---|---|---|---|---|
| Wall preparation | 320 m² × rate | Material/finish not named | Reported claim, E1–E2 | Does 320 m² reconcile to room measurements and openings? |
| Electrical work | One lump sum | Point count and cable grade absent | Reported claim, E1 | What points, routes, panel work, tests, and certifications are included? |
| Flooring | 74 m² × rate | Underlay/skirting/waste unclear | Partial E2 | Is waste included, and does the area match drawings? |
| Debris removal | One lump sum | Trips/weight/floor access absent | E1 | What triggers a change order? |
| Contingency | 10% | Use and approval undefined | E1 | Who approves use and how is unused value treated? |

The unusual or incomplete lines are reconciliation prompts, not accusations.

## Frontier round

1. **Question:** Is the decision to select a contractor or approve a construction-ready scope?
   **Recommendation:** Treat these as separate gates; shortlist first, then approve only after the scope is measurable. Yes accepts the two-gate approach.

2. **Question:** What payment exposure is acceptable before work is accepted?
   **Recommendation:** Tie payments to measurable milestones and keep a holdback until punch-list completion, subject to local legal advice. Yes accepts this commercial principle.

3. **Question:** Which items need qualified review?
   **Recommendation:** Require appropriate licensed/qualified review for electrical, gas, structural, waterproofing, or other safety-critical work. Yes accepts this safety gate.

## Provisional score

| Dimension | Score (0–4) | Weighted points | Reason |
|---|---:|---:|---|
| Problem severity | 4 | 15 | Renovation need is concrete |
| User evidence | 3 | 11.25 | Scope need exists, but measurements are incomplete |
| Value/price evidence | 1 | 3.75 | One non-normalized quote is weak market evidence |
| Economics/cash exposure | 1 | 3.75 | Change-order and payment risk are undefined |
| Delegability | 2 | 7.50 | Contractor delivery is delegable; oversight controls are incomplete |
| Procurement feasibility | 2 | 5 | Comparable scope-equivalent quotes can be obtained |
| Delivery/time-to-learning | 3 | 7.50 | Measurement reconciliation is fast |
| Risk/reversibility | 1 | 1.25 | Early payment and concealed work can be hard to reverse |
| **Total** |  | **55/100** | Approval decision as currently documented |

## Decision

**VALIDATE — high confidence that approval is premature; low confidence on whether the price itself is fair.**

### Evidence request

- measured bill of quantities with drawings or room measurements;
- named material grades/brands or performance specifications;
- labor/material split;
- inclusions, exclusions, tax, delivery, protection, cleanup, and disposal;
- milestone schedule and acceptance criteria;
- change-order rates and approval rules;
- warranty and responsibility for defects;
- two scope-equivalent comparison quotes or current supplier/labor evidence;
- qualified review of safety-critical items.

### Decision rule

- **GO:** quantities reconcile, scope is complete, safety review passes, commercial terms bound downside, and the total is within the owner's approved range after scope-equivalent comparison.
- **PIVOT:** retain the contractor but revise scope, materials, phasing, or payment terms.
- **STOP:** the contractor will not provide a measurable scope, requires unacceptable advance exposure, or material discrepancies remain unreconciled.

## Delegation design

- **Owner-only:** budget ceiling, finish priorities, contractor selection, exception approvals.
- **Delegable:** quantity check, quote normalization, progress photos, milestone checklist, invoice reconciliation.
- **Control:** one accountable project supervisor, signed scope baseline, change-order log, hold points before concealed work, weekly variance report.
- **Do not automate yet:** price scraping or fraud scoring before the scope and units are normalized.
