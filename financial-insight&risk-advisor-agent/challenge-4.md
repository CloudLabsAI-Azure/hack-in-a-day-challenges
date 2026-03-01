# Challenge 04: Configure Email Escalation Flow and Integrate it With the Copilot  

## Introduction  

The Copilot can now analyze financial documents and classify risk. In this challenge, you will build an **email escalation workflow** that sends a financial risk report to the CFO directly from the Copilot conversation. The Copilot will ask the user if they want the report emailed, and only if the user selects **Yes**, an escalation email will be sent.

## Challenge Objectives  

- Create an Outlook-based Send Email (V2) flow to send escalation alerts.  
- Connect the flow to the **Cash Flow Stability & Liquidity Outlook** topic.  
- Ask the user whether the report should be emailed and execute escalation accordingly.

## Steps to Complete

### Step 1: Create the Flow for Email Escalation  

1. In Copilot Studio, from the left navigation pane, select **Flows** and click **+ New agent flow**

1. You will be navigated to **Designer** pane, under the add a trigger pane, search for **When an agent calls the flow** and select it.

1. Inside **When an agent calls the flow** node, select **Add an input** option to add a **Text** input variable and provide the name as **Body**.

1. Once configured, add one more node by clicking on **+**.

1. Search for **Compose** and select it, It helps to perform operations on the Data. The agent returns responses in Markdown format (using ** for bold, * for italics, etc.). Since Outlook doesn't render Markdown natively, we need to convert these Markdown elements to HTML tags before sending the email. This ensures proper formatting when recipients view the message.

1. In the **Compose** node, click on the input area and select the function icon (fx) to add an expression.

1. In the function area, add the below expression and click on **Add**.

   ```
   replace(replace(replace(replace(triggerBody()?['text'], '**', '<b>'), '- ', '<br>• '), '\n', '<br>'), '*', '<em>')
   ```
1. Once configured, add one more node by clicking on **+**.

1. Search and Choose **Send an email (V2)** . 

1. In the configuration pane, provide **<inject key="AzureAdUserEmail"></inject>** in the **To** parameter.

1. Configure the flow:

   - **Subject:** `Risk with the financial report`

   - **Body:** Click on the input area of the parameter and type `/`, click on **Insert Dynamic Content** and select **Outputs** variable under **Compose**. This will pull the value from the output of compose node.

   - **Importance:** High

1. Select **Publish** to publish the flow.  

1. Once published, open the **Flow Overview** page and click **Edit** on the Details card.  

1. Change the flow name from **Untitled** to **Outlook Flow**.  

1. Select **Save**.

### Step 2: Connect the Flow to the Cash Flow Topic

1. Navigate back to **Topics**  open **Cash Flow Stability & Liquidity Outlook**.  

1. Scroll to the **last Generative Answers node** and select **Edit data source**.  

1. Scroll down and expand **Advanced options**.  

1. Under **Save agent response as**, click on the input area and Select **Create new variable**.  

### Step 3: Add User Confirmation and Execute the Escalation Flow

1. Select **+ Add node** under the Generative Answers node.  

1. Choose **Ask a question**.  

1. In the question text, enter:

   ```
   Do you want me to send this report to the CFO?
   ```

1. As the response type, by default will be **Multiple Choice**, add the below choices: 

   - Yes  

   - No  
   
1. Copilot Studio will automatically generate condition branches:
   - If **Yes selected**  
   - If **No selected**

#### Under the **Yes** branch:

1. Select **+** to add new node, from the list, select **Add a tool** and click on the **Outlook Flow** which you created earlier.

1. Add **Var2** as the input variable, using **...**.

1. Add **Send a message** node under that.

1. Add message text such as:  
   
   ```
   The email has been sent successfully.
   ```

#### Under the **No** branch:

1. Add **Send a message** node.

1. Add message text such as:  
  
   ```
   Thank you for reaching out. Let me know if you need anything else.
   ```

1. Select **Save**.

### Test the Complete Escalation Experience  

1. Click **Test** (top right).

1. Ask the Copilot: 
   
   - How does our cash flow look this quarter?

1. Confirm the full flow:  

   - Copilot analyzes the cash flow based on the answers provided by you. 
   - Copilot displays the full summary  
   - Copilot asks whether to send the report to the CFO  
   - If **Yes**, Outlook Flow runs and email is sent  
   - If **No**, Copilot thanks the user without escalation

## Success Criteria  

- The Outlook Flow successfully sends an escalation email only when the user selects **Yes**.  
- The full financial summary is included in the email body.  
- The Copilot confirms that the email has been sent.  
- If user selects **No**, conversation ends politely with no escalation attempt.

## Additional Resources  

- https://learn.microsoft.com/microsoft-copilot-studio/actions  
- https://learn.microsoft.com/microsoft-copilot-studio/create-plugin  
- https://learn.microsoft.com/power-automate/flows-overview

Click **Next** to continue to **Challenge 05: Publish the Copilot to Microsoft Teams and Test the Full Workflow**.