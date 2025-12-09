# Challenge 04: Send Shortlist Reports to the Hiring Manager via Email

## Introduction
The HR Interview Copilot can now evaluate resumes and generate personalized insights for HR.  
In this challenge, you will enhance the Copilot to automatically generate a **shortlist report** and email it to the **Hiring Manager** once HR approves.

This transforms the Copilot into a practical assistant that supports the full recruitment workflow, not just conversations.

## Challenge Objectives
- Request HR approval before sending the shortlist report.
- Trigger a Power Automate flow using Outlook.
- Email the Hiring Manager a structured candidate report based on evaluation results.
- Notify the user that the email has been successfully sent.

## Steps to Complete

### Step 1: Capture HR consent after resume evaluation

1. Open the **Resume Fit & Evaluation** topic in Copilot Studio.

1. Under data sources in **Generative answers** node, click on **edit**.

1. In the configuration pane, scroll down to bottom and expand **Advanced >** option.

1. Once expanded, under **Save agent response as**, click on the input area and Select **Create new variable**. This will create a new variable to save the agent response.

1. After the final **Generative answers** node, click **+ Add node**.

1. Select **Ask a question**.

1. Enter the following prompt:

   ```
   Would you like me to send the shortlist report to the Hiring Manager?
   ```

1. As the response type, by default will be **Multiple Choice**, add the below choices:

   - Yes  

   - No  

1. Copilot Studio will create two branches automatically.

### Step 2: Configure the **No** branch

1. Under the **No** branch, add a **Send a message** node.

1. Enter:
   No worries. Let me know if you need help with anything else in the hiring process.

1. This closes the evaluation workflow gracefully.

1. Click on save, to save the topic, you will congigure **Yes** branch later.

### Step 3: Create a Power Automate flow (Send Email to Hiring Manager)

1. In Copilot Studio, from the left navigation pane, select **Flows → + New agent flow**

1. You will be navigated to **Designer** pane, under the add a trigger pane, search for **When an agent calls the flow** and select it.

1. Inside **When an agent calls the flow** node, select **Add an input** option to add a input variable and provide the name as **Body**.

1. Once configured, add one more node by clicking on **+**.

1. Search for **Compose** and select it, It helps to perform operations on the Data. The agent returns responses in Markdown format (using ** for bold, * for italics, etc.). Since Outlook doesn't render Markdown natively, we need to convert these Markdown elements to HTML tags before sending the email. This ensures proper formatting when recipients view the message.

1. In the **Compose** node, click on the input area and select the function icon (fx) to add an expression.

1. In the function area, add the below expressiona nd click on **Add**.

   ```
   replace(replace(replace(replace(triggerBody()?['text'], '**', '<b>'), '- ', '<br>• '), '\n', '<br>'), '*', '<em>')
   ```
1. Once configured, add one more node by clicking on **+**.

1. Search and Choose **Send an email (V2)** node. 

1. In the configuration pane, provide **<inject key="AzureAdUserEmail"></inject>** in the **To** parameter.

1. Configure the flow:

   - **Subject:** `Candidate Evaluation Report`

   - **Body:** Click on the input area of the parameter and type `/`, click on **Insert Dynamic Content** and select **Outputs** variable under **Compose**. This will pull the value from the output of compose node.

1. Select **Publish** to publish the flow.  

1. Once published, open the **Flow Overview** page and click **Edit** on the Details card.  

1. Change the flow name from **Untitled** to **Outlook Flow**.  

1. Select **Save**.

### Step 4: Connect the flow to the “Yes” branch

1. Navigate back to **Agents** from left menu, select **HR Interview Copilot**.

1. In the **Resume Fit & Evaluation** topic, under the **Yes** branch, click **+ Add node**.

1. From the list, select **Add a tool** and click on the **Outlook Flow** which you created earlier.

1. After that node, add a **Send a message** node and enter:

   ```
   The shortlist report has been emailed to the Hiring Manager.
   ```

1. Click **Save** (top-right) to finalize the updated topic.

## Test the Shortlist Workflow

1. Click **Test** (top-right).

1. Trigger the Resume Fit & Evaluation workflow:

   ```
   Evaluate The candidate resumes
   ```
1. Once it asks for the role, enter any of the given role:

   - `Software Developer`
   - `AI Engineer`

1. On the next prompt to specify, enter the follwoing prompt:

   ```
   Evaluate all resumes and generate a report on shortlisted candidate.
   ```

1. Confirm the Copilot:
   - Evaluates the resume  
   - Asks if you want to email the shortlist report

1. Select **Yes**.

   >Note: If a pop up comes to **allow a connection**, please click on allow.

1. Verify the Copilot responds:

   ```
   The shortlist report has been emailed to the Hiring Manager.
   ```

1. Login to outlook with the same credentials you've used to login for Copilot Studio. Use the below URL to login: 

   ```
   https://outlook.office.com/
   ```
1. Verify that you recived a mail.

<validation step="2a5b1b60-20f7-438c-b026-02527c906a13" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- The Copilot now supports a full recruitment workflow, not just Q&A.
- The shortlist report email includes real evaluation details from uploaded documents.
- Only HR approval triggers the email — ensuring safe and controlled automation.
- Copilot communicates the result clearly after sending the email.

## Additional Resources
- https://learn.microsoft.com/microsoft-copilot-studio/topics
- https://learn.microsoft.com/en-us/power-automate/
- https://learn.microsoft.com/microsoft-copilot-studio/variables

Click **Next** to continue to **Challenge 05: Publish the HR Interview Copilot to Microsoft Teams and Test the Full Workflow**.
