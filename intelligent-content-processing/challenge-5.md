# Challenge 05: Persist Structured Data & Expose APIs (Cosmos DB + App Service)

## Introduction

In enterprise systems, AI-extracted data must be **stored securely**, **queried easily**, and **accessible through APIs**.
In this challenge, participants will persist validated document data into **Azure Cosmos DB** and expose it through **REST APIs hosted on Azure App Service**, completing the end-to-end automation pipeline.

## Challenge Objectives

* Create an **Azure Cosmos DB (NoSQL)** database and container.
* Store final, validated document JSON in Cosmos DB.
* Configure **Azure App Service** to orchestrate the workflow.
* Secure secrets using **Azure Key Vault**.
* Expose REST APIs to submit and retrieve processed documents.
* Perform a full end-to-end test of the solution.

## Steps to Complete

### Create Azure Cosmos DB (NoSQL)

1. In the **Azure Portal**, search for **Azure Cosmos DB** and click **Create**.

2. Select **Azure Cosmos DB for NoSQL**.

3. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** Select `challenge-rg-<inject key="DeploymentID" enableCopy="false"/>`
   * **Account Name:** `cosmos-docs-<inject key="DeploymentID" enableCopy="false"/>`
   * **Location:** Same region as other resources
   * **Capacity mode:** Provisioned throughput

4. Click **Review + Create** → **Create**.

5. After deployment succeeds, open the **Cosmos DB account**.

### Create Database and Container

6. In Cosmos DB, go to **Data Explorer**.

7. Click **New Database** and provide:

   * **Database ID:** `documents-db`

8. Click **New Container** and provide:

   * **Container ID:** `processed-documents`
   * **Partition key:** `/documentType`

9. Click **OK**.

### Insert Processed Document Data

10. In the container, click **New Item**.

11. Paste a **final approved JSON document** from Challenge 04:

    ```json
    {
    "id": "doc-002",
    "documentType": "HandwrittenNote",
    "referenceId": "John Doe",
    "amount": 0,
    "currency": "",
    "confidence": 0.90,
    "status": "APPROVED"
    }
    ```

12. Click **Save**.

13. Repeat for the invoice document if time permits.

### Configure Azure App Service

14. In the **Azure Portal**, open your existing **App Service**.

15. Enable **System Assigned Managed Identity**:

* Go to **Identity**
* Turn **Status** to **On**
* Click **Save**

### Configure Azure Key Vault Access

16. Open **Azure Key Vault**.

17. Go to **Access policies** (or **IAM**, depending on vault type).

18. Grant the App Service managed identity access to:

* **Get**
* **List**
  secrets.

### Store Secrets in Key Vault

19. In Key Vault, add secrets:

* `COSMOS_CONNECTION_STRING`
* `STORAGE_CONNECTION_STRING`
* `OPENAI_ENDPOINT`
* `OPENAI_API_KEY`
* `DOC_INTELLIGENCE_ENDPOINT`
* `DOC_INTELLIGENCE_KEY`

### Expose APIs via App Service (Conceptual)

20. In your App Service, create REST endpoints:

* `POST /process-document`
* `GET /document/{id}`

    > For the hackathon, implementation can be:
    >
    > * Minimal code
    > * Or mocked responses
    > * Or simple sample controller returning Cosmos DB data

### Test End-to-End Flow

21. Upload a document to Blob Storage.

22. Run through:

* OCR (Challenge 01)
* GPT extraction (Challenge 02)
* Schema mapping (Challenge 03)
* HITL approval (Challenge 04)

23. Verify:

* Final document exists in Cosmos DB
* Status is `APPROVED`
* Data can be retrieved via API or Data Explorer

### Success Criteria

You have successfully completed the Challenge 5:

* Cosmos DB stores structured document JSON
* App Service is configured and secured
* Secrets are managed via Key Vault
* End-to-end flow completes successfully

### Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

Congratulations! You've completed all challenges.