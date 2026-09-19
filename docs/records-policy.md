# OSIS Records Policy

## Purpose

This policy establishes the minimum record controls for live OSIS documents, approvals, signature evidence, email metadata, partner communications, and access-request records. The goal is to ensure each record is attributable, versioned, time-stamped, retrievable, tamper-evident, and reviewable without altering the underlying evidence.

## Scope

This policy applies to all human-authored, system-generated, and externally received records that may be relied upon for governance, operations, compliance, privacy requests, audits, or dispute resolution.

## Required record fields

Every record must preserve the following fields where applicable:

- record_id
- title
- document_type
- version
- status
- created_by
- created_at
- updated_by
- updated_at
- owner
- classification
- privacy_sensitivity
- retention_category
- related_document_ids
- related_email_ids
- approval_status
- signature_status
- signer_name
- signer_role
- identity_verification_method
- signed_at
- source_hash
- previous_hash
- audit_log_reference
- storage_location
- access_controls
- legal_hold

## Evidence standards

1. No record may be overwritten in place if it has been approved, signed, archived, or placed under legal hold.
2. Each record must have a hash or checksum generated at creation and whenever it is materially changed.
3. The hash must be retained alongside the record and the related audit log.
4. The current version must be linked to the previous version and the approval evidence.
5. All time stamps must use ISO-8601 UTC.
6. Evidence must be retrievable without altering the original artifact.

## Lifecycle

### Draft

- Created by an authorized author or system process.
- Retains metadata, reviewer notes, and version history.
- The document is not final until an approval step occurs.

### Review

- Reviewers log comments, decisions, and concerns.
- Rejections must be traceable to a specific version.
- The review record must preserve approvals or objections with timestamps.

### Approved

- The record receives an approval record, approver identity, and date/time.
- If the document is sensitive, access restrictions apply.

### Signed

- Signatures must be linked to the signer’s identity, role, method, and timestamp.
- Original signed copies must be preserved as immutable evidence.
- Signature and attachment hashes must be retained.

### Archived

- Finalized records must be stored in an immutable or write-once system where practical.
- Retention rules must be applied consistently.
- Archived records remain readable and reviewable without modification.

## Email and metadata preservation

When email, attachments, or message metadata are used as evidence or operational records, they must preserve:

- senders and recipients
- Message-ID and thread references
- subject and timestamp
- mailbox source and routing data
- attachment names and hashes
- delivery path metadata
- links to related operational records or matters

## ATIP and access requests

For access-to-information requests, privacy requests, investigations, or complaints:

- preserve all responsive records in a structured, searchable location
- mark records with legal_hold when required
- preserve metadata, redaction history, access logs, and disclosure decisions
- maintain an export and review trail without changing the original evidence

## Security and administrative controls

- Use least-privilege access.
- Separate system administration from approval authority.
- Protect private signing keys and administrative credentials.
- Use MFA, encryption in transit and at rest, and synchronized time sources.
- Maintain logs for user access, modifications, and disclosures.

## Compliance note

This record model is designed to support operational evidence, privacy obligations, governance review, and lawful disclosure. It does not replace legal advice or jurisdiction-specific retention requirements.

## Policy owner

The OSIS governance lead, compliance steward, or applicable data owner may define the implementation details for retention, approvals, and regional requirements under this policy.
