# Challenge 01: Set Up Azure Infrastructure

## Introduction

Before building the AI-powered SQL modernization pipeline, you need to provision the necessary Azure infrastructure. This challenge involves creating Azure AI Foundry project with GPT-4 model deployment, Cosmos DB for storing results and logs, Azure Storage for SQL file uploads, and an optional Azure SQL Database for validation testing.

## Challenge Objectives

- Set up an Azure AI Foundry project with GPT-4 model deployment
- Provision Cosmos DB with appropriate database and containers
- Create an Azure Storage Account for SQL file uploads
- (Optional) Set up Azure SQL Database for real query validation
- Verify all resources are properly configured and accessible

## Steps to Complete

### Part 1: Verify Pre-Deployed Resource Group

1. In the **Azure Portal**, search for **Resource groups** in the top search bar and select it.

2. You should see a pre-deployed resource group named **challenge-rg-<inject key="DeploymentID"></inject>**.

3. Click on **challenge-rg-<inject key="DeploymentID"></inject>** to open it.

4. This resource group will be used for all resources you create in this hackathon.

### Part 2: Create Azure AI Foundry Project with Model Deployment

1. In the **Azure Portal**, search for **Azure AI Foundry** or **Azure AI Studio** and select it.

2. Click **+ New project** to create a new AI Foundry project.

3. Configure the AI Foundry project:
   - **Project name**: **sql-modernization-ai-project**
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Region**: **<inject key="Region"></inject>** (ensure GPT-4 is available in this region)

4. Click **Create**.

5. Wait for deployment (2-3 minutes).

6. Once created, click **Go to project** or navigate to **Azure AI Foundry Studio**.

### Part 3: Deploy GPT-4 Model in AI Foundry

1. In **Azure AI Foundry Studio**, navigate to your project.

2. Click on **Deployments** in the left navigation menu.

3. Click **+ Deploy model** and select **Deploy base model**.

4. Search for and select **gpt-4** from the model catalog.

5. Configure the deployment:
   - **Deployment name**: `gpt-4-sql-translator`
   - **Model version**: Select the latest available version
   - **Deployment type**: **Standard**
   - **Tokens per Minute Rate Limit**: **30K** (or maximum quota available)

6. Click **Deploy**.

7. Wait for deployment to complete (1-2 minutes).

8. Verify the deployment shows as **Succeeded** in the Deployments list.

9. Click on your deployment to view details and copy:
   - **Target URI** (this is your endpoint)
   - Navigate to **Keys and Endpoint** section and copy **Primary Key**

### Part 4: Test the Model Deployment

1. In AI Foundry Studio, click on **Playground** in the left navigation.

2. Select **Chat** playground.

3. Choose your `gpt-4-sql-translator` deployment.

4. Test with a simple prompt:
   ```
   Translate this Oracle SQL to Azure SQL: SELECT * FROM dual WHERE ROWNUM <= 5;
   ```

5. Verify you get a response with Azure SQL translation.

6. This confirms your model is working correctly.

1. In the **Azure Portal**, search for **Azure AI Foundry** (or **Azure AI Studio**).

2. Click **+ Create** to create a new AI Foundry project.

3. Configure the AI Foundry project:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Project name**: **sql-modernization-ai-project**
   - **Region**: **<inject key="Region"></inject>**


4. Click **Review + Create**, then **Create**.

5. Wait for deployment (2-3 minutes).

6. Once created, click **Go to resource** and explore the AI Foundry workspace.

### Part 5: Create Azure Cosmos DB

1. In the **Azure Portal**, search for **Azure Cosmos DB** and select it.

2. Click **+ Create**.

3. Select **Azure Cosmos DB for NoSQL** (Core SQL API).

4. Configure Cosmos DB:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Account Name**: **sql-modernization-cosmos-<inject key="DeploymentID"></inject>**
   - **Location**: **<inject key="Region"></inject>**
   - **Capacity mode**: **Provisioned throughput** (400 RU/s minimum)
   - **Apply Free Tier Discount**: Select **Apply** if available

5. Click **Review + Create**, then **Create**.

6. Wait for deployment (5-7 minutes).

7. Once deployed, click **Go to resource**.

### Part 6: Create Cosmos DB Database and Containers

1. In your Cosmos DB account, click on **Data Explorer** in the left navigation.

2. Click **New Database**.

3. Configure the database:
   - **Database id**: `SQLModernizationDB`
   - **Provision throughput**: Check this box
   - **Database throughput**: **400** RU/s (manual)

4. Click **OK**.

5. Create the first container for translation results:
   - Expand **SQLModernizationDB** and click **New Container**
   - **Container id**: `TranslationResults`
   - **Partition key**: `/sourceDialect`
   - **Container throughput**: Use database throughput
   - Click **OK**

6. Create a second container for validation logs:
   - Click **New Container** again
   - **Container id**: `ValidationLogs`
   - **Partition key**: `/translationId`
   - **Container throughput**: Use database throughput
   - Click **OK**

