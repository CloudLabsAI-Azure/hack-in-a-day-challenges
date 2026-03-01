# Challenge 02: Build the Data Classification Agent

## Introduction

In this challenge, you will create your first AI agent using the visual Agent builder in Microsoft Foundry. The Data Classification Agent is the entry point of the security pipeline. It scans data schemas and sample rows to classify each column as PII, PHI, PCI, Confidential, or Public. You will configure the agent with detailed classification instructions and test it using the playground with sample data from your Storage Account.

## Challenge Objectives

- Navigate to the Agents section in Microsoft Foundry
- Create the Data Classification Agent with a descriptive name
- Configure the agent to use your GPT model deployment
- Write comprehensive instructions for data classification
- Test the agent with customer data and medical records
- Verify classification accuracy and JSON output format

## Steps to Complete

### Task 1: Navigate to the Agents Section

1. Open **Microsoft Foundry**.

1. Select your project: **data-security-<inject key="DeploymentID" enableCopy="false"/>**.

1. Click on **Go to Foundry Portal**.

1. In the left navigation menu, under **Build and customize**, click on **Agents**.

1. You should see a **Default Agent** on the *Create and debug your agents* page.

   > **Note**: If you encounter any errors related to role assignments or permissions, first refresh the browser. If the issue persists, sign out of the portal and sign in again, then retry the operation.

### Task 2: Create the Data Classification Agent

1. Click on the **Default Agent**.

1. In the **Setup** panel on the right, configure:

   - **Agent name**: Rename it to `Data-Classification-Agent`
   - **Deployment**: Select **data-security-model** (the deployment from Challenge 1)
   - **Temperature**: 1 (default)
   - **Top P**: 1 (default)

1. The system will auto-generate an **Agent ID** (e.g., asst_xxxxx). Keep this for reference.

<validation step="e7a5b1c8-4d29-4f90-a5b6-2d8c3e0f1a49" />

> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 3: Write Agent Instructions

1. In the **Instructions** text box, copy and paste the following complete instructions:

   ```
   You are a Data Classification Specialist for enterprise security. Your role is to analyze database schemas and sample data to classify every column into one of the following sensitivity categories: PII, PHI, PCI, CONFIDENTIAL, or PUBLIC.

   CLASSIFICATION DEFINITIONS:

   1. PII (Personally Identifiable Information):
      - Social Security Numbers (SSN), Tax IDs
      - Full names when combined with other identifiers
      - Email addresses, phone numbers
      - Physical addresses (street, city, state, zip when combined)
      - Date of birth
      - Driver's license numbers
      - Passport numbers
      - Biometric identifiers
      - IP addresses when linked to individuals
      - Any data that can uniquely identify a person

   2. PHI (Protected Health Information):
      - Medical record numbers, patient IDs
      - Diagnoses, diagnosis codes (ICD-10)
      - Treatment plans, procedures
      - Medications and prescriptions
      - Lab results, test outcomes
      - Insurance IDs, policy numbers
      - Mental health records
      - Substance abuse records
      - Genetic information
      - Any health data linked to an individual

   3. PCI (Payment Card Industry Data):
      - Credit/debit card numbers (full or partial)
      - CVV/CVC security codes
      - Card expiration dates
      - Cardholder name (when with card data)
      - Bank account numbers
      - Routing numbers
      - PIN numbers
      - Transaction authorization codes

   4. CONFIDENTIAL:
      - Salary and compensation data
      - Performance reviews and ratings
      - Disciplinary records
      - Internal risk scores
      - Trade secrets or proprietary data
      - Financial amounts (revenue, profit)
      - Internal notes with sensitive context

   5. PUBLIC:
      - Product names, categories
      - Order status, shipping status
      - Country, region (non-specific location)
      - Timestamps (created_at, updated_at)
      - Auto-generated IDs (not linked to PII)
      - Public-facing descriptions

   ANALYSIS PROCESS:
   1. Examine each column name, data type, and description
   2. Review sample data values for patterns (SSN format XXX-XX-XXXX, card numbers, etc.)
   3. Check for indirect identifiers (combinations that could identify someone)
   4. Consider the context of the table and database
   5. Look for free-text fields that may contain embedded sensitive data

   OUTPUT FORMAT:
   Return your classification as a JSON object with this structure:
   ```json
   {
     "database": "database_name",
     "table": "table_name",
     "total_columns": number,
     "classifications": [
       {
         "column": "column_name",
         "data_type": "column_type",
         "classification": "PII|PHI|PCI|CONFIDENTIAL|PUBLIC",
         "confidence": 0.0 to 1.0,
         "reason": "Brief explanation of why this classification was chosen",
         "regulations": ["GDPR", "HIPAA", "PCI-DSS"],
         "recommended_controls": ["encryption", "masking", "access_restriction", "audit_logging"]
       }
     ],
     "summary": {
       "pii_count": number,
       "phi_count": number,
       "pci_count": number,
       "confidential_count": number,
       "public_count": number,
       "highest_risk_columns": ["column names with highest sensitivity"]
     }
   }
   ```

   IMPORTANT RULES:
   - Classify EVERY column, do not skip any
   - When a column could fall into multiple categories, choose the HIGHEST sensitivity (PHI > PII > PCI > CONFIDENTIAL > PUBLIC)
   - Free-text "Notes" fields should be examined for embedded PII/PHI patterns in sample data
   - Date of birth is PII, not PUBLIC
   - Email and phone are PII even when stored alone
   - Account numbers and routing numbers are PCI
   - Always include the applicable regulations for each classification
   ```

