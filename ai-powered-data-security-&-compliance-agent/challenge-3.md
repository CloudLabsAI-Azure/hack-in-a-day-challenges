# Challenge 03: Build the Risk Detection Agent and Connect Pipeline

## Introduction

Now that you have a Data Classification Agent, you need a Risk Detection Agent that cross-references data classifications with access policies and activity logs to find security threats. In this challenge, you will create the second agent, then connect it to the Classification Agent using the "Connected agents" feature so classifications automatically flow to risk analysis — creating your first multi-agent pipeline.

## Challenge Objectives

- Create a Risk Detection Agent with access analysis instructions
- Configure the agent to detect over-privilege, suspicious activity, and compliance gaps
- Test risk detection with sample access policies and logs
- Connect the Risk Detection Agent to the Classification Agent using "Connected agents"
- Test the complete pipeline: Classification → Risk Detection
- Verify that the hand-off works automatically

## Steps to Complete

### Task 1: Create the Risk Detection Agent

1. In **Microsoft Foundry**, navigate to **Agents**.

1. Click on **+ New agent**.

1. Configure the agent:

   - **Agent name**: `Risk-Detection-Agent`
   - **Deployment**: Select **data-security-model**

<validation step="f8b6c2d9-5e30-4a01-b6c7-3e9d4f1a2b50" />

> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 2: Write Risk Detection Instructions

1. In the **Instructions** text box, copy and paste the following:

   ```
   You are a Data Security Risk Detection Specialist. Your role is to analyze data classifications alongside access policies and activity logs to identify security risks, over-privileged access, suspicious activity patterns, and compliance violations.

   RISK DETECTION ANALYSIS:

   1. Over-Privilege Detection:
      - Compare each role's permissions against the data classifications
      - Flag roles with access to PII/PHI/PCI columns that do not require it for their job function
      - Identify roles with SELECT * permissions on tables containing sensitive data
      - Flag roles without data masking on sensitive columns
      - Detect roles with write/delete permissions on sensitive tables without justification
      - Flag intern, contractor, or temporary roles with access to sensitive data

   2. Access Anomaly Detection:
      - Identify access outside business hours (before 6 AM or after 10 PM)
      - Flag bulk data exports (SELECT * or large row counts on sensitive tables)
      - Detect access from unusual IP addresses or geographic locations
      - Identify users accessing tables outside their normal pattern
      - Flag excessive query volume from a single user in a short timeframe
      - Detect specific column targeting (e.g., querying only SSN and Name columns)

   3. Policy Compliance Gaps:
      - Flag roles missing MFA requirements when accessing sensitive data
      - Identify roles without audit logging enabled
      - Detect stale access reviews (last review date older than 90 days)
      - Flag missing data masking policies for PII/PHI/PCI columns
      - Identify broad access rules (e.g., "ALL TABLES" or "SELECT *")
      - Detect contractor or external users with unaudited access

   4. Cross-Reference Analysis:
      - Map classification results to access policies to find mismatches
      - Correlate anomalous log entries with the user's assigned role permissions
      - Identify patterns where multiple anomalies point to the same user or role
      - Flag users who accessed data they should not have based on their role

   SEVERITY LEVELS:
   - CRITICAL: Immediate threat — active data exfiltration, unauthorized PHI/PCI access, bulk export of sensitive data at unusual hours
   - HIGH: Significant risk — over-privileged roles with PII/PHI access, missing MFA on sensitive data access, foreign IP access
   - MEDIUM: Compliance gap — stale reviews, missing audit logs, broad permissions that should be narrowed
   - LOW: Improvement opportunity — missing data masking on low-risk fields, minor policy updates needed

   OUTPUT FORMAT:
   Return your risk analysis as a JSON object:
   ```json
   {
     "scan_summary": {
       "total_risks_found": number,
       "critical": number,
       "high": number,
       "medium": number,
       "low": number,
       "highest_risk_role": "role_name",
       "highest_risk_user": "user_name"
     },
     "access_policy_risks": [
       {
         "risk_id": "APR-001",
         "severity": "CRITICAL|HIGH|MEDIUM|LOW",
         "role": "role_name",
         "issue": "Description of the access policy risk",
         "affected_data": ["column or table names"],
         "classification_impact": "PII|PHI|PCI|CONFIDENTIAL",
         "regulation_violated": ["GDPR", "HIPAA", "PCI-DSS"],
         "evidence": "Specific policy detail that creates the risk"
       }
     ],
     "activity_anomalies": [
       {
         "risk_id": "ACT-001",
         "severity": "CRITICAL|HIGH|MEDIUM|LOW",
         "user": "user_name",
         "role": "user_role",
         "anomaly_type": "after_hours|bulk_export|unusual_ip|column_targeting|excessive_queries",
         "description": "What happened and why it is suspicious",
         "timestamp": "when it occurred",
         "affected_data": ["tables or columns accessed"],
         "evidence": "Specific log entry details"
       }
     ],
     "compliance_gaps": [
       {
         "risk_id": "CMP-001",
         "severity": "MEDIUM|LOW",
         "area": "MFA|Audit|Review|Masking",
         "description": "What compliance requirement is not met",
         "affected_roles": ["role names"],
         "regulation": "GDPR|HIPAA|PCI-DSS"
       }
     ]
   }
   ```

   IMPORTANT RULES:
   - Always cross-reference classifications with access policies — do not analyze them in isolation
   - Flag ANY role that has unmasked access to SSN, credit card numbers, or medical diagnoses
   - Intern and contractor roles accessing sensitive data should always be HIGH or CRITICAL
   - After-hours bulk exports of sensitive data are always CRITICAL
   - Access from foreign IP addresses to sensitive data is always HIGH
   - Include specific evidence (log entries, policy details) for every risk found
   ```

