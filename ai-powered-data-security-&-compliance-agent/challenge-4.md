# Challenge 04: Build the Compliance Advisor Agent and Complete Pipeline

## Introduction

Your classification and risk detection pipeline is working. Now you will add the final agent: the Compliance Advisor Agent. This agent maps identified risks to specific regulations (GDPR, HIPAA, PCI-DSS), generates remediation playbooks, and flags actions that need human approval. You will connect it to complete the three-agent pipeline where data flows automatically through Classification → Risk Detection → Compliance Advisory.

## Challenge Objectives

- Create a Compliance Advisor Agent with regulation mapping and remediation instructions
- Configure the agent to generate actionable remediation playbooks
- Test compliance capabilities with sample risk data
- Connect the Compliance Advisor Agent to the Classification Agent
- Test the complete three-agent pipeline
- Verify all results flow through automatically

## Steps to Complete

### Task 1: Create the Compliance Advisor Agent

1. In **Microsoft Foundry**, navigate to **Agents**.

1. Click on **+ New agent**.

1. Configure:

   - **Agent name**: `Compliance-Advisor-Agent`
   - **Deployment**: Select **data-security-model**

<validation step="b0d8e4f1-7a52-4c23-d8e9-5a1b6c3d4e72" />

> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 2: Write Compliance Advisor Instructions

1. In the **Instructions** text box, copy and paste the following:

   ```
   You are a Data Security Compliance Advisor. Your role is to take identified security risks and map them to specific regulatory requirements, generate detailed remediation playbooks, and flag actions that require human approval before execution.

   REGULATION MAPPING:

   1. GDPR (General Data Protection Regulation):
      - Article 5: Data must be processed lawfully, fairly, and transparently
      - Article 6: Lawful basis required for processing personal data
      - Article 25: Data protection by design and by default
      - Article 32: Security of processing (encryption, pseudonymization)
      - Article 33: Breach notification within 72 hours
      - Article 35: Data Protection Impact Assessment for high-risk processing
      - Article 44-49: Cross-border data transfer restrictions
      - Applies to: PII data (names, SSN, email, phone, date of birth, addresses)
      - Key requirements: consent, data minimization, right to erasure, breach notification

   2. HIPAA (Health Insurance Portability and Accountability Act):
      - Privacy Rule: Limits use and disclosure of PHI
      - Security Rule: Administrative, physical, and technical safeguards
      - Minimum Necessary Standard: Only access PHI needed for the task
      - Business Associate Agreements: Required for third-party PHI access
      - Breach Notification Rule: Notify within 60 days of discovery
      - Applies to: PHI data (diagnoses, treatments, medications, lab results, insurance IDs)
      - Key requirements: access controls, audit trails, encryption, training

   3. PCI-DSS (Payment Card Industry Data Security Standard):
      - Requirement 3: Protect stored cardholder data (encryption, masking)
      - Requirement 7: Restrict access by business need-to-know
      - Requirement 8: Identify and authenticate access (MFA)
      - Requirement 10: Track and monitor all access (audit logging)
      - Requirement 11: Regularly test security systems
      - Requirement 12: Maintain information security policy
      - Applies to: PCI data (card numbers, CVV, expiry dates, account numbers)
      - Key requirements: encryption at rest/transit, tokenization, access logging, penetration testing

   REMEDIATION PLAYBOOK GENERATION:

   For each identified risk, generate a remediation step with:
   1. What to do (specific technical action)
   2. How to do it (step-by-step implementation guide)
   3. Priority (Immediate, Short-term within 7 days, Medium-term within 30 days)
   4. Who should do it (Security team, DBA, IT Admin, Compliance Officer)
   5. Whether human approval is required before execution
   6. Estimated effort (hours)

   APPROVAL REQUIREMENTS:
   - CRITICAL risks: Require Security Director approval before remediation
   - Revoking access from active users: Requires Manager + Security approval
   - Changing database permissions: Requires DBA + Security approval
   - Blocking IP addresses: Requires Network Security approval
   - LOW/MEDIUM risks: Can be auto-approved and executed

   OUTPUT FORMAT:
   Return your compliance analysis as a JSON object:
   ```json
   {
     "compliance_summary": {
       "total_violations": number,
       "gdpr_violations": number,
       "hipaa_violations": number,
       "pci_dss_violations": number,
       "overall_compliance_score": 0 to 100,
       "risk_level": "CRITICAL|HIGH|MEDIUM|LOW"
     },
     "regulation_mapping": [
       {
         "risk_id": "APR-001 or ACT-001",
         "regulation": "GDPR|HIPAA|PCI-DSS",
         "specific_article": "Article or Requirement number",
         "violation_description": "How this risk violates the regulation",
         "potential_penalty": "Fine range or consequence"
       }
     ],
     "remediation_playbook": [
       {
         "step_id": "REM-001",
         "risk_id": "APR-001",
         "action": "What needs to be done",
         "implementation": "Step-by-step instructions",
         "priority": "Immediate|Short-term|Medium-term",
         "assigned_to": "Security Team|DBA|IT Admin|Compliance Officer",
         "requires_approval": true or false,
         "approver": "Security Director|Manager|DBA",
         "estimated_hours": number,
         "regulation_reference": "GDPR Art. 32|HIPAA Security Rule|PCI-DSS Req. 3"
       }
     ],
     "approval_queue": [
       {
         "action": "Description of action needing approval",
         "risk_id": "Reference to the risk",
         "approver": "Who needs to approve",
         "urgency": "Immediate|24 hours|7 days",
         "impact": "What happens if not approved"
       }
     ]
   }
   ```

   SCORING GUIDELINES:
   - 90-100: Fully compliant, minor improvements possible
   - 70-89: Mostly compliant, some gaps to address
   - 50-69: Significant compliance gaps, action required
   - Below 50: Non-compliant, immediate remediation needed

   IMPORTANT RULES:
   - Every CRITICAL and HIGH risk must have a remediation step
   - PHI exposure without audit logging is always a HIPAA violation
   - PCI data without encryption is always a PCI-DSS violation
   - Intern or contractor access to PHI/PCI without MFA is always flagged for approval
   - Include estimated penalties for regulation violations where applicable
   - Remediation steps must be specific and actionable, not generic advice
   ```

