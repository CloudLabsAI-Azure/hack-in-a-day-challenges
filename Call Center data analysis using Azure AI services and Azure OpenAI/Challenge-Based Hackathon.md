# Challenge: Call Center Data Analysis using Azure AI Services and Azure OpenAI

* Lab 01: Provision Azure Resources – 60 mins
* Lab 02: Upload Audio Files – 45 mins
* Lab 03: Visualization with Power BI – 120 mins

---

## Problem Statement

A leading call center handles thousands of customer calls daily. Each conversation may contain critical insights such as customer sentiment, recurring issues, and service feedback. Currently, this data remains underutilized.

In this challenge, you will build an **AI-driven analytics pipeline** using **Azure AI Services, Azure OpenAI, and Power BI** to:

* Transcribe audio calls.
* Perform conversation summarization and sentiment analysis.
* Visualize insights for operational efficiency and improved customer satisfaction.

---

## Goals

* Provision Azure resources to handle audio transcription, conversation analysis, and SQL data storage.
* Upload customer call audio files for processing.
* Generate actionable insights using Azure OpenAI.
* Visualize sentiment trends and conversation summaries in Power BI dashboards.

---

##  Datasets

Use the sample audio recordings provided in the lab VM:

| File Path                                          | Description                |
| -------------------------------------------------- | -------------------------- |
| `C:\LabFiles\Recordings\bad_review.wav`            | Sample customer complaint  |
| `C:\LabFiles\Recordings\Call_pharmacy_call.wav`    | Customer inquiry           |
| `C:\LabFiles\Recordings\Call_apply_loan.wav`       | Loan application call      |
| `C:\LabFiles\Recordings\Call_health_insurance.wav` | Health insurance inquiry   |
| `C:\LabFiles\Recordings\good_review.wav`           | Positive customer feedback |

Additionally, the **Power BI report file**:

* `C:\LabFiles\callcenter-dataanalysis.pbix` (prebuilt report with models and visuals)

---

##  Challenge Objectives

###  Challenge 1: Provision Azure Resources

**Estimated Time:** 60 minutes

#### Objective

Deploy Azure resources for audio transcription, conversation analysis, and SQL data storage.

#### Tasks

**Task 1.1 – Deploy Resources with ARM Template**

1. In Azure Portal, search **Deploy a custom template**.
2. Select **Build your own template in the editor**.
3. Click **Load file** → Navigate to `C:\LabFiles` → Select `azuredeploy-01.json`.
4. Click **Save**.
5. On **Custom deployment** blade:

   * Resource group: `callcenter-`
   * Deployment ID: enter a unique value
   * Leave other parameters as default
6. Click **Review + Create → Create**
7. Wait ~6–7 minutes for deployment completion.

**Task 1.2 – Create Output Table in Azure SQL Database**

1. Open Azure SQL Database `Database-`.
2. Open **Query Editor (Preview)**.
3. Login:

   ```
   Username: sqluser
   Password: password.1!!
   ```
4. Paste and execute:

   ```sql
   CREATE TABLE dbo.Output (
       ID NVARCHAR(255) NOT NULL PRIMARY KEY,
       FileName NVARCHAR(MAX) NULL,
       Sentiment NVARCHAR(MAX) NULL,
       Summary NVARCHAR(MAX) NULL
   );
   ```
5. Verify table creation:

   ```sql
   SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Output';
   ```

####  Validation Check

* ARM deployment succeeded.
* `dbo.Output` table exists in SQL Database.

---

### Challenge 2: Upload Audio Files

**Estimated Time:** 45 minutes

#### Objective

Upload audio recordings and trigger transcription and analysis via Azure Functions.

#### Tasks

**Task 2.1 – Restart Function Apps**

1. Go to Azure **Function Apps**.
2. Restart each function: `StartTranscriptionFunction`, `FetchTranscriptionFunction`, `AnalyzeTranscriptionFunction`.
3. Ensure all functions are running.

**Task 2.2 – Upload Audio Files**

1. Go to **Storage Account → callcenterstore → Containers → audio-input**.
2. Upload the following files:

   * `bad_review.wav`
   * `Call_pharmacy_call.wav`
   * `Call_apply_loan.wav`
3. Wait 5–6 minutes.
4. Verify that JSON transcripts appear in `json-result-output` container.

####  Validation Check

* JSON transcripts exist in `json-result-output`.
* Functions processed the audio files correctly.

---

### Challenge 3: Visualization using Power BI

**Estimated Time:** 120 minutes

#### Objective

Connect Power BI to SQL Database, refresh prebuilt report, and create interactive dashboard.

#### Tasks

**Task 3.1 – Open Power BI Report**

1. Open **Power BI Desktop** from the lab VM.
2. Click **Open → Browse this device → `C:\LabFiles\callcenter-dataanalysis.pbix` → Open**.
3. Cancel any SQL Server pop-ups and close **Evaluating Queries** windows.

**Task 3.2 – Update Data Source Settings**

1. Click **Transform Data → Data source settings → Change Source**.

   * Server: `sqlserver.database.windows.net`
   * Database: `Database-`
2. Click **Edit Permissions → Edit → Database**, and provide credentials:

   ```
   Username: sqluser
   Password: password.1!!
   ```
3. Click **Save → OK → Close → Apply Changes**.

**Task 3.3 – Refresh Report**

* Click **Refresh**.
* Verify that visuals display sentiment distribution, conversation summaries, and trends.

**Task 3.4 – Publish Report Online**

1. Click **Publish → Save**.
2. Sign in with **Azure Work/School account**.
3. Assign report to **My Workspace → Select**.
4. Configure **Gateway authentication**:

   * Method: Basic
   * Username: sqluser
   * Password: password.1!!
   * Privacy Level: None

**Task 3.5 – Pin Report to Dashboard**

1. Open report → ellipsis beside Edit → **Pin to dashboard**.
2. Choose **New dashboard**, name: `callcenter-dataanalysis`, click **Pin live**.
3. Click **Go to dashboard**.
4. Apply filters for specific sentiment or conversation files.

**Task 3.6 – Upload New Audio and Refresh Dashboard**

1. Upload `Call_health_insurance.wav` and `good_review.wav` to `audio-input`.
2. Wait 5–6 minutes.
3. Refresh Power BI dashboard to see updated results.

####  Validation Check

* Report connects to SQL Database.
* Dashboard visuals display correct sentiment and conversation summaries.
* Newly uploaded audio files update dashboard metrics.

---

##  Success Criteria

* Azure resources deployed and operational.
* Audio files transcribed and analyzed using Azure OpenAI.
* Power BI report visualizes correct sentiment and summaries.
* Dashboard reflects updates from newly uploaded audio files.

---

##  Additional Resources

* [Azure Speech Service Documentation](https://learn.microsoft.com/azure/ai-services/speech-service/)
* [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
* [Azure Functions Overview](https://learn.microsoft.com/azure/azure-functions/)
* [Power BI Getting Started](https://learn.microsoft.com/power-bi/fundamentals/)

---

##  Conclusion

In this challenge, you successfully built an **end-to-end AI-powered analytics pipeline** for a call center.
You automated:

* Audio transcription via Azure Speech Services.
* Conversation summarization and sentiment analysis using Azure OpenAI.
* Visualization of insights in Power BI dashboards.

This workflow empowers call center management to make **data-driven decisions** and improve customer satisfaction efficiently.

 
