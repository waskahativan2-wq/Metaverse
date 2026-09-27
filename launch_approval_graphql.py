from __future__ import annotations

from collections.abc import Mapping, Sequence
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from graphql import (
    ExecutionResult,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLField,
    GraphQLID,
    GraphQLList,
    GraphQLNonNull,
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLString,
    graphql_sync,
)


RECORD_PATH = Path(__file__).resolve().parent / "docs" / "final-launch-approval-record.json"


@lru_cache(maxsize=1)
def load_canonical_records() -> dict[str, dict[str, Any]]:
    with RECORD_PATH.open(encoding="utf-8") as record_file:
        payload = json.load(record_file)
    return _index_canonical_records(payload)


def _index_canonical_records(payload: Any) -> dict[str, dict[str, Any]]:
    records: list[Mapping[str, Any]]

    if isinstance(payload, Mapping) and "record_id" in payload:
        records = [payload]
    elif isinstance(payload, Mapping):
        for key in ("records", "items", "launchApprovals", "launch_approvals"):
            candidate = _as_sequence(payload.get(key))
            if candidate:
                records = [record for record in candidate if isinstance(record, Mapping)]
                break
        else:
            records = []
    elif isinstance(payload, (list, tuple)):
        records = [record for record in payload if isinstance(record, Mapping)]
    else:
        records = []

    return {
        record["record_id"]: dict(record)
        for record in records
        if record.get("record_id")
    }


def _normalize_open_exception(exception: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "owner": exception.get("owner"),
        "issue": exception.get("issue"),
        "mitigation": exception.get("mitigation"),
        "dueDate": exception.get("due_date"),
        "expiryDate": exception.get("expiry_date"),
        "acceptanceAuthority": exception.get("acceptance_authority"),
        "status": exception.get("status"),
    }


def _as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _as_sequence(value: Any) -> Sequence[Any]:
    return (
        value
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray))
        else ()
    )


def _normalize_final_decision_block(block: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "finalDecision": block.get("final_decision"),
        "decisionTimestampUtc": block.get("decision_timestamp_utc"),
        "accountableOwner": block.get("accountable_owner"),
        "releaseStatus": block.get("release_status"),
        "approvalRecordId": block.get("approval_record_id"),
        "rollbackTrigger": block.get("rollback_trigger"),
        "nextReviewDate": block.get("next_review_date"),
    }


def _normalize_go_no_go_rule(rule: Mapping[str, Any]) -> dict[str, Any]:
    requirements = _as_mapping(rule.get("requirements_met"))
    return {
        "requirementsMet": {
            "authorityVerified": requirements.get("authority_verified"),
            "legalReviewComplete": requirements.get("legal_review_complete"),
            "privacyReviewComplete": requirements.get("privacy_review_complete"),
            "securityVerified": requirements.get("security_verified"),
            "safetyVerified": requirements.get("safety_verified"),
            "aiMrVerified": requirements.get("ai_mr_verified"),
            "reliabilityVerified": requirements.get("reliability_verified"),
            "rollbackTested": requirements.get("rollback_tested"),
            "noUnresolvedCriticalException": requirements.get("no_unresolved_critical_exception"),
            "requiredApprovalsSigned": requirements.get("required_approvals_signed"),
            "hashVerified": requirements.get("hash_verified"),
            "signatureVerified": requirements.get("signature_verified"),
            "signerAuthorityVerified": requirements.get("signer_authority_verified"),
        },
        "finalResult": rule.get("final_result"),
    }


def get_launch_approval(record_id: str) -> dict[str, Any] | None:
    record = load_canonical_records().get(record_id)
    if record is None:
        return None

    evidence_links = record.get("evidence_links")
    open_exceptions = record.get("open_exceptions")

    return {
        "recordId": record.get("record_id"),
        "title": record.get("title"),
        "version": record.get("version"),
        "status": record.get("status"),
        "owner": record.get("owner"),
        "classification": record.get("classification"),
        "approvalStatus": record.get("approval_status"),
        "signatureStatus": record.get("signature_status"),
        "decision": record.get("decision"),
        "decisionRationale": record.get("decision_rationale"),
        "releaseIdentifier": record.get("release_identifier"),
        "sourceHash": record.get("source_hash"),
        "auditLogReference": record.get("audit_log_reference"),
        "storageLocation": record.get("storage_location"),
        "evidenceLinks": [
            evidence_link
            for evidence_link in _as_sequence(evidence_links)
            if isinstance(evidence_link, str)
        ],
        "openExceptions": [
            _normalize_open_exception(exception)
            for exception in _as_sequence(open_exceptions)
            if isinstance(exception, Mapping)
        ],
        "finalDecisionBlock": _normalize_final_decision_block(
            _as_mapping(record.get("final_decision_block"))
        ),
        "goNoGoRule": _normalize_go_no_go_rule(_as_mapping(record.get("go_no_go_rule"))),
    }


