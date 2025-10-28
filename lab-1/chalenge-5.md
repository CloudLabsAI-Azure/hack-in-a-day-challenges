# Challenge 05: Visualize Extracted Invoice Summary

## Introduction
Once invoice data is stored, finance teams want quick visual insights — such as total spending, vendor breakdowns, and invoice trends.  
Azure Storage integrates seamlessly with **Power BI** and **Excel**, enabling instant data visualization and reporting.

In this challenge, you’ll visualize extracted invoice data using Power BI to create an invoice summary dashboard.

## Challenge Objectives
- Import JSON data from Azure Storage.  
- Build visual summaries for financial reporting.  
- Highlight total invoices, vendors, and tax summaries.

## Steps to Complete

1. Open **Power BI Desktop** in your environment.  
2. Click **Get Data → Azure → Azure Blob Storage**.  
3. Enter your Storage Account name and key.  
4. Navigate to `invoices-output` container and load the JSON file.  
5. Use **Transform Data** to flatten fields.  
6. Create visuals such as:
   - Total Invoices  
   - Total Amount Processed  
   - Vendor Distribution  

## Success Criteria
- Working financial summary report generated from extracted data.  
- Key metrics displayed clearly.

## Additional Resources
- [Import JSON into Excel](https://support.microsoft.com/office/import-json-data-into-excel)  
- [Connect Power BI to Azure Blob Storage](https://learn.microsoft.com/power-bi/connect-data/desktop-connect-azure-blob-storage)

Now, click **Next** to continue to **Challenge 06: Clean Up Resources**.