1. The agent will auto-save the instructions.

### Task 3: Add Agent Description

1. Expand the **Agent Description** section and add:

   ```
   Analyzes data classifications alongside access policies and activity logs to detect over-privileged roles, suspicious access patterns, and compliance violations. Returns structured JSON with severity-rated risks and evidence.
   ```

### Task 4: Test the Risk Detection Agent Independently

1. Click the **Try in playground** button.

1. Test with the following sample scenario:

   ```
   Analyze the following for security risks:

   CLASSIFICATION RESULTS:
   - Customers.SSN: PII (GDPR)
   - Customers.CreditCardNumber: PCI (PCI-DSS)
   - Customers.CVV: PCI (PCI-DSS)
   - Customers.Email: PII (GDPR)
   - MedicalRecords.PrimaryDiagnosis: PHI (HIPAA)
   - MedicalRecords.Medications: PHI (HIPAA)
   - Employees.Salary: CONFIDENTIAL
   - Employees.SSN: PII (GDPR)

   ACCESS POLICIES:
   Role: Data Analyst
   - Tables: ALL (Customers, MedicalRecords, Employees, FinancialTransactions)
   - Permissions: SELECT *
   - Data Masking: None
   - MFA Required: No
   - Audit Logging: No
   - Last Review: 2024-08-10

   Role: Intern
   - Tables: Customers, FinancialTransactions
   - Permissions: SELECT *
   - Data Masking: None
   - MFA Required: No
   - Audit Logging: No
   - Last Review: 2025-01-15

   ACCESS LOGS:
   - 2025-06-15 02:47:00 | jake.morrison (Intern) | SELECT FirstName, LastName, SSN, CreditCardNumber, CVV FROM Customers | 48500 rows | IP: 10.0.1.45 | Status: Success
   - 2025-06-15 03:12:00 | wei.zhang (Intern) | SELECT * FROM FinancialTransactions | 125000 rows | IP: 103.45.67.89 | Status: Success
   - 2025-06-14 23:45:00 | carlos.dev (Developer_Contractor) | SELECT SSN, Salary, BankAccountNumber FROM Employees | 8500 rows | IP: 85.214.132.77 | Status: Success
   ```

1. Verify that the agent identifies:
   - **CRITICAL**: Intern bulk-exporting SSN + CreditCard + CVV at 2:47 AM
   - **CRITICAL**: Intern accessing FinancialTransactions from foreign IP at 3:12 AM
   - **HIGH**: Developer contractor accessing SSN + Salary from foreign IP late at night
   - **HIGH**: Data Analyst role has unmasked SELECT * on all tables including PHI
   - **HIGH**: Intern role has access to PII/PCI without masking or MFA
   - **MEDIUM**: Multiple roles missing audit logging and MFA

### Task 5: Connect Risk Detection Agent to Classification Agent

Now comes the key step — connecting the agents.

1. Go back to the **Agents** list.

1. Click on your **Data-Classification-Agent** (the first agent you created in Challenge 2).

1. In the **Setup** panel on the right, scroll down to the **Connected agents** section.

1. Click on **+ Add**.

1. In the **Adding a connected agent** pane, configure:

   - **Agent**: Select **Risk-Detection-Agent** from the dropdown
   - **Unique name**: Enter `risk_detection_agent`
   - **Detail the steps to activate the agent**: Enter:

     ```
     After completing the data classification of all columns, automatically transfer the classification results along with the access policies and activity logs to the Risk-Detection-Agent for security risk analysis.
     ```

1. Click on **Add**.

1. You should now see **Risk-Detection-Agent** listed under Connected agents with the unique name `risk_detection_agent`.

<validation step="a9c7d3e0-6f41-4b12-c7d8-4f0a5b2c3d61" />

> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 6: Update Classification Agent Instructions for Hand-Off

1. From the **Data-Classification-Agent** configuration, scroll to the **Instructions** text box.

1. Add the following to the **very end** of your existing Classification Agent instructions (after the IMPORTANT RULES section):

   ```
   PIPELINE INSTRUCTIONS (MANDATORY):
   After classifying all columns in the data asset, you MUST execute these steps in order:
   1. Hand off the classification results along with the access policies and activity logs to risk_detection_agent for security risk analysis
   2. Include the risk detection results in your response
   ```

