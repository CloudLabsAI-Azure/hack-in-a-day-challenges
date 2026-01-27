# Challenge 05: Persist Structured Data & Validate End-to-End Automation

## Introduction

In enterprise document automation systems, AI-extracted data must be **stored securely**, **queried reliably**, and **auditable for downstream processes**. In this challenge, participants will persist the final, validated document data into **Azure Cosmos DB**, completing the end-to-end Intelligent Content Processing pipeline.

This challenge focuses on **data persistence**, **validation**, and **traceability**, ensuring that AI-generated outputs are production-ready—without introducing additional infrastructure complexity.

## Challenge Objectives

* Create an Azure Cosmos DB (NoSQL) database and container
* Store final, validated document JSON in Cosmos DB
* Understand how AI-extracted data is persisted for enterprise use
* Verify document status, confidence, and approval outcomes
* Complete a full end-to-end test of the content processing pipeline

## Steps to Complete

### Create Azure Cosmos DB (NoSQL)

1. In the **Azure Portal**, search for **Azure Cosmos DB** and click **Create** > **Create**.

2. Select **Azure Cosmos DB for NoSQL**.

3. Under **Basics**, provide:

   * **Workload Type:** Development/Testing
   * **Subscription:** Use the available subscription
   * **Resource Group:** Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   * **Account Name:** **cosmos-docs-<inject key="DeploymentID" enableCopy="false"/>**
   * **Location:** Same region as other resources
   * **Capacity mode:** Provisioned throughput

4. Click **Review + Create** → **Create**.

5. After deployment succeeds, open the **Cosmos DB account**.

### Create Database and Container

6. In Cosmos DB, go to **Data Explorer**.

7. Click **+ New Container** drop-down and then select **+ New Databases**, provide:

   * **Database ID:** `documents-db`
   * Click **OK**

8. Click **New Container** and provide:

   * **Database ID:** `Use existing`
   * **Container ID:** `processed-documents`
   * **Partition key:** `/documentType`

9. Click **OK**.

### Insert Processed Document Data

10. In the container, click **New Item**.

11. Paste a **final approved JSON document** from Challenge 04:

    ```json
    {
    "id": "doc-002",
    "documentType": "Patient Note",
    "referenceId": "John Doe",
    "amount": 0,
    "currency": "",
    "confidence": 0.90,
    "status": "APPROVED"
    }
    ```

12. Click **Save**.

13. Repeat for the invoice document if time permits.

### Test End-to-End Flow

14. Upload a document to Blob Storage.

15. Run through:

   * OCR (Challenge 01)
   * GPT extraction (Challenge 02)
   * Schema mapping (Challenge 03)
   * HITL approval (Challenge 04)

16. Verify:

* Final document exists in Cosmos DB
* Status is `APPROVED`
* Data can be retrieved via API or Data Explorer

<validation step="b168305b-cf36-4d19-92dc-0496001a08b0" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Success Criteria

You have successfully completed the Challenge 5:

* Cosmos DB stores structured document JSON
* End-to-end flow completes successfully

Congratulations! You've completed all challenges.