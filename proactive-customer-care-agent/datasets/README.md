# Customer Care Copilot - Knowledge Base Datasets

## Overview
This folder contains comprehensive customer care documentation across four major industries for building a Customer Care Copilot in Microsoft Copilot Studio.

## Contents

### Knowledge Base Documents (Markdown Format)
These documents should be converted to PDF format before uploading to Copilot Studio:

1. **customer-care-ecommerce.md**
   - Comprehensive e-commerce customer service procedures
   - Order management, shipping, returns, refunds
   - Account management and payment methods
   - Promotions, technical support, contact information
   - Size: Approximately 6,500 words

2. **customer-care-food-delivery.md**
   - Food delivery service customer care guide
   - Ordering process, delivery information, quality standards
   - Payment, billing, account management
   - Restaurant partners, promotions, technical support
   - Size: Approximately 5,800 words

3. **customer-care-retail.md**
   - Retail and department store customer service
   - Shopping services, store information, product details
   - Returns, exchanges, gift services, loyalty program
   - Online and in-store integration, payment options
   - Size: Approximately 6,200 words

4. **customer-care-telecom.md**
   - Telecommunications and wireless services support
   - Account management, billing, plans and services
   - Device support, network coverage, technical support
   - Moving services, business services
   - Size: Approximately 6,000 words

## Converting Markdown to PDF

### Method 1: Using Pandoc (Recommended)
```powershell
# Install Pandoc: https://pandoc.org/installing.html

# Convert all files
pandoc customer-care-ecommerce.md -o customer-care-ecommerce.pdf
pandoc customer-care-food-delivery.md -o customer-care-food-delivery.pdf
pandoc customer-care-retail.md -o customer-care-retail.pdf
pandoc customer-care-telecom.md -o customer-care-telecom.pdf
```

### Method 2: Using VS Code Extension
1. Install "Markdown PDF" extension in VS Code
2. Open each .md file
3. Right-click and select "Markdown PDF: Export (pdf)"
4. PDF will be saved in same directory

### Method 3: Using Microsoft Word
1. Open each .md file in VS Code or text editor
2. Copy all content
3. Paste into Microsoft Word
4. Format as needed (Word recognizes markdown formatting)
5. Save as PDF

### Method 4: Online Converters
- https://www.markdowntopdf.com/
- https://md2pdf.netlify.app/
- Upload .md file and download PDF

## Document Statistics

| Document | Pages (approx) | Words | Topics Covered |
|----------|----------------|-------|----------------|
| E-Commerce | 20-24 | 6,500 | 9 major sections, 60+ procedures |
| Food Delivery | 18-22 | 5,800 | 9 major sections, 50+ procedures |
| Retail | 19-23 | 6,200 | 9 major sections, 55+ procedures |
| Telecom | 19-23 | 6,000 | 9 major sections, 50+ procedures |

## Usage in Copilot Studio

### Step 1: Convert to PDF
Convert all 4 markdown files to PDF format using one of the methods above.

### Step 2: Upload to Copilot Studio
1. Open your copilot in Copilot Studio
2. Navigate to **Knowledge** section
3. Click **Add knowledge** → **Files**
4. Upload all 4 PDF files:
   - customer-care-ecommerce.pdf
   - customer-care-food-delivery.pdf
   - customer-care-retail.pdf
   - customer-care-telecom.pdf
5. Wait for indexing (may take 5-10 minutes)

### Step 3: Enable Generative Answers
1. Go to **Settings** → **Generative AI**
2. Toggle on **Generative answers**
3. Select **Search only selected sources**
4. Ensure all 4 documents are selected as knowledge sources

### Step 4: Test Knowledge Base
Test with sample questions across different domains:

**E-Commerce:**
- "What is your return policy?"
- "How do I track my order?"
- "Can I cancel my order?"

**Food Delivery:**
- "How long does delivery take?"
- "What if my food is cold?"
- "Do you have vegetarian options?"

**Retail:**
- "Where is the nearest store?"
- "Can I return items without a receipt?"
- "How does the loyalty program work?"

**Telecom:**
- "How do I change my plan?"
- "Why is my bill higher this month?"
- "How do I upgrade my phone?"

## Document Quality Assurance

### Coverage
- Order and service management: Complete
- Billing and payment: Complete
- Returns and refunds: Complete
- Customer support: Complete
- Account management: Complete
- Technical support: Complete

### Formatting
- Clear hierarchical structure with headers
- Numbered and bulleted lists
- Tables for quick reference
- Contact information sections
- Policy definitions and procedures

### Content Quality
- Real-world customer service scenarios
- Step-by-step instructions
- Clear escalation paths
- Multiple contact methods
- Professional tone throughout

## Maintenance and Updates

### Document Versioning
All documents include:
- Version number (current: 1.0)
- Last updated date
- Classification level
- Review schedule
- Revision history section

### Recommended Updates
- Quarterly: Review and update procedures
- Monthly: Update contact information and hours
- As needed: Policy changes and new services
- Annually: Full document review and revision

## Support and Feedback

For questions or suggestions about these knowledge base documents:
- Document owner: Customer Care Department
- Contact: customercare@contoso.com
- Last comprehensive review: December 2025
- Next scheduled review: June 2026

## License and Usage

**Classification:** Internal Use Only
**Distribution:** Lab participants and customer service teams
**Modification:** Encouraged for your organization's specific needs
**Format:** Markdown source files for easy customization

## Tips for Lab Participants

1. **Read the documents first** - Familiarize yourself with the content structure
2. **Test incrementally** - Upload one document at a time and test
3. **Use domain-specific questions** - Test each knowledge base thoroughly
4. **Monitor citations** - Verify copilot cites the correct source documents
5. **Iterate on responses** - Adjust if copilot answers incorrectly
6. **Combine scenarios** - Test questions that span multiple documents

## Common Issues and Solutions

### Issue: PDF upload fails
**Solution:** 
- Ensure each file is under 25 MB
- Markdown to PDF conversion should keep files well under this limit
- Check for special characters in filenames

### Issue: Copilot can't find information
**Solution:** 
- Verify documents are indexed (status should be "Ready")
- Check that Generative AI is enabled
- Ensure documents are selected as knowledge sources
- Allow 5-10 minutes for full indexing
- Try rephrasing the question

### Issue: Responses are too generic
**Solution:**
- Verify knowledge sources are properly configured
- Create custom topics for most common questions
- Use more specific queries in testing
- Check that correct document is being cited

### Issue: Wrong document cited
**Solution:**
- Questions may overlap between industries
- Use industry-specific terms in queries
- Review and adjust document content if needed
- Topics can specify which knowledge sources to use

## Document Structure

Each knowledge base document follows this consistent structure:

1. **Document Information** - Version, date, classification, industry
2. **Table of Contents** - Quick navigation to all sections
3. **Core Service Sections** - Industry-specific main topics (7-9 sections)
4. **Contact Information** - Multiple contact methods and support hours
5. **Document Control** - Revision history and review schedule

This consistent structure helps the AI understand and retrieve information effectively across all industries.

---

**Ready to build your Customer Care Copilot? Start by converting these documents to PDF format.**
