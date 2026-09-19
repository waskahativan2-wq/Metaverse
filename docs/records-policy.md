# OSIS Records Policy

## Purpose

This policy establishes the minimum record controls for live OSIS documents, approvals, signature evidence, email metadata, partner communications, access requests, and launch decisions. It ensures that records are attributable, versioned, time-stamped, tamper-evident, retrievable, and linked to approval evidence.

> This policy supports operational governance and lawful disclosure. It does not replace legal advice or jurisdiction-specific retention, privacy, records, employment, tenancy, accessibility, or Indigenous data-governance requirements.

## Scope

This policy applies to human-authored, system-generated, and externally received records relied upon for governance, operations, compliance, privacy requests, audits, launch decisions, incident response, or dispute resolution.

## Required record fields

Every record must preserve the following fields where applicable:

- `record_id`
- `title`
- `document_type`
- `version`
- `status`
- `created_by`
- `created_at`
- `updated_by`
- `updated_at`
- `owner`
- `classification`
- `privacy_sensitivity`
- `retention_category`
- `related_document_ids`
- `related_email_ids`
- `approval_status`
- `signature_status`
- `signer_name`
- `signer_role`
- `identity_verification_method`
- `signed_at`
- `source_hash`
- `previous_hash`
- `audit_log_reference`
- `storage_location`
- `access_controls`
- `legal_hold`

For approval records, also preserve the decision, decision rationale, release or artifact identifier, evidence links, open exceptions, rollback trigger, and next review date.

## Evidence and integrity standards

1. Do not overwrite a record that is approved, signed, archived, or under legal hold.
2. Generate a SHA-256 hash or equivalent checksum when a record is created and whenever it materially changes.
3. Retain each hash with the record and related audit log.
4. Link each version to its previous record and approval evidence. For an initial version, record `previous_hash: null` and document that it is the initial version.
5. A signed change creates a new version and requires re-review and re-signature.
6. Store finalized evidence in immutable, write-once, or tamper-evident storage where practical.
7. All timestamps must use ISO-8601 UTC.
8. Evidence must be retrievable without altering the original artifact.
9. The final evidence package must identify the exact release commit, artifact, configuration, and migration identifiers it validates.

## Lifecycle and approval workflow

### Draft

- Created by an authorized author or system process.
- Retains metadata, reviewer notes, and version history.
- Is not final until an approval step occurs.

### Review

- Reviewers record comments, decisions, objections, and conditions.
- Rejections are traceable to a specific version.
- The review record preserves approvals or objections with timestamps.

### Approved

- The record has an approval record, approver identity, decision, rationale, and date/time.
- Sensitive records have appropriate access restrictions.
- Any exception has an owner, mitigation, due date, expiry date, and acceptance authority.

### Signed

- Each signature is linked to the signer’s identity, role, verification method, exact version, hash, consent, and UTC signing time.
- Original signed copies are preserved as immutable evidence.
- Signature and attachment hashes are retained.
- MFA or equivalent strong verification is used for material approvals where available.

### Archived

- Finalized records are stored in an immutable or write-once system where practical.
- Retention rules are applied consistently.
- Archived records remain readable and reviewable without modification.

## Approval roles

Required roles depend on scope, but a production or public launch normally requires review by the accountable owner, product lead, security lead, privacy lead, safety/moderation lead, legal/compliance reviewer, and operations/reliability lead.

No single person should both administer the evidence system and provide the sole approval authority for a material decision.

## Email and metadata preservation

When email, attachments, or message metadata are evidence or operational records, preserve:

- senders and recipients
- Message-ID and thread references
- subject and timestamp
- mailbox source and routing data
- attachment names and hashes
- delivery-path metadata
- links to related operational records or matters

Do not rely on an email alone as proof of authority when a formal approval record or signature workflow is required.

## ATIP and access requests

For access-to-information requests, privacy requests, investigations, audits, complaints, or legal matters:

- preserve responsive records in a structured, searchable location
- apply `legal_hold` when required
- preserve metadata, redaction history, access logs, and disclosure decisions
- maintain an export and review trail without changing original evidence
- restrict access to authorized reviewers and record disclosures

## Security and administrative controls

- Use least-privilege access.
- Separate system administration from approval authority.
- Protect private signing keys and administrative credentials.
- Use MFA, encryption in transit and at rest, and synchronized time sources.
- Maintain logs for access, modifications, approvals, disclosures, exports, and deletions.
- Test backup restoration and evidence retrieval periodically.
- Never store production secrets or signing keys in source code, ordinary email, or application logs.

## Adaptable policy fields

The policy owner must define, for each jurisdiction and record class, retention periods, authorized signers, approval hierarchy, data residency, consent requirements, redaction rules, emergency access, release authority, and applicable Indigenous data-governance requirements.

OCAP® principles and community data rules must be defined with the applicable First Nation, organization, or data steward. A self-issued certificate or email alone does not establish authority, consent, or ownership.

## Policy statement

Every approved OSIS document must be attributable, versioned, time-stamped, tamper-evident, retrievable, and linked to its approval and signature evidence. Email and metadata must be preserved when they are part of the record. A release must not be marked Go unless its required evidence and approvals are complete.

## Policy owner

The OSIS governance lead, compliance steward, or applicable data owner defines implementation details for retention, approvals, regional requirements, and periodic review.
