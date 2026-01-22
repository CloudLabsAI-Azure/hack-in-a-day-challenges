# Challenge 02: Multi-Modal Understanding with Azure OpenAI

## Introduction

In this challenge, participants will enhance the OCR results generated in Challenge 01 by applying **multi-modal AI understanding**.
While OCR extracts raw text, it does not understand **meaning, context, or intent**.
Using **Azure OpenAI (gpt-4o-mini)**, participants will convert unstructured OCR text and images into **structured, meaningful JSON data**.

## Challenge Objectives

* Create an **Azure OpenAI** resource.
* Deploy the **gpt-4o-mini** model for multi-modal document understanding.
* Use GPT to extract structured data from OCR text (PDF documents).
* Use GPT Vision to understand handwritten image documents.
* Generate clean, valid JSON output suitable for automation.


## Steps to Complete

### Create Azure OpenAI Resource

1. In the **Azure Portal**, search for **Azure OpenAI** and click **Create**.

2. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** Select `challenge-rg-<inject key="DeploymentID" enableCopy="false"/>`
   * **Region:** Choose a supported Azure OpenAI region
   * **Name:** `openai-doc-ai-<inject key="DeploymentID" enableCopy="false"/>`
   * **Pricing Tier:** Standard

3. Click **Review + Create** → **Create**.

4. After deployment succeeds, open the **Azure OpenAI** resource.

### Deploy the GPT Model

5. In the Azure OpenAI resource, click **Go to Azure OpenAI Studio**.

6. Navigate to **Deployments** → **Create deployment**.

7. Provide:

   * **Model:** `gpt-4o-mini`
   * **Deployment name:** `gpt-4o-mini`
   * **Version:** Default / Latest
   * **Capacity:** Default

8. Click **Create** and wait for deployment to complete.

### Extract Structured Data from OCR Text (PDF Flow)

9. In **Azure OpenAI Studio**, go to **Chat playground**.

10. Select the deployment:

    * **Model:** `gpt-4o-mini`

11. Paste the **OCR text** extracted in Challenge 01 from `invoice.pdf`.

12. Use the following prompt:

    ```
    You are an AI assistant that extracts structured information from documents.

    Identify:
    - Document type
    - Invoice number
    - Vendor
    - Date
    - Total amount
    - Currency

    Return VALID JSON only.

    OCR TEXT:
    <Paste OCR text here>
    ```

13. Click **Submit**.

---

### Extract Structured Data from Image (Handwritten Note Flow)

14. In the **Chat playground**, click **Add image**.

15. Upload `handwritten_note.jpg`.

16. Use the following prompt:

    ```
    You are an AI assistant that understands handwritten documents.

    Identify:
    - Document type
    - Person name
    - Summary
    - Action required

    Return VALID JSON only.
    ```

17. Click **Submit**.

## Expected Outputs

### Invoice Output

```json
{
  "documentType": "Invoice",
  "invoiceNumber": "INV-1001",
  "vendor": "ABC Corporation",
  "date": "2026-01-21",
  "totalAmount": 1250,
  "currency": "USD"
}
```

### Handwritten Note Output

```json
{
  "documentType": "HandwrittenNote",
  "personName": "John Doe",
  "summary": "Patient prescribed medication for five days",
  "actionRequired": "Follow-up required"
}
```

### Success Criteria

You have successfully completed the Challenge 2:

* Azure OpenAI resource is created
* `gpt-4o-mini` deployment is active
* Structured JSON is generated from OCR text
* GPT correctly understands handwritten image content

### Additional Resources

- [Azure OpenAI Service – Overview](https://learn.microsoft.com/azure/ai-services/openai/overview)

- [Azure OpenAI Studio – Getting Started](https://learn.microsoft.com/azure/ai-services/openai/how-to/use-azure-openai-studio)

- [GPT-4o and GPT-4o-mini Models](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4o-and-gpt-4o-mini)

- [Vision-Capable Models in Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/vision)

- [Prompt Engineering Best Practices (JSON & Structured Output)](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)

Now, click **Next** to continue to **Challenge 03**.