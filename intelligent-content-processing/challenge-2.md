# Challenge 02: Multi-Modal Understanding with Microsoft Foundry

## Introduction

In this challenge, participants will enhance the OCR results generated in Challenge 01 by applying **multi-modal AI understanding**.
While OCR extracts raw text, it does not understand **meaning, context, or intent**.
Using **Microsoft Foundry (gpt-4o-mini)**, participants will convert unstructured OCR text and images into **structured, meaningful JSON data**.

## Challenge Objectives

* Create an **Microsoft Foundry** resource.
* Deploy the **gpt-4o-mini** model for multi-modal document understanding.
* Use GPT to extract structured data from OCR text (PDF documents).
* Use GPT Vision to understand handwritten image documents.
* Generate clean, valid JSON output suitable for automation.


## Steps to Complete

### Create Microsoft Foundry Resource

1. In the **Azure Portal**, search for **Microsoft Foundry**, from the left under **Use with Foundry**, select **Foundry** and click **Create**.

1. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   * **Region**: **<inject key="Region"></inject>**
   * **Name:** **openai-doc-ai-<inject key="DeploymentID" enableCopy="false"/>**
   * **Pricing Tier:** Standard

1. Click **Review + Create** → **Create**.

1. After deployment succeeds, open the **Microsoft Foundry** resource.

### Deploy the GPT Model

1. In the Microsoft Foundry resource, click **Go to Microsoft Foundry Studio**.

1. Navigate to **Deployments** → **Create deployment**.

1. Provide:

   * **Model:** `gpt-4o-mini`
   * **Deployment name:** `gpt-4o-mini`
   * **Deployment type:** `Standard`
   * **Version:** Default / Latest

1. Click **Deploy** and wait for deployment to complete.

### Extract Structured Data from OCR Text (PDF Flow)

1. In **Microsoft Foundry Studio**, go to **Chat playground**.

1. Select the deployment:

    * **Model:** `gpt-4o-mini`
    * **Give the model instructions and context:** 
    
      ```
      You are an AI assistant specialized in enterprise document processing.

      You understand OCR text from PDFs and scanned documents.
      Your role is to extract structured, machine-readable data from unstructured text.

      Always follow these rules:
      - Identify the document type correctly
      - Extract only the information present in the text
      - Normalize dates and numeric values
      - Return valid JSON only
      - Do not include explanations, markdown, or extra text
      ```

1. Select **Apply changes** → **Continue**

2. Paste the **OCR text** extracted in Challenge 01 from `invoice.pdf`.

1. Use the following prompt:

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

1. Click **Submit**.

### Extract Structured Data from Image (Handwritten Note Flow)

1. In the **Chat playground**, click **Add image**.

1. Update the **Give the model instructions and context:** 

    ```
    You are an AI assistant specialized in enterprise document processing.

    You can understand scanned and handwritten documents from images.
    Your role is to extract structured, machine-readable data from unstructured content.

    Always follow these rules:
    - Identify the document type correctly
    - Interpret handwritten text and fix recognition errors
    - Extract only information present in the document
    - Normalize values where possible
    - Return valid JSON only
    - Do not include explanations, markdown, or extra text
    ```

1. Select **Apply changes** → **Continue**

1. Upload `handwritten_note.jpg`.

1. Use the following prompt:

    ```
    You are an AI assistant that understands handwritten documents.

    Identify:
    - Document type
    - Person name
    - Summary
    - Action required

    Return VALID JSON only.
    ```

1. Click **Submit**.

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
  "documentType": "Patient Note",
  "personName": "John Doe",
  "summary": "Patient prescribed medication for 5 days",
  "actionRequired": "Follow-up required"
}
```

<validation step="d8239636-15d6-4f78-b064-786b79917066" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Success Criteria

You have successfully completed the Challenge 2:

* Microsoft Foundry resource is created
* `gpt-4o-mini` deployment is active
* Structured JSON is generated from OCR text
* GPT correctly understands handwritten image content

### Additional Resources

- [Microsoft Foundry Service – Overview](https://learn.microsoft.com/azure/ai-services/openai/overview)

- [Microsoft Foundry Studio – Getting Started](https://learn.microsoft.com/azure/ai-services/openai/how-to/use-azure-openai-studio)

- [GPT-4o and GPT-4o-mini Models](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4o-and-gpt-4o-mini)

- [Vision-Capable Models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/concepts/vision)

- [Prompt Engineering Best Practices (JSON & Structured Output)](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)

Now, click **Next** to continue to **Challenge 03**.