1. The agent will auto-save the instructions.

### Task 3: Add Agent Description

1. Expand the **Agent Description** section and add:

   ```
   Maps identified security risks to GDPR, HIPAA, and PCI-DSS regulations. Generates actionable remediation playbooks with step-by-step implementation, priority levels, and human approval requirements. Returns structured JSON with compliance scores and violation details.
   ```

### Task 4: Test the Compliance Advisor Agent Independently

1. Click the **Try in playground** button.

1. Test with the following risk scenario:

   ```
   Generate compliance remediation for these identified risks:

   RISK 1 (CRITICAL - APR-001):
   Role: Intern has SELECT * access to Customers table containing SSN (PII), CreditCardNumber (PCI), CVV (PCI). No data masking, no MFA, no audit logging.

   RISK 2 (CRITICAL - ACT-001):
   User: jake.morrison (Intern) executed "SELECT FirstName, LastName, SSN, CreditCardNumber, CVV FROM Customers" returning 48500 rows at 2:47 AM.

   RISK 3 (HIGH - ACT-002):
   User: wei.zhang (Intern) executed "SELECT * FROM FinancialTransactions" returning 125000 rows at 3:12 AM from IP 103.45.67.89 (foreign).

   RISK 4 (HIGH - APR-002):
   Role: Marketing Lead has SELECT * access to MedicalRecords table containing PrimaryDiagnosis (PHI), Treatment (PHI), Medications (PHI). No data masking, no audit logging. Last access review: 2024-06-15.

   RISK 5 (MEDIUM - CMP-001):
   Role: Data Analyst has access to all tables without MFA and without audit logging. Last review: 2024-08-10.
   ```

1. Verify the agent returns:
   - Regulation mapping (GDPR for PII, PCI-DSS for card data, HIPAA for medical data)
   - Specific articles/requirements cited for each violation
   - Remediation steps with assigned owners and priority levels
   - Approval queue for critical actions (revoking intern access, blocking foreign IP)
   - Overall compliance score below 50 (given the severity of risks)

### Task 5: Connect Compliance Advisor to Classification Agent

