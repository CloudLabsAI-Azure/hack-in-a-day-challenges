# Challenge 03: Schema-Based JSON Mapping & Confidence Scoring

## Introduction

In the previous challenge, participants used AI to extract structured information from documents.
However, AI outputs can vary across document types and prompts.
In this challenge, participants will **standardize AI output into a fixed JSON schema** and **add confidence scoring**, making the data reliable, auditable, and ready for enterprise automation.

## Challenge Objectives

* Define a **standard JSON schema** applicable to all document types.
* Normalize AI-generated outputs into the defined schema.
* Add a **confidence score** to measure AI reliability.
* Assign an initial **processing status** to each document.
* Prepare data for downstream storage and human validation.

## Steps to Complete

### Define a Standard JSON Schema

1. Create a new JSON file locally or in your editor.

2. Define the following schema (use this exactly):

    ```json
    {
    "id": "string",
    "documentType": "string",
    "referenceId": "string",
    "amount": "number",
    "currency": "string",
    "confidence": "number",
    "status": "string"
    }
    ```

3. Save the file as `document-schema.json`.

### Map Invoice AI Output to the Schema

4. Take the JSON output generated in **Challenge 02** for `invoice.pdf`.

5. Map the fields as follows:

   * `invoiceNumber` → `referenceId`
   * `totalAmount` → `amount`
   * Set `confidence` to a value between `0.0 – 1.0`
   * Set `status` to `PENDING`
   * `document_type` to `documentType`
   * `currency` to `currency`
   * Set `id` to `doc-001`

6. Example mapped output:

    ```json
    {
    "id": "doc-001",
    "documentType": "Invoice",
    "referenceId": "INV-1001",
    "amount": 1250,
    "currency": "USD",
    "confidence": 0.92,
    "status": "PENDING"
    }
    ```

### Map Handwritten Note AI Output to the Schema

7. Take the JSON output generated in **Challenge 02** for `handwritten_note.jpg`, and add it in the same `json`file.

8. Map the fields as follows:

   * `personName` → `referenceId`
   * Set `amount` to `0`
   * Leave `currency` empty
   * Assign a lower confidence if OCR quality was poor

9. Example mapped output:

    ```json
    {
    "id": "doc-002",
    "documentType": "Patient Note",
    "referenceId": "John Doe",
    "amount": 0,
    "currency": "",
    "confidence": 0.78,
    "status": "PENDING"
    }
    ```

10. Save the `json` file.

### Add Confidence Scoring Logic

11. Apply the following simple rule:

* Confidence ≥ `0.85` → Eligible for auto-approval
* Confidence < `0.85` → Requires human review

12. Keep all documents in `PENDING` state for now (approval happens in the next challenge).

### Success Criteria

You have successfully completed the Challenge 3:

* A single JSON schema is defined and reused
* Both document types conform to the same schema
* Confidence values are assigned realistically
* JSON output is valid and consistent

### Additional Resources

- [Designing JSON Schemas (General Guidance)](https://learn.microsoft.com/azure/architecture/best-practices/api-design#json-design)

- [Best Practices for Structured Data in APIs](https://learn.microsoft.com/azure/architecture/best-practices/api-design)

- [Azure OpenAI – Structured Output & Prompt Engineering](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)

- [Handling AI Confidence & Reliability (Azure AI Guidance)](https://learn.microsoft.com/azure/architecture/guide/ai/trustworthy-ai)

Now, click **Next** to continue to **Challenge 04**.
