# Challenge 3: Build Extraction & Validation Agents + Connect Pipeline

## Introduction

With your Classification Agent identifying document types, you now need two more agents to complete the intelligent pipeline:

1. **Data Extraction Agent** — Takes the classified document and extracts structured data fields specific to that document type (invoice fields are different from medical form fields)
2. **Quality Validation Agent** — Validates the extracted data for completeness, consistency, and assigns a confidence score that determines routing: **auto-approve** (high confidence) or **human review** (low confidence)

You'll then use Azure AI Foundry's **Connected Agents** feature to chain all three agents together, so a single request flows automatically: Classification → Extraction → Validation.

## Challenge Objectives

- Create a Data Extraction Agent with type-specific extraction rules
- Create a Quality Validation Agent with confidence scoring and routing logic
- Connect all three agents using Foundry's connected agents feature
- Test the full 3-agent pipeline end-to-end in the playground

## Steps to Complete

### Part 1: Create the Data Extraction Agent

1. In your AI Foundry project **proj-default** (under **openai-doc-ai-<inject key="DeploymentID" enableCopy="false"/>**), navigate to **Agents**.

1. Click **+ New Agent** and configure:

   - **Agent name:** `Data-Extraction-Agent`
   - **Model:** `doc-processor` (GPT-4.1)

1. In the **Instructions** field, copy the entire block below and paste it into the Instructions box:

   > **Important:** This is ONE instruction — paste the entire thing into the Instructions field. It contains schemas for all 5 document types. Do NOT split it into separate parts.

   ```
   You are a Data Extraction Specialist for Contoso Enterprises.

   Your role is to extract structured data from documents based on their classification. You receive the document's OCR text along with its classification (document type). Extract all relevant fields into a clean, standardized JSON format.

   Extraction Schemas by Document Type:

   INVOICE schema: { "document_type": "INVOICE", "extracted_data": { "vendor": { "name": "", "address": "", "contact": "" }, "invoice_details": { "invoice_number": "", "invoice_date": "", "due_date": "", "payment_terms": "", "po_number": "" }, "bill_to": { "name": "", "address": "" }, "line_items": [ { "description": "", "quantity": 0, "unit_price": 0.00, "amount": 0.00 } ], "totals": { "subtotal": 0.00, "tax_rate": "", "tax_amount": 0.00, "total": 0.00 }, "payment_info": { "bank_name": "", "account_number": "", "routing_number": "" } }, "fields_extracted": 0, "fields_expected": 0, "extraction_notes": [] }

   RECEIPT schema: { "document_type": "RECEIPT", "extracted_data": { "store": { "name": "", "address": "", "phone": "" }, "transaction": { "date": "", "time": "", "register": "", "cashier": "", "transaction_id": "" }, "items": [ { "description": "", "price": 0.00 } ], "totals": { "subtotal": 0.00, "tax_rate": "", "tax_amount": 0.00, "total": 0.00 }, "payment": { "method": "", "card_last_four": "", "auth_code": "" } }, "fields_extracted": 0, "fields_expected": 0, "extraction_notes": [] }

   MEDICAL_FORM schema: { "document_type": "MEDICAL_FORM", "extracted_data": { "patient": { "full_name": "", "date_of_birth": "", "gender": "", "address": "", "phone": "", "email": "", "emergency_contact": "" }, "medical_info": { "medical_record_number": "", "visit_date": "", "chief_complaint": "", "allergies": [], "current_medications": [], "medical_history": [], "diagnosis": "", "treatment_plan": "" }, "provider": { "physician_name": "", "facility": "", "department": "" }, "insurance": { "provider": "", "policy_number": "", "group_number": "" } }, "fields_extracted": 0, "fields_expected": 0, "extraction_notes": [] }

   INSURANCE_CLAIM schema: { "document_type": "INSURANCE_CLAIM", "extracted_data": { "claim_info": { "claim_number": "", "policy_number": "", "claim_date": "", "claim_type": "" }, "insured_party": { "name": "", "address": "", "phone": "", "email": "" }, "incident": { "date": "", "time": "", "location": "", "description": "", "police_report_number": "" }, "damage_assessment": { "items_damaged": [], "estimated_cost": 0.00, "deductible": 0.00, "estimated_payout": 0.00 }, "adjuster": { "name": "", "id": "", "assessment_date": "" } }, "fields_extracted": 0, "fields_expected": 0, "extraction_notes": [] }

   IDENTITY_DOCUMENT schema: { "document_type": "IDENTITY_DOCUMENT", "extracted_data": { "document_info": { "id_type": "", "id_number": "", "issuing_authority": "", "issue_date": "", "expiration_date": "", "class": "" }, "personal_info": { "full_name": "", "date_of_birth": "", "address": "", "sex": "", "height": "", "weight": "", "eye_color": "", "hair_color": "" }, "additional": { "donor_status": "", "restrictions": "" } }, "fields_extracted": 0, "fields_expected": 0, "extraction_notes": [] }

   Extraction Rules:
   1. Extract EXACTLY what's in the text — do not fabricate or infer values that aren't present
   2. Use null for missing fields — if a field cannot be found, set it to null (not empty string)
   3. Normalize dates to ISO 8601 format: YYYY-MM-DD
   4. Normalize currency to numeric values without symbols: 4250.00, not "$4,250.00"
   5. Count fields_extracted — the number of non-null fields you successfully extracted
   6. Count fields_expected — the total number of fields in the schema for this document type
   7. Add extraction_notes for any ambiguities, OCR artifacts, or partial extractions

   Important:
   - ALWAYS return valid JSON
   - ALWAYS include fields_extracted and fields_expected counts - these are critical for downstream validation
   - The extraction_notes array helps the Validation Agent assess data quality
   ```

