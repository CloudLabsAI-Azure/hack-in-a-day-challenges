# IT Support Copilot - Knowledge Base and Datasets

## Overview
This folder contains comprehensive IT support documentation and test scenarios for building an IT Support Copilot in Microsoft Copilot Studio.

## Contents

### Knowledge Base Documents (Markdown Format)
These documents should be converted to PDF format before uploading to Copilot Studio:

1. **IT_Support_FAQ_Password_Reset.md**
   - Comprehensive password reset procedures
   - Self-service portal instructions
   - Account lockout procedures
   - Security best practices
   - Common issues and solutions
   - Size: ~5000 words

2. **IT_Support_SOP_VPN_Issues.md**
   - VPN connection troubleshooting guide
   - Tier 1, 2, and 3 troubleshooting steps
   - Platform-specific instructions (Windows, macOS, mobile)
   - Common error codes and solutions
   - Network configuration guidance
   - Size: ~6000 words

3. **IT_Support_SOP_Slow_Laptop.md**
   - Performance troubleshooting procedures
   - Quick fixes (5-10 minutes)
   - Intermediate solutions (15-30 minutes)
   - Advanced troubleshooting (30+ minutes)
   - Hardware vs software issue identification
   - Preventive maintenance guide
   - Size: ~5500 words

4. **IT_Support_SOP_Printer_Issues.md**
   - Comprehensive printer troubleshooting
   - Network, USB, and wireless printer support
   - Paper jam removal procedures
   - Print quality troubleshooting
   - Driver installation and updates
   - Mobile printing instructions
   - Size: ~5000 words

### Test Scenarios

**IT_Support_Test_Scenarios.csv**
- 100 realistic user questions across all support categories
- Includes complexity ratings and expected response types
- Covers edge cases and multi-issue scenarios
- Use for testing copilot responses

## Converting Markdown to PDF

### Method 1: Using Pandoc (Recommended)
```bash
# Install Pandoc: https://pandoc.org/installing.html

# Convert all files
pandoc IT_Support_FAQ_Password_Reset.md -o IT_Support_FAQ_Password_Reset.pdf
pandoc IT_Support_SOP_VPN_Issues.md -o IT_Support_SOP_VPN_Issues.pdf
pandoc IT_Support_SOP_Slow_Laptop.md -o IT_Support_SOP_Slow_Laptop.pdf
pandoc IT_Support_SOP_Printer_Issues.md -o IT_Support_SOP_Printer_Issues.pdf
```

### Method 2: Using VS Code Extension
1. Install "Markdown PDF" extension in VS Code
2. Open each .md file
3. Right-click → "Markdown PDF: Export (pdf)"

### Method 3: Using Microsoft Word
1. Open each .md file in VS Code or text editor
2. Copy all content
3. Paste into Microsoft Word
4. Format as needed (Word will recognize markdown formatting)
5. Save as PDF

### Method 4: Online Converters
- https://www.markdowntopdf.com/
- https://md2pdf.netlify.app/
- Upload .md file → Download PDF

## Document Statistics

| Document | Pages (approx) | Words | Topics Covered |
|----------|----------------|-------|----------------|
| Password Reset FAQ | 15-18 | 5000 | 10 major sections, 80+ procedures |
| VPN Issues SOP | 18-22 | 6000 | 15 major sections, 3-tier troubleshooting |
| Slow Laptop SOP | 16-20 | 5500 | 16 major sections, 40+ fixes |
| Printer Issues SOP | 15-18 | 5000 | 10 major sections, all printer types |

## Usage in Copilot Studio

### Step 1: Convert to PDF
Convert all 4 markdown files to PDF format using one of the methods above.

### Step 2: Upload to Copilot Studio
1. Open your copilot in Copilot Studio
2. Navigate to **Knowledge** → **Add knowledge** → **Files**
3. Upload all 4 PDF files:
   - IT_Support_FAQ_Password_Reset.pdf
   - IT_Support_SOP_VPN_Issues.pdf
   - IT_Support_SOP_Slow_Laptop.pdf
   - IT_Support_SOP_Printer_Issues.pdf
