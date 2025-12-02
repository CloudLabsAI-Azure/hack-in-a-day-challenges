# Challenge 02: Extract Data Using the Prebuilt Invoice Model

## Introduction
Now that the Document Intelligence service is ready, Contoso Finance wants to test its **AI-powered invoice extraction**.  
Azure Document Intelligence provides **Prebuilt Models** trained on thousands of invoices.  
You can upload a PDF or image and instantly get structured output — including vendor name, invoice ID, dates, subtotals, and totals.

In this challenge, you’ll use the **Prebuilt Invoice Model** through the Azure Portal UI to extract data from a sample invoice.

## Challenge Objectives
- Access **Document Intelligence Studio** from the Azure Portal.  
- Use the **Prebuilt Invoice Model** to analyze sample documents.  
- View extracted fields and understand model accuracy.  

## Steps to Complete
1. In the Azure Portal, open your **Document Intelligence** resource.  
2. Click **Go to Document Intelligence Studio** (opens in a new tab).  
3. In the Studio, scroll to **Prebuilt Models** and select **Invoice**.  
4. Choose **Try the model**.  
5. Upload a sample invoice from the dataset provided.  
6. Wait for the analysis to complete.  
7. Observe the structured output:
   - **Vendor Name**
   - **Invoice ID**
   - **Invoice Date**
   - **Subtotal, Tax, and Total**
   - **Line Items (Description, Quantity, Unit Price)**

## Success Criteria
- Successfully uploaded and processed an invoice using the Prebuilt Model.  
- Model displays structured data fields accurately.  

## Additional Resources
- [Prebuilt Invoice Model](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-invoice)  
- [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio)

Now, click **Next** (bottom right corner) to continue to **Challenge 03: Validate Extracted Invoice Data**.