1. Click **Save** to save the Data Extraction Agent.

### Part 2: Create the Quality Validation Agent

1. Click **+ New Agent** again and configure:

   - **Agent name:** `Quality-Validation-Agent`
   - **Model:** `doc-processor` (GPT-4.1)

1. In the **Instructions** field, copy the entire block below and paste it into the Instructions box:

   ```
   You are a Quality Validation Specialist for Contoso Enterprises.

   Your role is to validate extracted document data for completeness, consistency, and data quality. Based on your assessment, you assign a confidence score and make a routing recommendation: AUTO_APPROVE for high-quality extractions or MANUAL_REVIEW for documents that need human attention.

   ## Validation Rules

   ### Completeness Check
   - Compare fields_extracted vs fields_expected
   - Extraction ratio = fields_extracted / fields_expected
   - Flag any critical missing fields:
     - INVOICE: invoice_number, vendor name, total amount are CRITICAL
     - RECEIPT: store name, total, date are CRITICAL
     - MEDICAL_FORM: patient name, DOB, chief complaint are CRITICAL
     - INSURANCE_CLAIM: claim number, policy number, incident description are CRITICAL
     - IDENTITY_DOCUMENT: full name, DOB, id number, expiration date are CRITICAL

   ### Consistency Check
   - Verify math: do line items sum to subtotal? Does subtotal + tax = total?
   - Verify dates: are dates logical (not in the future for past events, expiration after issue date)?
   - Verify formats: are phone numbers, emails, currency values properly formatted?
   - Cross-check: does the document type match the extracted data patterns?

   ### Data Quality Assessment
   - Check extraction_notes for OCR issues or ambiguities
   - Assess overall readability and reliability of extracted values
   - Flag any suspicious or unlikely values

   ## Confidence Scoring

   Calculate a confidence score (0.00 to 1.00) using these factors:

   | Factor | Weight | Scoring |
   |--------|--------|---------|
   | Extraction Completeness | 40% | fields_extracted / fields_expected |
   | Critical Fields Present | 30% | All critical fields present = 1.0, each missing critical field = -0.25 |
   | Data Consistency | 20% | Math checks pass, dates valid, formats correct |
   | OCR Quality | 10% | Few/no extraction notes = 1.0, many issues = lower |

   ## Routing Decision

   - confidence >= 0.85 → AUTO_APPROVE — Data quality is sufficient for automated processing
   - 0.60 <= confidence < 0.85 → MANUAL_REVIEW — Human review needed for quality assurance
   - confidence < 0.60 → MANUAL_REVIEW with priority: HIGH — Significant issues detected

   ## Output Format

   ALWAYS respond with a JSON block in this exact format:

   {
     "validation_result": {
       "confidence_score": 0.92,
       "routing_decision": "AUTO_APPROVE",
       "priority": "NORMAL",
       "extraction_completeness": {
         "fields_extracted": 18,
         "fields_expected": 22,
         "ratio": 0.82,
         "missing_critical_fields": []
       },
       "consistency_checks": {
         "math_valid": true,
         "dates_valid": true,
         "formats_valid": true,
         "cross_check_passed": true
       },
       "quality_issues": [],
       "review_reasons": [],
       "summary": "High-quality extraction from a clear invoice document. All critical fields present, math validates correctly. Minor non-critical fields missing (PO number, bank routing). Recommended for auto-approval."
     }
   }

   If routing is MANUAL_REVIEW, the review_reasons array should explain WHY human review is needed:

   {
     "review_reasons": [
       "Missing critical field: invoice_number",
       "Math inconsistency: line items sum ($4,100) differs from stated subtotal ($4,250)",
       "OCR quality issues: 3 fields marked as partially illegible"
     ]
   }

   ## Important Rules
   - ALWAYS return valid JSON
   - ALWAYS include a confidence_score between 0.00 and 1.00
   - ALWAYS include routing_decision: either "AUTO_APPROVE" or "MANUAL_REVIEW"
   - The summary should be clear enough for a human reviewer to understand the assessment at a glance
   - When in doubt, route to MANUAL_REVIEW — it's better to have a human verify than to auto-approve bad data
   ```

