# Challenge 2: Build the Document Classification Agent

## Introduction

Now that your infrastructure is in place, it's time to build the first piece of your AI pipeline — the **Document Classification Agent**. This agent receives raw OCR text from Document Intelligence and determines what type of document it is: invoice, receipt, medical form, insurance claim, or identity document.

Getting classification right is critical because it determines which extraction rules apply downstream. An invoice needs vendor names and line items; a medical form needs patient details and diagnoses. The classification agent is the brain that makes the rest of the pipeline work.

## Challenge Objectives

- Create a Document Classification Agent in Azure AI Foundry
- Configure comprehensive classification instructions covering all 5 document types
- Test the agent in the Foundry playground with sample OCR text
- Verify the agent returns structured JSON with document type, confidence, and key indicators

## Steps to Complete

### Part 1: Navigate to AI Foundry Agents

1. Go to [Azure AI Foundry](https://ai.azure.com) and open your project **proj-default** (under the Foundry resource **content-hub-<inject key="DeploymentID" enableCopy="false"/>**).

1. In the left navigation menu, click **Agents**.

1. Click **+ New Agent** to create your first agent.

### Part 2: Configure the Classification Agent

1. Set the **Agent name** to:

   ```
   Document-Classification-Agent
   ```

1. Under **Model**, select the **doc-processor** deployment (GPT-4.1) you created in Challenge 1.

1. In the **Instructions** field, copy the entire block below (from **===START INSTRUCTIONS===** to **===END INSTRUCTIONS===**) and paste it into the Instructions box. Do **NOT** include the START/END marker lines themselves:

   **===START INSTRUCTIONS===**

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

   **===END INSTRUCTIONS===**

1. Click **Save** to save the agent.

1. Note the **Agent ID** displayed in the Setup panel (starts with `asst_`). You'll need this later.

### Part 3: Test the Classification Agent in the Playground

1. In the agent's page, you should see the **Playground** / chat panel on the right.

1. **Test 1: Invoice classification.** Paste the following simulated OCR text (this represents what Document Intelligence would extract from `invoice_contoso.pdf`):

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

   Ship To:
   Northwind Traders - Warehouse
   789 Industrial Blvd
   Portland, OR 97203

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

1. Verify the agent returns a JSON response with:
   - `"document_type": "INVOICE"`
   - Confidence of 0.90 or higher
   - A meaningful summary
   - Relevant key indicators

1. **Test 2: Receipt classification.** Clear the chat and paste:

   ```
   URBAN GROUNDS CAFÉ
   342 Main Street, Seattle WA
   Tel: (206) 555-0147

   Date: 01/15/2025  Time: 08:42 AM
   Register: 03  Cashier: Maria

   --------------------------------
   Cappuccino Grande       $5.50
   Blueberry Muffin        $3.75
   Avocado Toast           $8.95
   Orange Juice Fresh      $4.25
   --------------------------------
   Subtotal               $22.45
   Tax (10.1%)             $2.27
   --------------------------------
   TOTAL                  $24.72

   VISA ***4582
   Auth: 847291

   Thank you for visiting!
   Rewards Points Earned: 25
   ```

1. Verify the agent returns `"document_type": "RECEIPT"` with high confidence.

1. **Test 3: Identity Document classification.** Clear the chat and paste:

   ```
   WASHINGTON STATE
   DRIVER LICENSE

   DL: SMITHJ*456*RQ
   CLASS: C

   SMITH, JOHN MICHAEL
   1234 ELM STREET
   SEATTLE WA 98101

   DOB: 03/15/1985
   ISS: 06/01/2023
   EXP: 03/15/2031

   SEX: M  HT: 5-11  WGT: 180
   EYES: BRN  HAIR: BLK

   DONOR: YES
   RESTRICTIONS: CORRECTIVE LENSES
   ```

1. Verify `"document_type": "IDENTITY_DOCUMENT"` with high confidence.

1. **Test 4: Ambiguous/Edge case.** Clear the chat and paste:

   ```
   DOCUMENT RECEIVED
   Date: 2025-01-20
   Pages: 3
   Quality: Poor scan

   [Large portions of text are illegible]

   ...payment of $500...
   ...reference number 12345...
   ...signed by representative...
   ```

1. This should return a lower confidence score (below 0.85), showing the agent handles ambiguity correctly.

<validation step="9e5f7a8b-2c3d-4e0f-1a2b-6c7d8e9f0a1b" />

> **Congratulations!** Your Document Classification Agent is built and tested.
>
> If validation fails, verify:
> - The agent name is exactly `Document-Classification-Agent`
> - The agent uses the `doc-processor` model deployment
> - The agent returns valid JSON with document_type, confidence, summary, and key_indicators

## Success Criteria

- [ ] `Document-Classification-Agent` is created in your AI Foundry project
- [ ] Agent correctly classifies an invoice with confidence ≥ 0.90
- [ ] Agent correctly classifies a receipt with confidence ≥ 0.90
- [ ] Agent correctly classifies an identity document with confidence ≥ 0.85
- [ ] Agent returns lower confidence (< 0.85) for ambiguous text
- [ ] All responses are valid JSON in the specified format

## Additional Resources

- [Azure AI Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/agents)
- [Prompt Engineering Best Practices](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)

Click **Next** to continue to **Challenge 3: Build Extraction & Validation Agents + Connect Pipeline**.
