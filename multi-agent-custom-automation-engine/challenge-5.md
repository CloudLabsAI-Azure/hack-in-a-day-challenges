# Challenge 05: End-to-End Execution & Validation

## Introduction

In this final challenge, you will execute and validate the complete Multi-Agent Automation Engine built throughout the hackathon. Rather than focusing on infrastructure deployment, this challenge emphasizes reliability, correctness, and observability of AI-driven workflows.

Participants will run the central orchestrator, trigger multi-agent collaboration using Semantic Kernel, and verify that agents successfully share context, make decisions, and persist execution state in Azure Cosmos DB. This approach ensures that all participants can complete the hackathon within the allotted time, regardless of infrastructure or subscription constraints.

By the end of this challenge, you will have a fully working enterprise-style automation engine that demonstrates real-world AI orchestration patterns without being blocked by cloud deployment limitations.

## Challenge Objectives

* Execute the complete multi-agent workflow end-to-end

* Trigger agent collaboration through the central orchestrator

* Validate agent outputs across extraction, validation, communication, and reporting

* Persist workflow state and execution history in Azure Cosmos DB

* Verify workflow completion, status transitions, and audit traceability

* Demonstrate a production-ready AI orchestration pattern suitable for enterprise automation

## Step 1: Verify Project Structure

Your project root **must look like this**:

```
multi-agent-engine/
│
├─ app/
│   ├─ main.py
│   ├─ orchestrator.py
│   ├─ agents/
│   └─ storage/
│
├─ requirements.txt
├─ Dockerfile
└─ .venv/        (ignored)
```

## Step 2: Create `requirements.txt`

In the **project root**, create a file named:

```
requirements.txt
```

Paste the following:

```txt
semantic-kernel
azure-identity
azure-cosmos
python-dotenv
```

Save the file.

## Step 3: Create the Dockerfile

In the **project root**, create a file named:

```
Dockerfile
```

Paste **exactly** this content, and save the file:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

CMD ["python", "app/main.py"]
```

> **Do NOT copy `.env` files into the image**

## Step 4: Build the Image Using Azure ACR

1. Run the command to login to Azure.

   ```
   az login
   ```

   >**Note:** Sign in with the azure credentials.

2. Run this command from the project root:

   ```powershell
   az acr build --registry agentacr<inject key="DeploymentID" enableCopy="false"/> --image agent-orchestrator:v1 .
   ```

### Expected Result

```
Successfully built and pushed image
```

## Step 5: Verify Image in Azure Portal

1. Open **Azure Portal**
2. Go to **Container Registry → agentacr<inject key="DeploymentID" enableCopy="false"/>**
3. Select **Services** > **Repositories**
4. Confirm:

   ```
   agent-orchestrator : v1
   ```

## Step 6: Run the Multi-Agent Workflow

In this hackathon, the **multi-agent automation engine** is executed **locally** using Azure services for AI and persistence.

This approach ensures:

* Zero infrastructure permission blockers
* Faster execution
* Focus on AI orchestration and agent collaboration

### Run the Workflow

From the project root, run:

```powershell
py app/main.py
```

### Expected Output

```
Workflow completed
Workflow ID: <guid>
```

## Step 7: Verify Workflow State in Azure Cosmos DB

1. Open **Azure Portal**
2. Navigate to **Azure Cosmos DB**
3. Open **Data Explorer**
4. Select:

   * Database: `agent-memory-db`
   * Container: `agent-state`
5. Locate the document using the workflow ID

Confirm the following:

* `status` = `COMPLETED`
* `agentData` contains:

  * extraction
  * validation
  * communication
  * reporting
* `history` shows all agent executions

## Completion Criteria

You have successfully completed the hackathon:

* Multi-agent workflow executes end-to-end
* Agents collaborate using shared state
* Cosmos DB stores the complete workflow history
* Outputs are validated and traceable

Congratulations! You've completed all challenges. 