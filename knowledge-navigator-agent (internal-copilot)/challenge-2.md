# Challenge 02: Connect SharePoint Knowledge Source

## Introduction
Now that you've created your Internal Knowledge Navigator copilot and uploaded all Contoso company documents to SharePoint in Challenge 1, it's time to connect that SharePoint site to your copilot as a knowledge source. This will enable your copilot to search through all 40+ company documents and provide accurate answers to employee questions.

In this challenge, you'll connect the SharePoint site to Copilot Studio, verify the knowledge source is properly indexed, and test basic knowledge retrieval to ensure your copilot can answer questions using the Contoso documents.

## Challenge Objectives
- Connect the SharePoint site as a knowledge source in Copilot Studio
- Verify all documents are successfully indexed
- Configure knowledge source settings
- Test basic knowledge retrieval across different document types
- Ensure the copilot responds using Contoso company documents

## Prerequisites

Before starting this challenge, ensure you have:
- Created the **Internal Knowledge Navigator** agent in Challenge 1
- Created the SharePoint site `contoso-documents-<inject key="DeploymentID"></inject>` in Challenge 1
- Uploaded all 40+ Contoso documents to the SharePoint site in Challenge 1
- Saved the SharePoint site URL

## Steps to Complete

### Step 1: Add SharePoint Knowledge Source

- Open **Microsoft Copilot Studio** in your browser:

   ```
   https://copilotstudio.microsoft.com
   ```

- Ensure you're in the **ODL_User<inject key="DeploymentID"></inject>** environment (check the environment selector in the top-right).

- Select your **Internal Knowledge Navigator** agent from the agents list.

- On the **Start building your agent** page, scroll down and select **+ Add** to add knowledge sources.

- Select **SharePoint** from the **Add Knowledge** window.

- Enter the **SharePoint site URL** that you copied in Challenge 1:
   ```
   https://yourdomain.sharepoint.com/sites/contoso-documents-<inject key="DeploymentID"></inject>
   ```

   > **Tip:** If you didn't save the URL, go back to your SharePoint site in another tab and copy it from the address bar.

- Select **Add**.

   > **Note:** If the site link shows **"This item was not found in your SharePoint or OneDrive files"**, this may occur due to temporary indexing delays. Select **Add anyway** to continue.

- Select **Add to agent** to add the SharePoint knowledge source.

- Wait for the confirmation message that the SharePoint site has been added.

   > **What's happening:** Copilot Studio is now connecting to your SharePoint site and will automatically index all 40+ documents you uploaded in Challenge 1.

### Step 2: Verify Knowledge Source Connection

- After adding SharePoint, navigate to **Knowledge** in the left navigation pane.

- You should see the SharePoint site listed as a knowledge source with the name: `contoso-documents-<inject key="DeploymentID"></inject>`

- The status should show as **Processing** or **Syncing** initially.

- Wait for the status to change to **Active** or **Ready** (this may take 3-10 minutes for 40+ documents).

   > **Note:** The SharePoint connector will automatically index all documents in the Documents library. You don't need to upload individual files.

- If the status shows **Failed** or **Error**, try the following:
   - Verify the SharePoint site URL is correct
   - Check that you have access to the SharePoint site
   - Remove and re-add the knowledge source

### Step 3: Verify Knowledge Source Indexing

- In the **Knowledge** section, click on your SharePoint knowledge source to view details.

- You should see information about:
   - **Source type:** SharePoint
   - **Status:** Active (or Ready)
   - **Documents indexed:** Number of documents found and indexed
   - **Last synced:** Timestamp of last indexing

- Verify that the document count is approximately 40+ documents.

   > **Note:** The SharePoint connector automatically indexes all files in the Documents library. You'll see a single SharePoint entry, not individual files listed.

- If indexing is still in progress, wait a few more minutes and refresh the page.

### Step 4: Disable Web Search

- In the **Knowledge** section, scroll down to the **Web Search** area.

- Ensure that **Web Search** is set to **Disabled**.

   > **Important:** This ensures the agent only uses information from your Contoso SharePoint documents and doesn't search the public web for answers.

## Success Criteria
- SharePoint knowledge source is connected to Copilot Studio
- SharePoint knowledge source shows **Active** or **Ready** status
- Knowledge source has indexed 40+ Contoso documents
- Web Search is disabled for the agent

## Additional Resources
- [Add knowledge sources to your copilot](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)  
- [Generative answers with uploaded files](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node)  
- [Manage knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-manage-sources)

---

Now, click **Next** to continue to **Challenge 03: Design Department Topics**.
