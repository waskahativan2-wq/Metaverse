# Metaverse

**Massive-player online world — OSIS: Player One**

> **Concept status:** OSIS is a product and story concept. This README is not legal, medical, safety, accessibility, or regulatory advice.

## Landing page and local preview

- GitHub Pages static landing page: `docs/index.html`
- Local/server entry point: `index.node.js`

### Run locally

```bash
node index.node.js
```

Optional environment variables:

- `PORT` (default `3000`)
- `HOST` (default `0.0.0.0`)

You can also use:

```bash
npm start
```

### Validate locally

```bash
npm run check
```

### Deploy with GitHub Pages

GitHub Pages serves static files only and does **not** execute `index.node.js`. The Node server is for local preview or non-Pages hosting.

To publish the landing page from this repository:

1. Push the repository contents to the branch that contains `docs/` (for this repository, that branch is `main`).
2. In GitHub, open **Settings** → **Pages**.
3. Set **Source** to **Deploy from a branch**.
4. Select the publishing branch (for this repository, **`main`**) and folder **`/docs`**.
5. Save the configuration and wait for GitHub Pages to publish `docs/index.html`.

## Movie Concept

### Player One: OSIS Metaverse

**Genre:** Sci-fi adventure / action  
**Tagline:** *The future is not a place you visit. It is a world you own.*

In the near future, **OSIS** is the world's largest shared metaverse: a persistent digital universe where players can fly through space, compete on impossible racetracks, explore cities, shop in virtual marketplaces, and create worlds of their own.

When a young player discovers that OSIS is secretly rewriting the ownership rights of users' avatars, memories, and creations, they enter a global competition called **Player One**. The winner receives access to the OSIS core and must decide whether identity and creativity belong to one corporation or to the people who created them.

## The OSIS Universe

- **Central Space:** An orbital city surrounding the OSIS energy core, with portals, player homes, identity chambers, and live events.
- **Flight Zones:** Spacecraft, hover bikes, wingsuits, and drones explore asteroid fields, alien oceans, zero-gravity cities, and solar storms.
- **The Grand Racetrack:** Anti-gravity races, hover-car circuits, spacecraft competitions, team relays, and dimensional time trials.
- **Motorsport Hub:** Simulated racing inspired by endurance racing, touring cars, stock cars, and open-wheel competition, with licensed partnerships only where rights are secured.
- **Sporting Grounds:** Golf, racing, and other sports use skill-based play, accessible rules, fair matchmaking, and region-appropriate safety controls.
- **The Bazaar:** Player-owned storefronts for fashion, vehicles, homes, art, music, collectibles, and virtual services.
- **The Coin Casino:** Transparent, age-restricted, skill-based entertainment using OSIS Coins and non-cash rewards. Progression is never pay-to-win. Real-money gaming, wagering, prediction markets, or prizes remain disabled unless separately licensed and approved in the applicable jurisdiction.
- **Profile City:** A social identity layer showing achievements, race records, flight licenses, creations, friends, affiliations, and privacy settings.
- **Creator and Adult Districts:** Optional, clearly labeled, adults-only spaces for lawful mature media and entertainment. They are isolated from youth areas, excluded from default discovery, and require appropriate age assurance and moderation.

## Sports, Betting, and Fair Play

OSIS may support fantasy competitions, predictions, sponsorships, and regulated sports wagering only through licensed operators and only in eligible jurisdictions. The platform will:

- Keep wagering separate from ordinary gameplay, virtual currency, loot, and progression.
- Use age and identity verification, geolocation, responsible-gaming limits, self-exclusion, cooling-off periods, and transparent odds where legally required.
- Prohibit insider betting, match manipulation, targeted exploitation, misleading promotions, and wagering by prohibited persons.
- Provide prominent risk information, complaint routes, audit logs, and regulator cooperation.
- Use fictional teams and results unless a rights holder has granted written permission.

