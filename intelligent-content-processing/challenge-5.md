# Challenge 05: Persist Structured Data & Expose APIs (Cosmos DB + App Service)

## Introduction

In enterprise systems, AI-extracted data must be **stored securely**, **queried easily**, and **accessible through APIs**.
In this challenge, participants will persist validated document data into **Azure Cosmos DB** and expose it through **REST APIs hosted on Azure App Service**, completing the end-to-end automation pipeline.

## Challenge Objectives

* Create an **Azure Cosmos DB (NoSQL)** database and container.
* Store final, validated document JSON in Cosmos DB.
* Configure **Azure App Service** to orchestrate the workflow.
* Secure secrets using **Environment variables**.
* Expose REST APIs to submit and retrieve processed documents.
* Perform a full end-to-end test of the solution.

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

### Create Azure App Service

14. In the Azure Portal, search for **App Services** and click **Create** > **+ Web App**.

15. Under Basics, provide:

   * **Subscription**: Use the available subscription

   * **Resource Group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**

   * **Name**: **app-doc-processing-<inject key="DeploymentID" enableCopy="false"/>**

   * **Publish**: Code

   * **Runtime stack**: Any (Python / Node.js / .NET)

   * **Operating System**: Windows

   * **Region**: Same region as other resources

   * **Pricing Plan**: Free F1

   * Click **Review + Create** → **Create**.

After deployment succeeds, open the **App Service**.

### Enable Managed Identity for App Service

16. In the App Service, go to **Settings > Identity**.

17. Under **System assigned**, set **Status** to **On**.

18. Click **Save** and select **Yes**.

### Add Environment Variables in App Service

19. Go to **Settings** → Open your **Environment Variables**.

20. Under **App settings**, add each one individually:

      | Name                        | Value                         |
      | --------------------------- | ----------------------------- |
      | `OPENAI_API_KEY`            | `<your OpenAI key>`           |
      | `OPENAI_ENDPOINT`           | `<your OpenAI endpoint>`      |
      | `DOC_INTELLIGENCE_KEY`      | `<doc intelligence key>`      |
      | `DOC_INTELLIGENCE_ENDPOINT` | `<doc intelligence endpoint>` |
      | `COSMOS_CONNECTION_STRING`  | `<cosmos connection string>`  |
      | `STORAGE_CONNECTION_STRING` | `<storage connection string>` |

      >**Note:** Fetch all the details from the respective resources.

21. Leave **Deployment slot setting** unchecked.

22. Click **OK** for each. Click **Save**. Restart the App Service when prompted.

### Test End-to-End Flow

23. Upload a document to Blob Storage.

24. Run through:

   * OCR (Challenge 01)
   * GPT extraction (Challenge 02)
   * Schema mapping (Challenge 03)
   * HITL approval (Challenge 04)

25. Verify:

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
* App Service is configured and secured
* Secrets are managed via Environment variables
* End-to-end flow completes successfully

Congratulations! You've completed all challenges.