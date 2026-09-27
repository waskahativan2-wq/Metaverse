import unittest

from graphql import graphql_sync

from launch_approval_graphql import _index_canonical_records, execute_query, schema


KNOWN_RECORD_ID = "FLFN-LAUNCH-APPROVAL-2026-0001"


class LaunchApprovalGraphQLTests(unittest.TestCase):
    def test_schema_builds_and_executes_query(self) -> None:
        result = execute_query(
            """
            query LaunchApproval($recordId: ID!) {
              launchApproval(recordId: $recordId) {
                recordId
                title
                decision
              }
            }
            """,
            {"recordId": KNOWN_RECORD_ID},
        )

        self.assertIsNone(result.errors)
        self.assertEqual(result.data["launchApproval"]["recordId"], KNOWN_RECORD_ID)
        self.assertEqual(result.data["launchApproval"]["decision"], "No-go")

    def test_unknown_record_returns_null(self) -> None:
        result = graphql_sync(
            schema,
            """
            query {
              launchApproval(recordId: "UNKNOWN") {
                recordId
              }
            }
            """,
        )

        self.assertIsNone(result.errors)
        self.assertIsNone(result.data["launchApproval"])

    def test_record_index_supports_collection_payloads(self) -> None:
        indexed_records = _index_canonical_records(
            {
                "records": [
                    {"record_id": "A-1", "title": "First"},
                    {"record_id": "B-2", "title": "Second"},
                ]
            }
        )

        self.assertEqual(sorted(indexed_records), ["A-1", "B-2"])
        self.assertEqual(indexed_records["B-2"]["title"], "Second")

    def test_nested_open_exceptions_are_exposed(self) -> None:
        result = execute_query(
            """
            query LaunchApproval($recordId: ID!) {
              launchApproval(recordId: $recordId) {
                openExceptions {
                  owner
                  issue
                  mitigation
                  dueDate
                  expiryDate
                  acceptanceAuthority
                  status
                }
              }
            }
            """,
            {"recordId": KNOWN_RECORD_ID},
        )

        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data["launchApproval"]["openExceptions"]), 4)
        self.assertEqual(
            result.data["launchApproval"]["openExceptions"][0]["issue"],
            "Authority verification pending",
        )
        self.assertEqual(
            result.data["launchApproval"]["openExceptions"][3]["acceptanceAuthority"],
            "pending",
        )

    def test_no_go_and_blocked_gate_state_is_preserved(self) -> None:
        result = execute_query(
            """
            query LaunchApproval($recordId: ID!) {
              launchApproval(recordId: $recordId) {
                decision
                finalDecisionBlock {
                  finalDecision
                  releaseStatus
                  approvalRecordId
                }
                goNoGoRule {
                  finalResult
                  requirementsMet {
                    authorityVerified
                    requiredApprovalsSigned
                    hashVerified
                    signatureVerified
                  }
                }
              }
            }
            """,
            {"recordId": KNOWN_RECORD_ID},
        )

        self.assertIsNone(result.errors)
        self.assertEqual(result.data["launchApproval"]["decision"], "No-go")
        self.assertEqual(
            result.data["launchApproval"]["finalDecisionBlock"]["finalDecision"], "NO-GO"
        )
        self.assertEqual(
            result.data["launchApproval"]["finalDecisionBlock"]["releaseStatus"],
            "blocked",
        )
        self.assertEqual(
            result.data["launchApproval"]["finalDecisionBlock"]["approvalRecordId"],
            KNOWN_RECORD_ID,
        )
        self.assertEqual(result.data["launchApproval"]["goNoGoRule"]["finalResult"], "NO-GO")
        self.assertFalse(
            result.data["launchApproval"]["goNoGoRule"]["requirementsMet"][
                "authorityVerified"
            ]
        )
        self.assertFalse(
            result.data["launchApproval"]["goNoGoRule"]["requirementsMet"][
                "requiredApprovalsSigned"
            ]
        )
        self.assertFalse(
            result.data["launchApproval"]["goNoGoRule"]["requirementsMet"]["hashVerified"]
        )
        self.assertFalse(
            result.data["launchApproval"]["goNoGoRule"]["requirementsMet"][
                "signatureVerified"
            ]
        )


if __name__ == "__main__":
    unittest.main()