OpenExceptionType = GraphQLObjectType(
    name="OpenException",
    fields=lambda: {
        "owner": GraphQLField(GraphQLString),
        "issue": GraphQLField(GraphQLString),
        "mitigation": GraphQLField(GraphQLString),
        "dueDate": GraphQLField(GraphQLString),
        "expiryDate": GraphQLField(GraphQLString),
        "acceptanceAuthority": GraphQLField(GraphQLString),
        "status": GraphQLField(GraphQLString),
    },
)


FinalDecisionBlockType = GraphQLObjectType(
    name="FinalDecisionBlock",
    fields=lambda: {
        "finalDecision": GraphQLField(GraphQLString),
        "decisionTimestampUtc": GraphQLField(GraphQLString),
        "accountableOwner": GraphQLField(GraphQLString),
        "releaseStatus": GraphQLField(GraphQLString),
        "approvalRecordId": GraphQLField(GraphQLID),
        "rollbackTrigger": GraphQLField(GraphQLString),
        "nextReviewDate": GraphQLField(GraphQLString),
    },
)


GoNoGoRequirementsType = GraphQLObjectType(
    name="GoNoGoRequirements",
    fields=lambda: {
        "authorityVerified": GraphQLField(GraphQLBoolean),
        "legalReviewComplete": GraphQLField(GraphQLBoolean),
        "privacyReviewComplete": GraphQLField(GraphQLBoolean),
        "securityVerified": GraphQLField(GraphQLBoolean),
        "safetyVerified": GraphQLField(GraphQLBoolean),
        "aiMrVerified": GraphQLField(GraphQLBoolean),
        "reliabilityVerified": GraphQLField(GraphQLBoolean),
        "rollbackTested": GraphQLField(GraphQLBoolean),
        "noUnresolvedCriticalException": GraphQLField(GraphQLBoolean),
        "requiredApprovalsSigned": GraphQLField(GraphQLBoolean),
        "hashVerified": GraphQLField(GraphQLBoolean),
        "signatureVerified": GraphQLField(GraphQLBoolean),
        "signerAuthorityVerified": GraphQLField(GraphQLBoolean),
    },
)


GoNoGoRuleType = GraphQLObjectType(
    name="GoNoGoRule",
    fields=lambda: {
        "requirementsMet": GraphQLField(GoNoGoRequirementsType),
        "finalResult": GraphQLField(GraphQLString),
    },
)


LaunchApprovalType = GraphQLObjectType(
    name="LaunchApproval",
    fields=lambda: {
        "recordId": GraphQLField(GraphQLID),
        "title": GraphQLField(GraphQLString),
        "version": GraphQLField(GraphQLString),
        "status": GraphQLField(GraphQLString),
        "owner": GraphQLField(GraphQLString),
        "classification": GraphQLField(GraphQLString),
        "approvalStatus": GraphQLField(GraphQLString),
        "signatureStatus": GraphQLField(GraphQLString),
        "decision": GraphQLField(GraphQLString),
        "decisionRationale": GraphQLField(GraphQLString),
        "releaseIdentifier": GraphQLField(GraphQLString),
        "sourceHash": GraphQLField(GraphQLString),
        "auditLogReference": GraphQLField(GraphQLString),
        "storageLocation": GraphQLField(GraphQLString),
        "evidenceLinks": GraphQLField(GraphQLList(GraphQLString)),
        "openExceptions": GraphQLField(GraphQLList(OpenExceptionType)),
        "finalDecisionBlock": GraphQLField(FinalDecisionBlockType),
        "goNoGoRule": GraphQLField(GoNoGoRuleType),
    },
)


QueryType = GraphQLObjectType(
    name="Query",
    fields=lambda: {
        "launchApproval": GraphQLField(
            LaunchApprovalType,
            args={"recordId": GraphQLArgument(GraphQLNonNull(GraphQLID))},
            resolve=lambda _root, _info, recordId: get_launch_approval(recordId),
        )
    },
)


schema = GraphQLSchema(query=QueryType)


def execute_query(
    query: str, variable_values: Mapping[str, Any] | None = None
) -> ExecutionResult:
    return graphql_sync(schema, query, variable_values=variable_values)
