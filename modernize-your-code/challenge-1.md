# Challenge 01: Set Up Azure Infrastructure

## Introduction

Before building the AI-powered SQL modernization pipeline, you need to provision the necessary Azure infrastructure. This challenge involves creating a Microsoft Foundry project with GPT-4.1 model deployment and Cosmos DB for storing translation results and history.

## Challenge Objectives

- Set up a Microsoft Foundry project with GPT-4.1 model deployment
- Provision Cosmos DB with an appropriate database and containers
- Verify all resources are properly configured and accessible

## Steps to Complete

### Task 1: Verify Pre-Deployed Resource Group

1. In the **Azure Portal**, search for **Resource groups** in the top search bar and select it.

1. You should see a pre-deployed resource group named **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**.

1. Click on **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>** to open it.

1. This resource group will be used for all resources you create in this hackathon.

### Task 2: Create Microsoft Foundry Project with Model Deployment

1. In the **Azure Portal**, search for **Microsoft Foundry** and select it.

1. In the **Use with Foundry** tab, click on **Foundry**.

1. Click **+ Create** to create a new Foundry project.

1. Configure the AI Foundry project:

   - **Subscription**: Select the available **Azure subscription**.
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Project name**: **sql-modernize-<inject key="DeploymentID" enableCopy="false"/>**
   - **Region**: **<inject key="Region"></inject>**.
   - **Default project name**: Keep it as default
   - Click **Review + Create**.

1. Click **Create**.

1. Please wait for the deployment to complete as it can take 2-3 minutes.

1. Once created, click **Go to Foundry portal** in the overview section.

<validation step="616b2c9f-85e8-44de-932a-418e889351a1" />

 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 3: Deploy GPT-4.1 Model in Microsoft Foundry

1. In **Microsoft Foundry** portal.

1. Click on **Models + Endpoints** from the left navigation menu.

1. Click on **+ Deploy model** and select **Deploy base model**.

1. Search for and select **gpt-4.1** from the model catalog and click on **Confirm** button.

1. Configure the deployment:

      - **Deployment name**: `sql-translator`
      - **Deployment type**: **Global Standard**
      - Click **Customize**.
      - **Tokens per Minute Rate Limit**: **50K**

         > **Important**: Do not increase the TPM limit beyond 50K to avoid exceeding quota limits and additional costs.

1. Click **Create**.

### Task 4: Test the Model Deployment

1. In your `sql-translator` model deployment.

1. Select **Open in playground**.

1. In the **Chat History** page, enter and test with the simple prompt:
   ```
   Translate this Oracle SQL to Azure SQL: SELECT * FROM dual WHERE ROWNUM <= 5;
   ```

1. Verify you receive a response with Azure SQL translation.

<validation step="0561d3a2-e34a-4731-925b-4e0b02decc29" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 5: Create Azure Cosmos DB

1. In the **Azure Portal**, search for **Azure Cosmos DB** and select it.

1. Click on **+ Create** button.

1. Click on **Create** for **Azure Cosmos DB for NoSQL**.

1. Configure Cosmos DB:

      - **Workload Type**: Select **Development/Testing**
      - **Subscription**: Select the available **Azure subscription**
      - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Account Name**: **sql-modernization-cosmos-<inject key="DeploymentID" enableCopy="false"/>**
      - **Availability Zones**: Select **Disable**
      - **Location**: Keep it **Default**
      - **Capacity mode**: Select **Provisioned throughput**
      - **Apply Free Tier Discount**: Select **Apply**
      - **Limit total account throughput**: Keep it selected

         >**Note:** If you are unable to create **Azure Cosmos DB** with the workload type set to **Development/Testing**, select **Production** and try again.

1. Click **Review + Create**, then **Create**.

1. Wait for the deployment to complete as it can take 10-15 minutes.

<validation step="c9460cd7-b2b8-4294-8143-516ccadd3f20" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 6: Create Cosmos DB Database and Containers

1. In your Cosmos DB account, click on **Data Explorer** from the left navigation.

      >**Note:** Close all pop-up windows.

2. Click **+ New Container** drop-down. From the drop-down, select **+ New Database**.

3. Configure the database:

      - **Database id**: `SQLModernizationDB`
      - Click **OK**

4. Click **OK**.

5. Create the first container for translation results:

    - Right-Click on the **SQLModernizationDB** and click **New Container**
    - **Database id**: Select **Use existing** and choose **SQLModernizationDB**.
    - **Container id**: `TranslationResults`
    - **Partition key**: `/sourceDialect`
    - Click **OK**

6. Create a second container for validation logs:

    - Right-Click on the **SQLModernizationDB** and click **New Container** again
    - **Database id**: Select **Use existing** and choose **SQLModernizationDB**.
    - **Container id**: `ValidationLogs`
    - **Partition key**: `/translationId`
    - Click **OK**

7. Create a third container for optimization suggestions:

      - Right-Click on the **SQLModernizationDB** and click **New Container** again
      - **Database id**: Select **Use existing** and choose **SQLModernizationDB**.
      - **Container id**: `OptimizationResults`
      - **Partition key**: `/translationId`
      - Click **OK**

8. Verify all three containers are visible in Data Explorer.

9. Navigate to **Keys** in the left menu under **Settings** and copy:

      - **URI**
      - **PRIMARY KEY**

      - Save these values for later use.

<validation step="47428908-2f8d-456b-84a5-df4c148f8c67" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 7: Verify All Resources

1. Navigate back to your resource group: **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**

1. Verify you see the following resources:

      - Microsoft Foundry hub and project resources
      - Cosmos DB account

1. Ensure all resources show **Deployment succeeded** status.

### Task 8: Gather Configuration Values

Create a text file or note with the following information (you'll need these in subsequent challenges):

```text
Microsoft Foundry (with GPT-4.1 deployment):
- Foundry Endpoint: [your-foundry-services-endpoint with /api/projects/...]
- Deployment Name: sql-translator

Cosmos DB:
- URI: https://sql-modernization-cosmos-xxxxx.documents.azure.com:443/
- Primary Key: [your-key]
- Database Name: SQLModernizationDB
- Containers: TranslationResults, ValidationLogs, OptimizationResults
```

## Success Criteria

- Microsoft Foundry project created with GPT-4.1 model deployed successfully
- Model tested in Chat Playground and working correctly
- Cosmos DB account created with database and three containers (TranslationResults, ValidationLogs, OptimizationResults)
- All connection strings, keys, and endpoints documented for future use
- All resources deployed in the same resource group and region

## Additional Resources

- [Azure OpenAI in AI Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft Foundry Overview](https://learn.microsoft.com/azure/ai-studio/)
- [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/azure/cosmos-db/nosql/)

Now, click **Next** to continue to **Challenge 02**.