# Challenge 04: Configure Email Escalation Flow and Integrate it With the Copilot  

## Introduction  
The Copilot can now analyze financial documents and classify risk.  
In this challenge, you will build an **email escalation workflow** that sends a financial risk report to the CFO directly from the Copilot conversation.  
The Copilot will ask the user if they want the report emailed, and only if the user selects **Yes**, an escalation email will be sent.

## Challenge Objectives  
- Create an Outlook-based Send Email (V2) flow to send escalation alerts.  
- Connect the flow to the **Cash Flow Stability & Liquidity Outlook** topic.  
- Ask the user whether the report should be emailed and execute escalation accordingly.

---

## Steps to Complete

### 1 — Create the Flow for Email Escalation  
1. In Copilot Studio, open the **Financial Risk Advisor Copilot** project.  
2. From the left navigation pane, select **Agent flows → + New flow**.  
3. Choose **Send an email (V2)**.  
4. Configure the flow:
   - **Subject:** Risk with the financial report  
   - **Body:** Use the **body** variable (this will carry the complete financial summary from the Copilot)  
   - **Importance:** High  
5. After configuring these fields, add a **Send message** node at the end of the flow.  
6. In the message text box, enter:  
   *The email has been sent successfully.*  
7. Select **Publish** to publish the flow.  
8. Once published, open the **Flow Overview** page and click **Edit** on the Details card.  
9. Change the flow name from **Untitled** to **Outlook Flow**.  
10. Select **Save**.

---

### 2 — Connect the Flow to the Cash Flow Topic  
1. Navigate back to **Topics** → open **Cash Flow Stability & Liquidity Outlook**.  
2. Scroll to the **last Generative Answers node** and select **Edit data source**.  
3. Scroll down and expand **Advanced options**.  
4. Under **Save agent response as**, select **Create new variable**.  
5. Name the variable: **body**  
   (This variable will pass the entire financial summary to the Outlook Flow.)

---

### 3 — Add User Confirmation and Execute the Escalation Flow  
1. Select **+ Add node** under the Generative Answers node.  
2. Choose **Ask a question**.  
3. In the question text, enter:  
   *Do you want me to send this report to the CFO?*  
4. Change the response type to **Multiple choice** with options:  
   • Yes  
   • No  
5. Copilot Studio will automatically generate condition branches:
   • If **Yes selected**  
   • If **No selected**

#### Under the **Yes** branch:
1. Select **Add node → Action**.  
2. Choose **Outlook Flow**.

#### Under the **No** branch:
1. Select **Add node → Send a message**.  
2. Add message text such as:  
   *Thank you for reaching out. Let me know if you need anything else.*

3. Select **Save**.

---

### Test the Complete Escalation Experience  
1. Click **Test** (top right).  
2. Ask the Copilot:  
   *How does our cash flow look this quarter?*  
3. Confirm the full flow:  
   • Copilot analyzes the cash flow  
   • Copilot displays the full summary  
   • Copilot asks whether to send the report to the CFO  
   • If **Yes** → Outlook Flow runs and email is sent  
   • If **No** → Copilot thanks the user without escalation

---

## Success Criteria  
- The Outlook Flow successfully sends an escalation email only when the user selects **Yes**.  
- The full financial summary is included in the email body.  
- The Copilot confirms that the email has been sent.  
- If user selects **No**, conversation ends politely with no escalation attempt.

## Additional Resources  
- https://learn.microsoft.com/microsoft-copilot-studio/actions  
- https://learn.microsoft.com/microsoft-copilot-studio/create-plugin  
- https://learn.microsoft.com/power-automate/flows-overview

---
