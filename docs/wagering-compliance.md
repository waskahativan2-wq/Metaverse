# OSIS Wagering and Gaming Compliance Policy

## Purpose

This policy defines the minimum compliance controls for any OSIS feature that involves wagering, betting, casino-style play, prediction markets, sweepstakes, prizes, fantasy competitions, or convertible virtual currency. It exists so that no real-money or prize-linked gaming is enabled by default, by accident, or without documented lawful approval.

> This is an operational governance policy, not legal advice. Gambling, gaming, lottery, securities, consumer-protection, advertising, payments, and Indigenous-governance requirements are jurisdiction-specific. Obtain qualified legal review for each jurisdiction and each feature before enablement.

## Definitions

- **Wagering feature:** Any feature where a player stakes money, convertible value, or convertible virtual items on an uncertain outcome with the possibility of winning money, prizes, or convertible value. This includes casino games, sports betting, pari-mutuel-style pools, prediction markets with cash-out, and paid fantasy competitions with prizes.
- **Non-wagering feature:** Free-to-play predictions, skill-based competitions with non-cash, non-convertible rewards, and entertainment features where nothing of convertible value is staked or won.
- **Convertible value:** Anything that can be exchanged, directly or indirectly, for money or money's worth — including OSIS Coins if they can be purchased, cashed out, traded, or redeemed for prizes.

## Core rule: disabled by default

1. Every wagering feature is **disabled in all jurisdictions by default**.
2. A wagering feature may be enabled only when **all** of the following are true and recorded:
   - A valid licence, registration, or documented legal basis covers the exact feature in the exact jurisdiction.
   - Qualified legal counsel for that jurisdiction has reviewed and approved enablement in writing.
   - The accountable owner and the legal/compliance reviewer have signed the enablement record.
   - The technical controls in this policy are implemented, tested, and evidenced.
3. A signed or approved wagering record is never overwritten. A material change to the feature, the licence scope, or the jurisdiction list creates a new record version and requires re-review and re-signature, consistent with `docs/records-policy.md`.
4. If any licence expires, is suspended, or is found not to cover the feature, the feature is disabled in the affected jurisdiction immediately and the incident is recorded.
5. Region-level kill switches must be able to disable each wagering feature independently of the rest of the platform.

## Jurisdiction gating

- A wagering feature may be exposed only to players verified to be physically located in a jurisdiction where it is licensed and approved.
- Geolocation controls must be resistant to trivial bypass (VPN, GPS spoofing, emulator), must re-verify location at appropriate intervals, and must fail closed: when location or eligibility cannot be verified, access is denied.
- Where a jurisdiction is not approved, the platform offers only a compliant non-wagering alternative (for example free-to-play predictions with non-cash rewards) and does not upsell or deep-link into the wagering feature.
- Each jurisdiction enablement records the licence reference, licensee entity, regulator, scope, effective date, and expiry date.

## Age, identity, and eligibility

- Age and identity verification is completed **before** any wager is accepted. Verification is proportionate, privacy-preserving, and not trivially bypassable.
- Minimum age is the higher of the platform rule and the jurisdiction's legal requirement. Age-restricted areas remain separated, labelled, and excluded from default discovery.
- Prohibited-person rules are enforced: self-excluded players, cooling-off participants, minors, platform staff and contractors with insider access, athletes/officials/creators for markets they can influence, and any class of person excluded by law or licence condition.
- Accounts used for wagering have MFA, device revocation, session controls, and tested account recovery.

## Separation from gameplay, currency, and minors

- Wagering is kept technically and visually separate from ordinary gameplay, progression, loot, achievements, and the general marketplace.
- Virtual currency or items that can be purchased or cashed out must not flow into or out of wagering features except through a documented, licensed, and audited conversion path approved for that jurisdiction.
- Loot boxes or randomized rewards purchasable with convertible value are treated as wagering-adjacent and are disabled unless separately reviewed and approved.
- No wagering advertising, prompts, or odds are shown to minors, to self-excluded users, or in youth, education, or family areas.

## Responsible gaming controls

