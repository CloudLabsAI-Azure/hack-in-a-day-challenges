# Challenge 01: Set Up Azure Infrastructure

## Introduction

Before building the AI-powered SQL modernization pipeline, you need to provision the necessary Azure infrastructure. This challenge involves creating Microsoft Foundry project with GPT-4.1 model deployment and Cosmos DB for storing translation results and history.

## Challenge Objectives

- Set up an Microsoft Foundry project with GPT-4.1 model deployment
- Provision Cosmos DB with appropriate database and containers
- Verify all resources are properly configured and accessible

## Steps to Complete

### Part 1: Verify Pre-Deployed Resource Group

1. In the **Azure Portal**, search for **Resource groups** in the top search bar and select it.

1. You should see a pre-deployed resource group named **challenge-rg-<inject key="DeploymentID"></inject>**.

1. Click on **challenge-rg-<inject key="DeploymentID"></inject>** to open it.

1. This resource group will be used for all resources you create in this hackathon.

### Part 2: Create Microsoft Foundry Project with Model Deployment

1. In the **Azure Portal**, search for **Microsoft Foundry** and select it.

1. In the **Use with Foundry** tab, click on **Foundry**.

1. Click **+ Create** to create a new Foundry project.

1. Configure the AI Foundry project:

   - **Subscription**: Select the avialble **Azure subscription**.
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Project name**: **sql-modernize-<inject key="DeploymentID"></inject>**
   - **Region**: **<inject key="Region"></inject>**.
   - **Default project name**: Keep the name **Default**.
   - Click **Review + Create**.

1. Click **Create**.

1. Wait for deployment (2-3 minutes).

1. Once created, click **Go to Foundry Project** in the overview section.

### Part 3: Deploy GPT-4.1 Model in AI Foundry

1. In **Microsoft Foundry Studio**.

1. Click on **Models + Endpoints** in the left navigation menu.

1. Click **+ Deploy model** and select **Deploy base model**.

1. Search for and select **gpt-4.1** from the model catalog and click **Confirm**.

1. Configure the deployment:

   - **Deployment name**: `sql-translator`
   - **Deployment type**: **Global Standard**
   - Click **Customize**.
   - **Tokens per Minute Rate Limit**: **50K**

   > **Important**: Do not increase the TPM limit beyond 50K to avoid exceeding quota limits and additional costs.

1. Click **Deploy**.

### Part 4: Test the Model Deployment

1. In your `sql-translator` model deployment.

1. Select **Open in playground**.

1. Test with a simple prompt:
   ```
   Translate this Oracle SQL to Azure SQL: SELECT * FROM dual WHERE ROWNUM <= 5;
   ```

1. Verify you get a response with Azure SQL translation.

### Part 5: Create Azure Cosmos DB

1. In the **Azure Portal**, search for **Azure Cosmos DB** and select it.

1. Click **+ Create**.

1. Select **Azure Cosmos DB for NoSQL** (Core SQL API).

1. Configure Cosmos DB:

   - **Workload Type**: Select **Learning**.
   - **Subscription**: Select the avialble **Azure subscription**.
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**.
   - **Account Name**: **sql-modernization-cosmos-<inject key="DeploymentID"></inject>**.
   - **Availability Zones**: Select **Disable**.
   - **Location**: Keep it **Defualt**.
   - **Capacity mode**: Select **Provisioned throughput**.
   - **Apply Free Tier Discount**: Select **Apply**.
   - **Limit total account throughput**: Turn **On** the **Checkbox**.

1. Click **Review + Create**, then **Create**.

1. Wait for deployment (10-15 minutes).

### Part 6: Create Cosmos DB Database and Containers

1. In your Cosmos DB account, click on **Data Explorer** in the left navigation.

1. Click **New Database**.

1. Configure the database:

   - **Database id**: `SQLModernizationDB`
   - **Provision throughput**: Check this box.
   - **Database throughput**: Select **Manual**.
   - **Database Required RU/s**: **400** RU/s.

1. Click **OK**.

1. Create the first container for translation results:

   - Expand **SQLModernizationDB** and click **New Container**
   - **Database id**: Select **Use existing** and choose **SQLModernizationDB**.
   - **Container id**: `TranslationResults`
   - **Indexing**: Selct **Automatic**.
   - **Partition key**: `/sourceDialect`
   - Click **OK**

1. Create a second container for validation logs:

   - Expand **SQLModernizationDB** and click **New Container** again
   - **Database id**: Select **Use existing** and choose **SQLModernizationDB**.
   - **Container id**: `ValidationLogs`
   - **Indexing**: Selct **Automatic**.
   - **Partition key**: `/translationId`
   - Click **OK**

1. Create a third container for optimization suggestions:

   - Expand **SQLModernizationDB** and click **New Container** again
   - **Database id**: Select **Use existing** and choose **SQLModernizationDB**.
   - **Container id**: `OptimizationResults`
   - **Indexing**: Selct **Automatic**.
   - **Partition key**: `/translationId`
   - Click **OK**

1. Verify all three containers are visible in Data Explorer.

1. Navigate to **Keys** in the left menu under **Settings** and copy:

   - **URI**
   - **PRIMARY KEY**

   Save these values for later use.

### Part 7: Verify All Resources

1. Navigate back to your resource group: **challenge-rg-<inject key="DeploymentID"></inject>**

1. Verify you see the following resources:
   - Microsoft Foundry hub and project resources
   - Cosmos DB account

1. Ensure all resources show **Deployment succeeded** status.

### Part 8: Gather Configuration Values

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