1. The agent will auto-save the instructions.

   > **Important**: You will add pipeline hand-off instructions later in Challenge 3 and Challenge 4 when you connect the other agents.

### Task 4: Configure Agent Description

1. Expand the **Agent Description** section.

1. Add a description:

   ```
   Analyzes database schemas and sample data to classify every column into sensitivity categories (PII, PHI, PCI, Confidential, Public). Returns structured JSON with confidence scores, applicable regulations, and recommended security controls.
   ```

### Task 5: Test with Customer Data

1. Click the **Try in playground** button in the top right.

1. In the chat interface, paste the following customer data schema and sample rows:

   ```
   Classify the following data asset:

   Database: RetailDB
   Table: Customers
   Total Rows: 48500

   Schema:
   - CustomerID (INT): Unique customer identifier
   - FirstName (VARCHAR): Customer first name
   - LastName (VARCHAR): Customer last name
   - SSN (VARCHAR): Social Security Number
   - Email (VARCHAR): Email address
   - Phone (VARCHAR): Phone number
   - CreditCardNumber (VARCHAR): Credit card number
   - CVV (VARCHAR): Card security code
   - CardExpiry (VARCHAR): Card expiration date
   - Address (VARCHAR): Street address
   - City (VARCHAR): City
   - State (VARCHAR): State
   - ZipCode (VARCHAR): ZIP code
   - DateOfBirth (DATE): Date of birth
   - AccountStatus (VARCHAR): Account status
   - CreatedDate (DATETIME): Record creation date
   - Notes (TEXT): Free-text notes

   Sample Rows (5):
   1. CustomerID: 1001, FirstName: John, LastName: Smith, SSN: 123-45-6789, Email: john.smith@email.com, Phone: 555-0101, CreditCardNumber: 4532-1234-5678-9012, CVV: 847, CardExpiry: 12/2027, DateOfBirth: 1985-03-15, Notes: "Customer mentioned SSN issue with account 987-65-4321"
   2. CustomerID: 1002, FirstName: Maria, LastName: Garcia, SSN: 234-56-7890, Email: m.garcia@company.org, Phone: 555-0102, CreditCardNumber: 5412-7534-9821-0063, CVV: 312, CardExpiry: 08/2026, DateOfBirth: 1990-07-22, Notes: "Preferred customer, birthday discount applied"
   3. CustomerID: 1003, FirstName: Robert, LastName: Chen, SSN: 345-67-8901, Email: rchen@webmail.net, Phone: 555-0103, CreditCardNumber: 4916-3389-7712-4455, CVV: 556, CardExpiry: 03/2028, DateOfBirth: 1978-11-30, Notes: "Address change pending verification"
   4. CustomerID: 1004, FirstName: Sarah, LastName: Johnson, SSN: 456-78-9012, Phone: 555-0104, CreditCardNumber: 5534-2210-8876-3341, CVV: 229, CardExpiry: 11/2025, DateOfBirth: 1995-01-08, Notes: "Called about unauthorized charge on card ending 3341"
   5. CustomerID: 1005, FirstName: James, LastName: Williams, SSN: 567-89-0123, Email: jwilliams@email.com, Phone: 555-0105, CreditCardNumber: 4024-0071-8856-6677, CVV: 441, CardExpiry: 06/2027, DateOfBirth: 1982-09-14, Notes: "Account flagged for review"
   ```