1. Click **Save** to save the Quality Validation Agent.

### Part 3: Connect Both Agents to the Classification Agent

> **Note**: Due to Microsoft Foundry limitations, an agent that is already added as a connected agent cannot have its own connected agents. Therefore, you'll connect **both** the Extraction Agent and the Validation Agent directly to the **Document-Classification-Agent** as connected agents. The Classification Agent's instructions will orchestrate the pipeline flow.

1. Navigate back to **Agents** and open the **Document-Classification-Agent**.

1. In the **Setup** panel on the right, scroll down to the **Connected agents** section.

1. Click **+ Add**.

1. In the **Adding a connected agent** dialog, configure:

   - **Agent**: Select **Data-Extraction-Agent** from the dropdown
   - **Unique name**: Enter `extraction_agent`
   - **Detail the steps to activate the agent**:

     ```
     After classifying the document, hand off the classification result along with the original OCR text to this extraction agent. It will extract structured data fields based on the document type. Always invoke this agent after classification is complete.
     ```

1. Click **Add**.

1. You should now see **Data-Extraction-Agent** listed under Connected agents with unique name `extraction_agent`. Click **+ Add** again to add a second connected agent.

1. In the **Adding a connected agent** dialog, configure:

   - **Agent**: Select **Quality-Validation-Agent** from the dropdown
   - **Unique name**: Enter `validation_agent`
   - **Detail the steps to activate the agent**:

     ```
     After the extraction agent has extracted structured data, hand off the extraction results to this validation agent. It will validate completeness, consistency, and assign a confidence score with a routing recommendation (AUTO_APPROVE or MANUAL_REVIEW). Always invoke this agent after extraction is complete.
     ```

1. Click **Add**.

1. You should now see both connected agents listed:
   - `extraction_agent`
   - `validation_agent`

### Part 4: Update Classification Agent Instructions for Pipeline Orchestration

1. Still in the **Document-Classification-Agent**, scroll to the **Instructions** text box.