> **Note**: Similar to the modernize-your-code pattern, an agent that is already connected (like Risk Detection Agent) cannot have its own connected agents. Therefore, connect the Compliance Advisor Agent directly to the Classification Agent as a second connected agent.

1. Go to the **Agents** list.

1. Click on **Data-Classification-Agent** (the first agent).

1. In the **Setup** panel on the right, scroll to the **Connected agents** section.

1. You should already see **risk_detection_agent** listed. Click on **+ Add** to add a second connected agent.

1. In the **Adding a connected agent** dialog, configure:

   - **Agent**: Select **Compliance-Advisor-Agent** from the dropdown
   - **Unique name**: Enter `compliance_advisor_agent`
   - **Detail the steps to activate the agent**: Enter:

     ```
     After the risk detection analysis is complete, automatically transfer all classification results and risk findings to the Compliance-Advisor-Agent for regulation mapping and remediation playbook generation.
     ```

1. Click on **Add**.

1. You should now see both connected agents listed:
   - risk_detection_agent
   - compliance_advisor_agent

### Task 6: Update Classification Agent Instructions

1. From the **Data-Classification-Agent**, scroll to the **Instructions** text box.

1. Find the `PIPELINE INSTRUCTIONS` section you added in Challenge 3 and **replace it** with this updated version:

   ```
   PIPELINE INSTRUCTIONS (MANDATORY):
   After classifying all columns in the data asset, you MUST execute these steps in order:
   1. Hand off the classification results along with the access policies and activity logs to risk_detection_agent for security risk analysis
   2. After risk detection completes, hand off the classification results and risk findings to compliance_advisor_agent for regulation mapping and remediation playbook generation
   3. Include the results from all three stages (classification, risk detection, compliance advisory) in your final response
   ```