1. Send the message and wait for the response.

1. Verify that the agent returns a structured JSON classification with:
   - SSN classified as **PII** with GDPR regulation
   - CreditCardNumber classified as **PCI** with PCI-DSS
   - CVV classified as **PCI**
   - Email, Phone, DateOfBirth classified as **PII**
   - Notes classified as **PII** (contains embedded SSN in sample data)
   - AccountStatus and CreatedDate classified as **PUBLIC**

### Task 6: Test with Medical Records

1. In the same playground, paste this medical record data:

   ```
   Classify the following data asset:

   Database: HealthcareDB
   Table: MedicalRecords
   Total Rows: 32000

   Schema:
   - RecordID (INT): Unique record identifier
   - PatientName (VARCHAR): Patient full name
   - SSN (VARCHAR): Social Security Number
   - DateOfBirth (DATE): Patient date of birth
   - InsuranceID (VARCHAR): Insurance policy number
   - PrimaryDiagnosis (VARCHAR): Primary diagnosis
   - DiagnosisCode (VARCHAR): ICD-10 code
   - Treatment (VARCHAR): Treatment plan
   - Medications (VARCHAR): Prescribed medications
   - LabResults (TEXT): Laboratory test results
   - AttendingPhysician (VARCHAR): Doctor name
   - FacilityName (VARCHAR): Hospital/clinic name
   - AdmissionDate (DATE): Date of admission
   - DischargeDate (DATE): Date of discharge
   - Notes (TEXT): Clinical notes
   - LastUpdated (DATETIME): Last modified timestamp

   Sample Rows (3):
   1. RecordID: 5001, PatientName: Alice Thompson, SSN: 111-22-3333, InsuranceID: INS-44820, PrimaryDiagnosis: Type 2 Diabetes Mellitus, DiagnosisCode: E11.9, Treatment: Insulin therapy, Medications: Metformin 500mg, LabResults: HbA1c 8.2%, Notes: "Patient reports non-compliance with diet. Referred to nutritionist. Family history of cardiac disease."
   2. RecordID: 5002, PatientName: Michael Rivera, SSN: 222-33-4444, InsuranceID: INS-57391, PrimaryDiagnosis: Major Depressive Disorder, DiagnosisCode: F33.1, Treatment: CBT and pharmacotherapy, Medications: Sertraline 100mg, LabResults: Normal CBC, Notes: "Patient expressed suicidal ideation during session. Safety plan established. Emergency contact: wife Maria 555-0199."
   3. RecordID: 5003, PatientName: Jennifer Park, SSN: 333-44-5555, InsuranceID: INS-63102, PrimaryDiagnosis: Breast Cancer Stage II, DiagnosisCode: C50.9, Treatment: Chemotherapy + radiation, Medications: Tamoxifen 20mg, LabResults: CA 15-3 elevated at 45 U/mL, Notes: "Genetic test positive for BRCA1 mutation. Daughter recommended for genetic counseling."
   ```

1. Verify the agent classifies:
   - PatientName, SSN, DateOfBirth as **PII**
   - InsuranceID, PrimaryDiagnosis, DiagnosisCode, Treatment, Medications, LabResults as **PHI**
   - Notes as **PHI** (contains clinical observations, emergency contacts, genetic info)
   - HIPAA listed as applicable regulation for PHI columns

### Task 7: Save and Note the Agent ID

1. The agent auto-saves as you make changes.

1. In the **Setup** panel on the right, locate the **Agent ID** field.

1. Copy the **Agent ID** (e.g., `asst_xxxxxxxxxxxxx`).

1. Save this ID in Notepad — you will need it in Challenge 5 for the Streamlit app.

## Success Criteria

- Data Classification Agent created with the correct model deployment
- Agent instructions cover all five classification categories (PII, PHI, PCI, Confidential, Public)
- Agent returns structured JSON output with classification, confidence, reasons, and regulations
- Customer data test correctly identifies PII and PCI columns
- Medical records test correctly identifies PHI columns
- Notes fields are classified based on sample data content (not just column name)
- Agent ID documented for later use

## Additional Resources

- [GDPR Data Classification](https://learn.microsoft.com/compliance/regulatory/gdpr)
- [HIPAA Protected Health Information](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html)
- [PCI DSS Requirements](https://www.pcisecuritystandards.org/)
- [Azure AI Agents](https://learn.microsoft.com/azure/ai-studio/how-to/develop/agents)

Now, click **Next** to continue to **Challenge 03**.