- Deposit, loss, wager, and time limits are available, easy to set, and binding. Limit decreases take effect immediately; limit increases take effect only after a cooling-off period where required.
- Self-exclusion and cooling-off are honoured across all OSIS wagering features and are not reversible during the exclusion period.
- Players see transparent odds, house or commission rules, fees, and clear risk information before staking.
- Reality checks, session time displays, and access to responsible-gaming support and complaint routes are provided in the player's language.
- Behavioural data is never used to identify and target vulnerable players for promotion. Profiling for exploitation, urgency-based offers, and misleading promotions are prohibited.

## Integrity and fair play

- Insider betting, match manipulation, collusion, and wagering on markets the bettor can influence are prohibited and monitored.
- Markets use fictional teams and results unless a rights holder has granted written permission.
- Wagering operators, data feeds, and odds providers are licensed or otherwise lawful in the applicable jurisdiction and are under contract with audit and cooperation clauses.
- Suspicious betting patterns are escalated to the regulator, sports governing body, or law enforcement where required, and the platform preserves the relevant evidence under `docs/records-policy.md`.

## Advertising and promotion

- Wagering advertising is truthful, substantiated, age-appropriate, frequency-limited, and clearly distinguishable from gameplay and editorial content.
- Bonus, free-bet, and promotional offers disclose eligibility, wagering requirements, expiry, and jurisdiction restrictions before commitment.
- No advertising targets minors, self-excluded users, or prohibited jurisdictions, and no biometric, psychological, or emotional data is used for wagering promotion without specific legal review and consent.

## Payments and financial crime

- Payment flows for wagering are tested for deposits, withdrawals, refunds, chargebacks, taxes, reconciliation, and sanctions/AML screening, and comply with licence conditions.
- Withdrawal terms, fees, and timelines are disclosed before the first deposit, and winnings are paid within stated timelines.
- Funds belonging to self-excluded or suspended players are handled per law and licence conditions; payment holds are used only where lawful and are documented.

## Records and approval evidence

Each jurisdiction enablement of a wagering feature is preserved as a `wagering_compliance` record following `docs/records-policy.md` and `docs/records-schema.json`, and must include, where applicable:

- licence or legal-basis reference, licensee entity, regulator, scope, effective and expiry dates
- feature identifier, version, and the exact release commit/artifact the enablement applies to
- jurisdiction and age gates, geolocation method, and bypass-resistance test results
- responsible-gaming control test results (limits, self-exclusion, cooling-off, reality checks)
- prohibited-person enforcement test results
- payment, AML, and sanctions-screening test results
- legal review reference and named qualified reviewers
- accountable owner approval with signer identity, role, verification method, and ISO-8601 UTC signing time
- `source_hash`, `previous_hash`, `audit_log_reference`, and `storage_location`
- open exceptions with owner, mitigation, due date, expiry date, and acceptance authority
- rollback/disable trigger and kill-switch test evidence

## Enablement states

- **DISABLED (default):** No licence or approval on file, or any required control is untested or failing. The feature is not reachable by players.
- **PENDING_REVIEW:** Evidence is being collected. The feature remains disabled.
- **ENABLED (jurisdiction-scoped):** All requirements in this policy are met, evidenced, and signed for a specific jurisdiction and feature version. Enablement expires with the licence or the approval record, whichever is sooner.
- **SUSPENDED:** Previously enabled, now disabled due to licence lapse, regulator action, control failure, or incident. Re-enablement requires a new approval record.

## Relationship to launch gates

Wagering features are subject to the release gates in `docs/metaverse-finalization-checklist.md`. Any unresolved wagering compliance item is a critical finding: the release decision for the affected feature and jurisdiction is **No-go** until it is closed or formally accepted by the accountable owner. The final launch approval remains **No-go** while any wagering feature lacks complete licensing, legal review, control evidence, or signed approval for the jurisdictions in scope.

## Policy owner

The OSIS governance lead, compliance steward, or applicable data owner defines implementation details for licence registers, jurisdictional reviews, responsible-gaming thresholds, retention, and periodic review, consistent with `docs/records-policy.md`.
