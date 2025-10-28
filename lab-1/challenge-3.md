# Challenge 03: Validate Extracted Invoice Data

## Introduction
While AI models can extract information efficiently, it’s important to **validate the extracted data** before it’s stored or used in financial reports.  
Common checks include verifying totals, date formats, and completeness of vendor or invoice details.

In this challenge, you’ll perform validation checks on the extracted invoice data using built-in features of Document Intelligence Studio.

## Challenge Objectives
- Review extracted JSON output from the prebuilt model.  
- Validate key fields against logical business rules.  
- Identify missing or inaccurate data entries.

## Steps to Complete
1. In **Document Intelligence Studio**, click **View JSON Output** on your analyzed invoice.  
2. Review extracted fields such as:
   - `InvoiceId`
   - `VendorName`
   - `Subtotal`
   - `Tax`
   - `Total`
3. Manually confirm:
   - **Subtotal + Tax ≈ Total** (allowing rounding differences).  
   - **Invoice Date** is formatted as `YYYY-MM-DD`.  
   - **VendorName** and **InvoiceId** are not empty.  
4. Document any inconsistencies in your Notes section or workspace comments.  
5. (Optional) Download the JSON output for later storage.

## Success Criteria
- Extracted data validated against business logic.  
- Ready for storage and reporting in the next challenge.

## Additional Resources
- [Azure Document Intelligence Field Output Reference](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-fields)  
- [Best Practices for Model Accuracy](https://learn.microsoft.com/azure/ai-services/document-intelligence/how-to-improve-results)

Now, click **Next** to proceed to **Challenge 04: Store Extracted Results in Azure Storage**.