7. Create a third container for optimization suggestions:
   - Click **New Container** again
   - **Container id**: `OptimizationResults`
   - **Partition key**: `/translationId`
   - **Container throughput**: Use database throughput
   - Click **OK**

8. Verify all three containers are visible in Data Explorer.

9. Navigate to **Keys** in the left menu and copy:
   - **URI**
   - **PRIMARY KEY**

   Save these values for later use.

### Part 7: Create Azure Storage Account

1. In the **Azure Portal**, search for **Storage accounts** and select it.

2. Click **+ Create**.

3. Configure the storage account:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Storage account name**: **sqlmodernization<inject key="DeploymentID"></inject>** (lowercase, no hyphens)
   - **Region**: **<inject key="Region"></inject>**
   - **Performance**: **Standard**
   - **Redundancy**: **Locally-redundant storage (LRS)**

4. Click **Review**, then **Create**.

5. Wait for deployment (1-2 minutes).

6. Once created, go to the resource.

7. In the storage account, navigate to **Containers** under **Data storage**.

8. Click **+ Container** and create:
   - **Name**: `sql-uploads`
   - **Public access level**: **Private**
   - Click **Create**

9. Navigate to **Access keys** and copy:
   - **Storage account name**
   - **Key1** (Connection string)

### Part 8: (Optional) Create Azure SQL Database for Validation

> **Note**: This step is optional but recommended for enabling real database validation in Challenge 3.

1. In the **Azure Portal**, search for **SQL databases** and select it.

2. Click **+ Create**.

3. Configure the SQL database:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Database name**: `ValidationTestDB`
   - **Server**: Click **Create new**
     - **Server name**: **sql-validation-<inject key="DeploymentID"></inject>**
     - **Location**: **<inject key="Region"></inject>**
     - **Authentication method**: **Use SQL authentication**
     - **Server admin login**: `sqladmin`
     - **Password**: `P@ssw0rd123!` (or create a secure password)
     - Click **OK**

4. Configure compute and storage:
   - **Workload environment**: **Development**
   - Click **Configure database**
   - Select **Basic** tier (5 DTUs, 2 GB storage)
   - Click **Apply**

5. Click **Review + Create**, then **Create**.

6. Wait for deployment (3-5 minutes).

7. Once created, navigate to the SQL server resource.

8. Click on **Networking** in the left menu.

9. Under **Firewall rules**, add:
   - **Allow Azure services and resources to access this server**: Check this box
   - Click **+ Add your client IPv4 address** to add your current IP
   - Click **Save**

10. Copy and save:
    - **Server name** (e.g., sql-validation-xxxxx.database.windows.net)
    - **Admin login**: `sqladmin`
    - **Password**: Your chosen password

### Part 9: Verify All Resources

1. Navigate back to your resource group: **challenge-rg-<inject key="DeploymentID"></inject>**

2. Verify you see the following resources:
   - Azure AI Foundry hub and project resources
   - Cosmos DB account
   - Storage account
   - (Optional) SQL database server and database

3. Ensure all resources show **Deployment succeeded** status.

### Part 10: Gather Configuration Values

Create a text file or note with the following information (you'll need these in subsequent challenges):

```text
Azure AI Foundry (with GPT-4 deployment):
- Endpoint: [your-ai-foundry-endpoint or target-uri]
- API Key: [your-primary-key]
- Deployment Name: gpt-4-sql-translator

Cosmos DB:
- URI: https://sql-modernization-cosmos-xxxxx.documents.azure.com:443/
- Primary Key: [your-key]
- Database Name: SQLModernizationDB
- Containers: TranslationResults, ValidationLogs, OptimizationResults

Storage Account:
- Account Name: sqlmodernizationxxxxx
- Connection String: [your-connection-string]
- Container: sql-uploads

Azure SQL (Optional):
- Server: sql-validation-xxxxx.database.windows.net
- Database: ValidationTestDB
- Admin Login: sqladmin
- Password: [your-password]
```

## Success Criteria

- Azure AI Foundry project created with GPT-4 model deployed successfully
- Model tested in Chat Playground and working correctly
- Cosmos DB account created with database and three containers (TranslationResults, ValidationLogs, OptimizationResults)
- Azure Storage Account created with sql-uploads container
- (Optional) Azure SQL Database created with firewall configured
- All connection strings, keys, and endpoints documented for future use
- All resources deployed in the same resource group and region

## Additional Resources

- [Azure OpenAI in AI Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Foundry Overview](https://learn.microsoft.com/azure/ai-studio/)
- [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/azure/cosmos-db/nosql/)
- [Azure Storage Accounts](https://learn.microsoft.com/azure/storage/common/storage-account-overview)
- [Azure SQL Database](https://learn.microsoft.com/azure/azure-sql/database/sql-database-paas-overview)

Now, click **Next** to continue to **Challenge 02**.
