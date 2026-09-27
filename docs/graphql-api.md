# OSIS launch approval GraphQL API

This repository includes a read-only `graphql-core` schema for the canonical launch approval record in [`docs/final-launch-approval-record.json`](./final-launch-approval-record.json).

## Install

```bash
python3 -m pip install -r requirements.txt
```

## Example query

```graphql
query LaunchApproval($recordId: ID!) {
  launchApproval(recordId: $recordId) {
    recordId
    title
    decision
    evidenceLinks
    openExceptions {
      issue
      mitigation
      status
    }
    finalDecisionBlock {
      finalDecision
      releaseStatus
      approvalRecordId
    }
    goNoGoRule {
      finalResult
      requirementsMet {
        authorityVerified
        legalReviewComplete
        privacyReviewComplete
        securityVerified
        safetyVerified
        aiMrVerified
        reliabilityVerified
        rollbackTested
        noUnresolvedCriticalException
        requiredApprovalsSigned
        hashVerified
        signatureVerified
        signerAuthorityVerified
      }
    }
  }
}
```

## Python execution example

```python
from launch_approval_graphql import execute_query

result = execute_query(
    """
    query LaunchApproval($recordId: ID!) {
      launchApproval(recordId: $recordId) {
        recordId
        decision
        finalDecisionBlock {
          releaseStatus
        }
      }
    }
    """,
    {"recordId": "FLFN-LAUNCH-APPROVAL-2026-0001"},
)

print(result.data)
```