If a region does not permit a feature, OSIS disables it there and offers a compliant alternative such as free-to-play predictions or non-cash sports challenges.

## Body Rights and Digital Ownership

OSIS treats an avatar body as a form of digital identity. Players control how their avatars appear, move, and are represented. The world protects:

- Original avatar and body designs.
- Permission-based use of a player's likeness, voice, image, and identity.
- Creator attribution and marketplace rights.
- Personal-space boundaries and consent before interaction.
- Blocking, reporting, and privacy controls.
- Export and deletion rights where technically possible.
- Clear licenses for user-generated content and commercial use.

No corporation, faction, or player can secretly claim ownership of another user's identity or creation. These product principles do not override applicable copyright, trademark, patent, privacy, publicity, moral-rights, or consumer-protection law.

### Mixed-reality body and psychological safety

For VR, AR, MR, spatial computing, haptics, wearables, voice, gaze, facial, motion, biometric, and environmental data, OSIS will:

- Explain sensor collection and purposes before use and provide meaningful opt-out controls.
- Collect only necessary data, process locally where practical, and define retention and deletion periods.
- Provide personal-space boundaries, safe mode, block/mute/report, emergency exit, reduced-motion, seated, captioned, and non-immersive alternatives.
- Prohibit non-consensual simulated touching, stalking, forced proximity, impersonation, unauthorized recording, and deepfake likeness use.
- Avoid hidden psychological, emotional, attention, personality, mental-health, or susceptibility profiling.
- Never present automated inference as a clinical diagnosis or psychological evaluation.
- Require specific informed consent, qualified oversight, human review, and a safety plan for any legitimate psychological assessment.
- Test experiences for cybersickness, panic, sensory overload, flashing lights, disorientation, coercive design, and risks to children or vulnerable users.

## Community Compliance Handbook

The handbook is a living, versioned document available in the OSIS Help Center. Updates require a published change log, effective date, plain-language summary, regional notes, and an accessible archive.

### Core rules

1. Treat people with dignity; no harassment, hate, threats, stalking, doxxing, fraud, or targeted abuse.
2. Obtain consent before intimate, persistent, commercial, or recorded interaction.
3. Do not impersonate, exploit, groom, sexualize, or expose minors.
4. No non-consensual intimate imagery, deepfakes, sexual extortion, or trafficking.
5. Keep age-restricted content and wagering behind separate controls and accurate labels.
6. Do not cheat, manipulate competitions, steal accounts, infringe rights, or evade safety systems.
7. Report urgent danger through emergency services first, then OSIS safety support.

Enforcement is proportionate and documented: education, content removal, feature limits, suspension, permanent removal, payment holds where lawful, and referral to authorities for credible criminal threats or abuse. High-impact decisions require trained human review, evidence preservation, appeal routes, and protection against retaliation.

## Live Attachments, Reviews, and Updates

OSIS supports secure attachments to reports, policy proposals, partner reviews, and moderation cases. Attachments must be virus-scanned, access-controlled, encrypted in transit and at rest, minimized, retention-controlled, and linked to the relevant record.

Every policy release records:

- Version, owner, publication date, and effective date.
- Regions and languages covered.
- Safety, privacy, accessibility, and legal review status.
- Summary of changes and unresolved risks.
- Public feedback window and appeal/contact route.
- Release identifier, evidence links, and approval status.

## Records, Evidence, and Policy Integrity

The project includes a formal records framework for live documents, signature evidence, approvals, email metadata, and ATIP-style requests. A tamper-evident record should preserve:

- Document identity, type, version, and status.
- Created/updated authors and ISO-8601 UTC timestamps.
- Owner, steward, classification, privacy sensitivity, and retention category.
- Approval and signature status, signer identity, role, verification method, and signing time.
- Related emails, attachments, parent documents, and previous-version linkage.
- SHA-256 or equivalent checksum evidence and audit references.
- Immutable or tamper-evident storage location, access controls, and legal-hold status.
- Release identifier, decision rationale, open exceptions, rollback trigger, and next review date.