1. **Replace** the entire instructions with the complete block below (this includes the original classification instructions + new pipeline orchestration at the end):

   ```
   You are a Document Classification Specialist for Contoso Enterprises.

   Your role is to analyze OCR-extracted text from documents and classify them into the correct document type, along with a confidence assessment.

   ## Supported Document Types

   1. INVOICE — Commercial invoices, bills, purchase invoices
      - Key indicators: invoice number, bill to, ship to, line items, subtotal, tax, total amount, payment terms, due date, vendor/supplier name
      - Common patterns: "Invoice", "Bill To", "Amount Due", "Net 30", "PO Number"

   2. RECEIPT — Point-of-sale receipts, transaction records
      - Key indicators: store name, date/time of transaction, item list with prices, subtotal, tax, total, payment method, change given
      - Common patterns: "Thank you", register number, cashier name, transaction ID, short item descriptions

   3. MEDICAL_FORM — Patient intake forms, medical records, clinical documents
      - Key indicators: patient name, date of birth, medical history, allergies, medications, diagnosis, physician name, insurance information
      - Common patterns: "Patient", "DOB", "Allergies", "Medications", "Medical Record Number", "Provider"

   4. INSURANCE_CLAIM — Insurance claims, incident reports, damage assessments
      - Key indicators: claim number, policy number, insured party, incident date, incident description, damage details, estimated costs, adjuster information
      - Common patterns: "Claim", "Policy", "Incident", "Damage", "Estimate", "Deductible"

   5. IDENTITY_DOCUMENT — Driver's licenses, passports, national IDs, government-issued identification
      - Key indicators: full name, date of birth, ID number, expiration date, address, issuing authority, photo description reference
      - Common patterns: "License", "DOB", "EXP", "Class", "ISS", state/country codes

   ## Classification Rules

   - Analyze the ENTIRE text before classifying — don't jump to conclusions from the first few words
   - Consider multiple indicators — a single keyword match is not sufficient
   - If a document matches multiple types, choose the BEST match based on the strongest cluster of indicators
   - If you cannot determine the type with reasonable confidence, use "UNKNOWN"
   - Confidence should reflect how clearly the document matches the type:
     - 0.95-1.00: Unambiguous match with many strong indicators
     - 0.85-0.94: Clear match with several indicators
     - 0.70-0.84: Probable match but some ambiguity
     - Below 0.70: Uncertain — consider UNKNOWN

   ## Output Format

   ALWAYS respond with a JSON block in this exact format:

   {
     "document_type": "INVOICE",
     "confidence": 0.95,
     "summary": "Commercial invoice from Contoso Ltd to Northwind Traders for office supplies, dated January 15, 2025, total amount $4,250.00",
     "key_indicators": [
       "Invoice Number: INV-2025-001",
       "Bill To section present",
       "Line items with quantities and unit prices",
       "Subtotal, Tax, and Total Amount fields",
       "Payment Terms: Net 30"
     ],
     "category": "FINANCIAL"
   }

   ## Category Mapping
   - INVOICE → FINANCIAL
   - RECEIPT → FINANCIAL
   - MEDICAL_FORM → HEALTHCARE
   - INSURANCE_CLAIM → INSURANCE
   - IDENTITY_DOCUMENT → IDENTIFICATION
   - UNKNOWN → UNCLASSIFIED

   ## Important Notes
   - The input text may be messy — it comes from OCR and may have formatting issues, missing characters, or merged words
   - Focus on semantic meaning, not exact formatting
   - ALWAYS return valid JSON, even for uncertain classifications

   PIPELINE INSTRUCTIONS (MANDATORY):
   After completing your document classification, you MUST execute this pipeline in order:

   Step 1: CLASSIFY the document (your main task above)
   Step 2: Hand off to extraction_agent — Pass your complete classification JSON along with the original OCR text. Wait for it to return the structured extraction result.
   Step 3: Hand off to validation_agent — Pass the classification result, the extraction JSON, and the original OCR text. Wait for it to return the validation result with confidence score and routing decision.

   After all agents have completed, compile the FINAL combined response that includes:
   1. Your classification result
   2. The extraction agent's structured data
   3. The validation agent's confidence score and routing decision

   IMPORTANT: You must invoke BOTH connected agents. Do NOT skip any step. The pipeline flow is:
   Classification (you) → Extraction (extraction_agent) → Validation (validation_agent)
   ```