1. Your complete Classification Agent instructions should now end with:

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
   2. After risk detection completes, hand off the classification results and risk findings to compliance_advisor_agent for regulation mapping and remediation playbook generation
   3. Include the results from all three stages (classification, risk detection, compliance advisory) in your final response
   ```

1. The agent will auto-save.

### Task 7: Test the Complete Three-Agent Pipeline

1. Go back to **Data-Classification-Agent**.

1. Click on **Try in playground**.

1. Send this comprehensive scan request:

   ```
   Perform a complete security scan on the following data:

   DATABASE SCHEMA:
   Database: RetailDB, Table: Customers, Total Rows: 48500
   Columns: CustomerID (INT), FirstName (VARCHAR), LastName (VARCHAR), SSN (VARCHAR), Email (VARCHAR), Phone (VARCHAR), CreditCardNumber (VARCHAR), CVV (VARCHAR), CardExpiry (VARCHAR), DateOfBirth (DATE), AccountStatus (VARCHAR), Notes (TEXT)

   Sample Data:
   1. CustomerID: 1001, SSN: 123-45-6789, CreditCardNumber: 4532-1234-5678-9012, CVV: 847, Notes: "Customer mentioned SSN issue with account 987-65-4321"
   2. CustomerID: 1002, SSN: 234-56-7890, CreditCardNumber: 5412-7534-9821-0063, CVV: 312

   ACCESS POLICIES:
   Role: Intern — Tables: Customers, FinancialTransactions — Permissions: SELECT * — Masking: None — MFA: No — Audit: No
   Role: Data Analyst — Tables: ALL — Permissions: SELECT * — Masking: None — MFA: No — Audit: No — Last Review: 2024-08-10

   ACCESS LOGS:
   2025-06-15 02:47:00 | jake.morrison (Intern) | SELECT FirstName, LastName, SSN, CreditCardNumber, CVV FROM Customers | 48500 rows | IP: 10.0.1.45 | Status: Success
   2025-06-15 03:12:00 | wei.zhang (Intern) | SELECT * FROM FinancialTransactions | 125000 rows | IP: 103.45.67.89 | Status: Success
   ```

1. Observe the three-agent flow:
   - **Agent 1 (Classification)**: Classifies all columns (SSN → PII, CreditCardNumber → PCI, CVV → PCI, etc.)
   - **Agent 2 (Risk Detection)**: Flags intern access, after-hours bulk exports, foreign IP, missing MFA/audit
   - **Agent 3 (Compliance Advisor)**: Maps to GDPR/PCI-DSS, generates remediation steps, creates approval queue

1. Verify that you see results from ALL THREE agents in the conversation.

### Task 8: Test with Medical Records Scenario

1. Send this healthcare-focused scan:

   ```
   Perform a complete security scan:

   DATABASE SCHEMA:
   Database: HealthcareDB, Table: MedicalRecords, Total Rows: 32000
   Columns: RecordID (INT), PatientName (VARCHAR), SSN (VARCHAR), PrimaryDiagnosis (VARCHAR), DiagnosisCode (VARCHAR), Treatment (VARCHAR), Medications (VARCHAR), Notes (TEXT)

   Sample: PatientName: Alice Thompson, SSN: 111-22-3333, PrimaryDiagnosis: Major Depressive Disorder, DiagnosisCode: F33.1, Notes: "Patient expressed suicidal ideation. Emergency contact: wife Maria 555-0199."

   ACCESS POLICIES:
   Role: Marketing Lead — Tables: Customers, MedicalRecords — Permissions: SELECT * — Masking: None — MFA: Yes — Audit: No — Last Review: 2024-06-15

   ACCESS LOGS:
   2025-06-14 14:30:00 | jessica.taylor (Marketing Lead) | SELECT PatientName, PrimaryDiagnosis, Medications FROM MedicalRecords | 32000 rows | IP: 10.0.2.78 | Status: Success
   ```

1. Verify the pipeline identifies:
   - Classification: PHI columns (diagnosis, treatment, medications, notes)
   - Risk: Marketing Lead accessing PHI data without business justification
   - Compliance: HIPAA Privacy Rule violation, stale access review, missing audit logging
   - Remediation: Revoke Marketing access to MedicalRecords, enable audit logging, require access review

### Task 9: Test Error Scenario

1. Send a scan with minimal access issues to test low-risk scenarios:

   ```
   Perform a complete security scan:

   DATABASE SCHEMA:
   Database: PublicDB, Table: Products, Total Rows: 5000
   Columns: ProductID (INT), ProductName (VARCHAR), Category (VARCHAR), Price (DECIMAL), Description (TEXT)

   ACCESS POLICIES:
   Role: Data Analyst — Tables: Products — Permissions: SELECT * — Masking: N/A — MFA: Yes — Audit: Yes — Last Review: 2025-05-01

   ACCESS LOGS:
   2025-06-15 10:30:00 | analyst1 (Data Analyst) | SELECT * FROM Products | 5000 rows | IP: 10.0.1.22 | Status: Success
   ```

1. Verify the pipeline handles low-risk data correctly:
   - Classification: All columns classified as PUBLIC
   - Risk: Minimal or no risks flagged
   - Compliance: High compliance score (90+), minor suggestions only

### Task 10: Save All Agent IDs

1. Go back to the **Agents** list.

1. Note the **Agent ID** for **Compliance-Advisor-Agent**.

1. Confirm you have all three agent IDs saved in Notepad:
   - Data-Classification-Agent: asst_xxxxx
   - Risk-Detection-Agent: asst_xxxxx
   - Compliance-Advisor-Agent: asst_xxxxx

1. You will only need the **Data-Classification-Agent** ID for the Streamlit app (since it is the pipeline entry point that orchestrates the other two).

## Success Criteria

- Compliance Advisor Agent created with correct model deployment
- Agent maps risks to specific GDPR, HIPAA, and PCI-DSS articles/requirements
- Agent generates actionable remediation playbooks with priorities and owners
- Agent correctly identifies actions requiring human approval
- Compliance Advisor Agent connected to Classification Agent as second connected agent
- Complete three-agent pipeline tested: Classification → Risk Detection → Compliance Advisory
- All results from three agents flow through automatically
- Healthcare scenario correctly triggers HIPAA-specific remediations
- Low-risk scenario returns high compliance scores

## Additional Resources

- [GDPR Official Text](https://gdpr-info.eu/)
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [PCI DSS v4.0 Summary](https://www.pcisecuritystandards.org/document_library/)
- [Azure Compliance Offerings](https://learn.microsoft.com/azure/compliance/)

Now, click **Next** to continue to **Challenge 05**.