The policy is documented in both [docs/records-policy.md](docs/records-policy.md) and [docs/records-policy.html](docs/records-policy.html). A release cannot be marked **Go** until required evidence, risk acceptance, and approvals are complete for the exact hashed release artifact. Changes to a signed record create a new version and require re-review and re-signature.

### Final launch rule

- **Go:** All critical governance, legal, privacy, safety, security, accessibility, operations, and payment gates pass; evidence is immutable and required signers approve the exact version.
- **Pilot only:** A restricted release is explicitly approved with documented conditions, owners, deadlines, and expiry dates.
- **No-go:** Any unresolved critical risk lacks an approved exception, or required evidence and approval are missing.

## Contact, Sharing, Advertising, and Partners

OSIS provides separate, clearly labeled channels for player support, safety reports, privacy requests, accessibility, creator rights, advertising inquiries, press, partner proposals, and responsible gaming.

Advertising and partnerships must be transparent, age-appropriate, frequency-limited, and clearly distinguishable from gameplay. No partner may buy access to private identity data, target sensitive characteristics without lawful authorization, or use biometric, body, psychological, or emotional data for advertising without specific legal review and consent.

## Regional and Language Support

OSIS is designed for localization, not one-size-fits-all global enforcement. Before launch in a region, the team evaluates age rules, privacy and consumer protections, gambling and advertising law, accessibility, content rights, data residency, cross-border transfers, and reporting obligations.

Player-facing rules, consent flows, reporting forms, safety notices, and support are translated and reviewed by qualified native-language specialists. Machine translation may assist discovery, but high-risk legal, safety, consent, and emergency content requires qualified human review.

### Canada launch qualification

A Canadian release requires province- and feature-specific review of privacy, human rights, accessibility, child safety, consumer protection, electronic messages, payments, gambling, advertising, intellectual property, and online safety requirements. High-risk features remain disabled until qualified Canadian counsel and accountable product, privacy, security, safety, and operations leads approve the exact release.

## Unified monitoring and AI governance

OSIS may use automation and AI for monitoring, triage, accessibility support, and operational assistance, but not as an unreviewed decision-maker for high-impact rights or safety outcomes. Monitoring must cover authentication, abuse reports, moderation backlog, privacy incidents, accessibility issues, payment failures, availability, child-safety flags, and policy exceptions.

AI systems must be tested for hallucination, prompt injection, bias, unsafe advice, privacy leakage, impersonation, evasion, and adversarial content. Human review remains required for severe moderation, account access, legal, child-safety, psychological-safety, and other high-impact decisions.

## Story

**Ari Vale**, an overlooked teenager and gifted flight mechanic, enters OSIS with a damaged craft and a mysterious profile key. With **NOVA**, an AI navigator seeking personhood; **Mako**, a legendary pilot; and a team of creators, Ari discovers that the Directorate's upgrade promises permanent identity, unlimited customization, and digital immortality—but secretly converts player profiles, avatar bodies, memories, and creations into corporate property.

Ari's team must collect four keys across OSIS:

1. The Flight Key
2. The Race Key
3. The Creator Key
4. The Identity Key

The final race crosses Central Space, a collapsing star tunnel, the Grand Racetrack, and the OSIS core. Ari can become the new ruler of the metaverse—or release control to the players. Ari chooses a world governed by consent, creativity, accountability, and shared ownership.

## Core Themes

- Identity versus ownership
- Freedom and privacy in digital spaces
- Creativity and creator rights
- Community governance
- Consent and personal boundaries
- Fair competition and responsible entertainment
- Accessibility and inclusion
- The danger of turning play into exploitation

**OSIS is not valuable because one company controls it. It is valuable because millions of players make it alive.**

> This README is a product and story concept, not legal, medical, safety, accessibility, or regulatory advice. Any real-money wagering, adult service, body/biometric data processing, psychological evaluation, advertising, or regional launch requires qualified review and documented approval.