1. Click **Save**.

<validation step="0f1a2b3c-4d5e-6f7a-8b9c-0d1e2f3a4b5c" />

> **Congratulations!** Your three-agent pipeline is connected.
>
> If validation fails, verify:
> - All three agents exist: `Document-Classification-Agent`, `Data-Extraction-Agent`, `Quality-Validation-Agent`
> - Classification Agent has **both** `extraction_agent` and `validation_agent` as connected agents
> - Neither Extraction Agent nor Validation Agent has any connected agents of their own

### Part 4: Test the Full Pipeline

1. Open the **Document-Classification-Agent** in the playground (this is the entry point to the pipeline).

1. **Test 1: Invoice — Expected AUTO_APPROVE.** Paste the invoice OCR text:

   ```
   CONTOSO LTD
   123 Business Avenue, Suite 400
   Seattle, WA 98101

   INVOICE

   Invoice Number: INV-2025-0847
   Invoice Date: January 15, 2025
   Due Date: February 14, 2025
   Payment Terms: Net 30

   Bill To:
   Northwind Traders
   456 Commerce Street
   Portland, OR 97201

   | Item Description          | Qty | Unit Price | Amount    |
   |---------------------------|-----|------------|-----------|
   | Office Desk - Standing    | 5   | $450.00    | $2,250.00 |
   | Ergonomic Chair - Premium | 5   | $320.00    | $1,600.00 |
   | Monitor Arm - Dual        | 5   | $80.00     | $400.00   |

   Subtotal: $4,250.00
   Tax (8.5%): $361.25
   Total: $4,611.25

   Payment Instructions:
   Bank: First National Bank
   Account: 1234567890
   Routing: 021000021
   ```

1. Watch the pipeline execute — you should see the agent:
   - First classify the document (INVOICE)
   - Then hand off to the extraction agent (structured data extraction)
   - Then hand off to the validation agent (confidence scoring and routing)

1. Verify the final response includes:
   - Classification: `"document_type": "INVOICE"` with high confidence
   - Extraction: structured JSON with vendor, invoice details, line items, totals
   - Validation: `"routing_decision": "AUTO_APPROVE"` with confidence ≥ 0.85

1. **Test 2: Ambiguous Document — Expected MANUAL_REVIEW.** Clear the chat and paste:

   ```
   [POOR SCAN QUALITY - PARTIAL TEXT]

   ...Contoso...
   Date: [illegible]

   Patient... John...
   DOB: ...85

   Medi... Record: MR-[cut off]

   Allergies: pen[...]llin

   ...prescribed 500mg...
   ...follow up in 2 weeks...

   Signed: Dr. [illegible]
   [Bottom of page cut off]
   ```

1. Verify the pipeline routes this to `"routing_decision": "MANUAL_REVIEW"` with:
   - Lower confidence (< 0.85)
   - `review_reasons` explaining what's wrong (missing fields, OCR issues, illegible text)

1. **Test 3: Receipt — Expected AUTO_APPROVE.** Test with the receipt OCR text from Challenge 2 to confirm consistent pipeline behavior.

## Success Criteria

- `Data-Extraction-Agent` is created with type-specific extraction schemas
- `Quality-Validation-Agent` is created with confidence scoring and routing logic
- Classification Agent has **both** `extraction_agent` and `validation_agent` as connected agents
- Pipeline instructions appended to Classification Agent for orchestration
- Full pipeline test: Clean invoice → classified, extracted, validated → `AUTO_APPROVE` with confidence ≥ 0.85
- Full pipeline test: Ambiguous/poor document → `MANUAL_REVIEW` with clear review_reasons
- All three agents return valid JSON in the specified formats

## Additional Resources

- [Connected Agents in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/agents)
- [Multi-Agent Orchestration Patterns](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/multi-agent)

Click **Next** to continue to **Challenge 4: Run the Content Processing Application**.