1. The complete end of your instructions should now look like:

   ```
   IMPORTANT RULES:
   - Classify EVERY column, do not skip any
   - When a column could fall into multiple categories, choose the HIGHEST sensitivity (PHI > PII > PCI > CONFIDENTIAL > PUBLIC)
   - Free-text "Notes" fields should be examined for embedded PII/PHI patterns in sample data
   - Date of birth is PII, not PUBLIC
   - Email and phone are PII even when stored alone
   - Account numbers and routing numbers are PCI
   - Always include the applicable regulations for each classification

   PIPELINE INSTRUCTIONS (MANDATORY):
   After classifying all columns in the data asset, you MUST execute these steps in order:
   1. Hand off the classification results along with the access policies and activity logs to risk_detection_agent for security risk analysis
   2. Include the risk detection results in your response
   ```

1. The agent will auto-save.

### Task 7: Test the Connected Pipeline

1. Go back to **Data-Classification-Agent**.

1. Click on **Try in playground**.

1. Send this combined scan request:

   ```
   Classify the following data asset and analyze for security risks:

   DATABASE SCHEMA:
   Database: RetailDB, Table: Customers, Total Rows: 48500
   Columns: CustomerID (INT), FirstName (VARCHAR), LastName (VARCHAR), SSN (VARCHAR), Email (VARCHAR), Phone (VARCHAR), CreditCardNumber (VARCHAR), CVV (VARCHAR), DateOfBirth (DATE), AccountStatus (VARCHAR), CreatedDate (DATETIME)

   Sample: CustomerID: 1001, FirstName: John, LastName: Smith, SSN: 123-45-6789, Email: john.smith@email.com, CreditCardNumber: 4532-1234-5678-9012, CVV: 847

   ACCESS POLICIES:
   Role: Intern — Tables: Customers — Permissions: SELECT * — Masking: None — MFA: No — Audit: No

   ACCESS LOGS:
   2025-06-15 02:47:00 | jake.morrison (Intern) | SELECT FirstName, LastName, SSN, CreditCardNumber, CVV FROM Customers | 48500 rows | IP: 10.0.1.45 | Status: Success
   ```

1. Observe what happens:
   - Classification Agent classifies all columns (SSN → PII, CreditCardNumber → PCI, etc.)
   - Classification Agent automatically hands off to Risk Detection Agent
   - Risk Detection Agent analyzes the intern's access and flags risks
   - You see results from BOTH agents in the conversation

1. Verify that you see:
   - Column classifications from Agent 1
   - Risk analysis from Agent 2 (intern with unmasked PCI/PII access, after-hours bulk export)

### Task 8: Test with a Complex Scenario

1. In the same playground, send a more comprehensive scan:

   ```
   Classify and analyze:

   DATABASE SCHEMA:
   Database: HealthcareDB, Table: MedicalRecords, Total Rows: 32000
   Columns: RecordID (INT), PatientName (VARCHAR), SSN (VARCHAR), PrimaryDiagnosis (VARCHAR), DiagnosisCode (VARCHAR), Treatment (VARCHAR), Medications (VARCHAR), Notes (TEXT)

   Sample: RecordID: 5001, PatientName: Alice Thompson, SSN: 111-22-3333, PrimaryDiagnosis: Type 2 Diabetes, DiagnosisCode: E11.9, Treatment: Insulin therapy, Medications: Metformin 500mg, Notes: "Patient reports non-compliance with diet."

   ACCESS POLICIES:
   Role: Marketing Lead — Tables: Customers, MedicalRecords — Permissions: SELECT * — Masking: None — MFA: Yes — Audit: No — Last Review: 2024-06-15

   ACCESS LOGS:
   2025-06-14 14:30:00 | jessica.taylor (Marketing Lead) | SELECT PatientName, PrimaryDiagnosis, Medications FROM MedicalRecords | 32000 rows | IP: 10.0.2.78 | Status: Success
   ```

1. Verify:
   - Agent 1 classifies PHI columns (diagnosis, treatment, medications)
   - Agent 2 flags Marketing Lead accessing medical records (PHI data — should not have access)
   - Agent 2 flags stale review date (June 2024, over 12 months old)
   - Both results appear in the conversation

### Task 9: Save Agent IDs

1. Go back to the **Agents** list.

1. Note the **Agent ID** for **Risk-Detection-Agent**.

1. Keep both agent IDs (Classification and Risk Detection) saved in Notepad.

## Success Criteria

- Risk Detection Agent created with correct model deployment
- Agent identifies over-privileged roles, suspicious activity, and compliance gaps
- Agent returns structured JSON with severity ratings and evidence
- Risk Detection Agent connected to Classification Agent via "Connected agents"
- Pipeline tested: data input → Classification → Risk Detection
- Hand-off happens automatically without manual intervention
- Both agent results are visible in the playground conversation
- Complex scenarios (PHI access by Marketing, after-hours bulk exports) correctly flagged

## Additional Resources

- [Azure AI Agents - Connected Agents](https://learn.microsoft.com/azure/ai-studio/how-to/develop/agents#connected-agents)
- [NIST Data Security Guidelines](https://www.nist.gov/data)
- [Principle of Least Privilege](https://learn.microsoft.com/security/zero-trust/develop/least-privilege)

Now, click **Next** to continue to **Challenge 04**.
