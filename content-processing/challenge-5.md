# Challenge 05: Review Queue & End-to-End Validation

## Introduction

Your document processing pipeline is live - documents flow through OCR, classification, extraction, and validation automatically. But the power of your system is not just automation; it's **intelligent human-in-the-loop processing**. Documents that the AI is confident about get auto-approved, while uncertain ones land in a review queue for human decision-making.

In this final challenge, you will use the dashboard's **Review Queue** to examine, approve, or reject flagged documents. You will then process all remaining sample documents, validate the end-to-end pipeline, and explore the analytics dashboard.

## Challenge Objectives

- Use the Review Queue tab to review, approve, and reject flagged documents
- Process all 5 sample documents through the complete pipeline
- Validate correct routing: high-confidence to ProcessedDocuments, low-confidence to ReviewQueue
- Explore the Analytics dashboard for processing metrics

## Steps to Complete

### Task 1: Process All Sample Documents

1. In the Streamlit app, go to the **Process Documents** tab.

1. Process each of the 5 sample documents using the **Use sample data** dropdown. If you already processed some in Challenge 04, process the remaining ones:

   - **invoice_contoso** - Expected Classification: INVOICE, Expected Routing: AUTO_APPROVE (confidence >= 0.85)
   - **receipt_cafe** - Expected Classification: RECEIPT, Expected Routing: AUTO_APPROVE (confidence >= 0.85)
   - **medical_form** - Expected Classification: MEDICAL_FORM, Routing varies - may go to review if OCR quality is low
   - **insurance_claim** - Expected Classification: INSURANCE_CLAIM, Routing varies - depends on extraction completeness
   - **identity_doc** - Expected Classification: IDENTITY_DOCUMENT, Expected Routing: AUTO_APPROVE (confidence >= 0.85)

1. After processing all documents, note how many were auto-approved vs. sent to review.

### Task 2: Review Flagged Documents

1. Click on the **Review Queue** tab.

1. You should see a list of documents flagged for human review (those with confidence < 0.85 or the `poor_scan.txt` from Challenge 04).

1. For each document in the queue:

   - **View the extracted data** - click on a document to expand its details
   - **Review the validation report** - see the confidence score, missing fields, and review reasons
   - **View the original OCR text** - compare what was extracted vs. the raw text

1. For each document, you have three options:

   - **Approve** - Moves the document from `ReviewQueue` to `ProcessedDocuments` container, marks status as `HUMAN_APPROVED`
   - **Reject** - Marks the document as `REJECTED` in `ReviewQueue`, with an optional rejection reason
   - **Edit & Approve** - Opens an editor to correct extracted fields, then approves the corrected version

1. **Approve** at least one document - this demonstrates the human-in-the-loop workflow. The document should:

   - Disappear from the Review Queue
   - Appear in the `ProcessedDocuments` Cosmos DB container with `review_status: "HUMAN_APPROVED"`

1. **Reject** at least one document (you can reject the `poor_scan.txt` if it's in the queue). Provide a rejection reason like "Document is illegible, rescan required."

<validation step="b168305b-cf36-4d19-92dc-0496001a08b0" />

 
> **Congratulations** on completing the Task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Task. If you receive a success message, you can proceed to the next Task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 3: Explore the Analytics Dashboard

1. Click on the **Analytics** tab.

1. The dashboard shows key metrics about your document processing pipeline:

   - **Total Documents Processed** - Count of all documents that went through the pipeline
   - **Auto-Approved** - Documents routed directly to ProcessedDocuments (high confidence)
   - **Sent to Review** - Documents routed to ReviewQueue (low confidence)
   - **Human Approved** - Documents manually approved by reviewers
   - **Rejected** - Documents rejected during human review
   - **Average Confidence Score** - Mean confidence across all processed documents

1. The dashboard also shows:

   - **Document Type Distribution** - pie/bar chart of document types processed
   - **Confidence Score Distribution** - histogram of confidence scores
   - **Processing Timeline** - when documents were processed

1. Review the metrics and confirm they match your processing history.

### Task 4: Validate End-to-End in Cosmos DB

1. Go to the Azure portal > Cosmos DB > **Data Explorer**.

1. **ProcessedDocuments container** - Verify:

   - Contains auto-approved documents with `routing_decision: "AUTO_APPROVE"`
   - Contains human-approved documents with `review_status: "HUMAN_APPROVED"`
   - Each document has complete `classification`, `extraction`, and `validation` data

1. **ReviewQueue container** - Verify:

   - Contains rejected documents with `review_status: "REJECTED"` and a `rejection_reason`
   - May still contain pending documents (not yet reviewed)

1. Run this query in Data Explorer for the `ProcessedDocuments` container to see a summary:

   ```sql
   SELECT c.docType, c.classification.confidence, c.validation.confidence_score, 
          c.routing_decision, c.review_status, c.timestamp
   FROM c
   ORDER BY c.timestamp DESC
   ```

<validation step="3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f" />

 
> **Congratulations** on completing the Task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Task. If you receive a success message, you can proceed to the next Task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- All 5 sample documents have been processed through the pipeline
- At least 2 documents were auto-approved (routed to `ProcessedDocuments`)
- At least 1 document was sent to the Review Queue
- At least 1 document was manually approved from the Review Queue (status: `HUMAN_APPROVED`)
- At least 1 document was rejected from the Review Queue (with a rejection reason)
- Analytics dashboard shows accurate metrics matching your processing history
- Cosmos DB contains complete records in both `ProcessedDocuments` and `ReviewQueue` containers

## Additional Resources

- [Azure Cosmos DB Data Explorer](https://learn.microsoft.com/en-us/azure/cosmos-db/data-explorer)
- [Streamlit Charts and Dashboards](https://docs.streamlit.io/library/api-reference/charts)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)

## Summary

You have built a complete enterprise document processing pipeline that demonstrates:

- **Document Ingestion** - Azure Blob Storage for secure document storage
- **OCR Extraction** - Azure AI Document Intelligence for text, tables, and key-value pairs
- **AI Classification** - Multi-agent pipeline with Document Classification Agent
- **Structured Extraction** - Data Extraction Agent with type-specific schemas
- **Quality Validation** - Quality Validation Agent with confidence scoring
- **Smart Routing** - Automated approval vs. human review based on confidence
- **Human-in-the-Loop** - Review Queue with approve/reject/edit workflow
- **Analytics** - Real-time dashboard with processing metrics
- **Persistence** - Dual Cosmos DB containers for processed and review data

This architecture scales to thousands of documents daily and can be extended with Azure Functions for event-driven triggers, Logic Apps for notifications, and Power BI for advanced analytics.