4. Wait for indexing (may take 5-10 minutes)

### Step 3: Enable Generative Answers
1. Go to **Settings** → **Generative AI**
2. Toggle on **Generative answers**
3. Select **Search only selected sources**
4. Ensure all 4 documents are selected

### Step 4: Test with Scenarios
Use questions from IT_Support_Test_Scenarios.csv to test your copilot:
- Easy scenarios (1-30): Basic questions, should answer quickly
- Medium scenarios (31-60): More complex, may require multiple steps
- Hard scenarios (61-85): Advanced troubleshooting
- Edge cases (86-100): Security, policy, and escalation scenarios

## Document Quality Assurance

### Coverage
✅ Password resets - Complete (self-service, manual, lockouts)
✅ VPN issues - Complete (all platforms, error codes, troubleshooting tiers)
✅ Slow laptops - Complete (quick to advanced fixes, hardware vs software)
✅ Printer issues - Complete (all printer types, quality, connectivity)

### Formatting
✅ Clear hierarchical structure with headers
✅ Step-by-step instructions with numbered lists
✅ Visual indicators (✅ ❌ ⚠️ icons)
✅ Tables for quick reference
✅ Decision trees and flowcharts
✅ Code blocks for commands

### Content Quality
✅ Real-world scenarios and solutions
✅ Success rates and estimated times
✅ Escalation criteria clearly defined
✅ Contact information included
✅ Common errors and troubleshooting
✅ Best practices and prevention tips

## Maintenance and Updates

### Document Versioning
All documents include:
- Version number (current: 2.1 - 3.2)
- Last updated date
- Revision history table
- Next review date

### Recommended Updates
- Quarterly: Review and update procedures
- After major software updates: Update screenshots and steps
- When new issues emerge: Add to troubleshooting sections
- Annually: Full document review and rewrite

## Support and Feedback

For questions or suggestions about these knowledge base documents:
- Document owner: IT Support Team
- Contact: itsupport@company.com
- Last comprehensive review: December 2025
- Next scheduled review: June 2026

## License and Usage

**Classification:** Internal Use Only
**Distribution:** Lab participants and IT staff
**Modification:** Encouraged for your organization's specific needs

## Pro Tips for Lab Participants

1. **Read the documents first** - Familiarize yourself with the content structure
2. **Test incrementally** - Upload one document at a time and test
3. **Use test scenarios** - Systematically work through the CSV test cases
4. **Iterate on responses** - If copilot answers incorrectly, check document phrasing
5. **Monitor citations** - Verify copilot is citing the correct documents
6. **Expand gradually** - Start with simple questions, then move to complex ones

## Common Issues and Solutions

### Issue: PDF upload fails
**Solution:** Ensure file size is under 25 MB each. Markdown to PDF conversion should keep files under this limit.

### Issue: Copilot can't find information
**Solution:** 
- Check if documents are indexed (status should be "Ready")
- Verify Generative AI is enabled and documents are selected as sources
- Try rephrasing the question

### Issue: Responses are too generic
**Solution:**
- Add more specific instructions in Generative AI settings
- Create custom topics for the most common questions
- Fine-tune the system prompt

### Issue: Citations missing
**Solution:**
- Enable "Show sources" in Generative AI settings
- Documents must be fully indexed
- Complex queries may combine multiple sources

## Appendix: Document Structure

Each knowledge base document follows this structure:
1. **Document Information** - Version, date, classification
2. **Table of Contents** - Quick navigation
3. **Overview** - Purpose, scope, common causes
4. **Quick Reference** - Fast lookup tables and checklists
5. **Detailed Procedures** - Step-by-step instructions
6. **Troubleshooting** - Issue-specific solutions
7. **Advanced Topics** - Complex scenarios
8. **Escalation Criteria** - When to involve IT support
9. **Contact Information** - Support channels
10. **Appendix** - Additional resources and references

This consistent structure helps the AI understand and retrieve information effectively.

---

**Ready to build your IT Support Copilot? Start by converting these documents to PDF!**
