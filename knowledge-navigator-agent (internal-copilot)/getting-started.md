## Getting Started with Your Lab

Welcome to Hack in a Day: Knowledge Navigator Agent (Internal Copilot)! We've prepared a complete environment with 40+ Contoso company documents ready for you to build an AI-powered knowledge assistant. Let's begin by setting up your workspace.

### Accessing Your Challenge Environment

Once you're ready to dive in, your virtual machine and challenge guide will be right at your fingertips within your web browser.

![](./media/gs1.png)

### Exploring Your Challenge Resources

To get a better understanding of your challenge resources and credentials, navigate to the Environment tab.

![](./media/gs-leave-2.png)

### Utilizing the Split Window Feature

For convenience, you can open the challenge guide in a separate window by selecting the Split Window button from the top right corner.

![](./media/gs-leave-3.png)

### Managing Your Virtual Machine

Feel free to start, stop, or restart your virtual machine as needed from the Resources tab. Your experience is in your hands!

![](./media/gs-leave-4.png)

## Let's Get Started with Your Environment Setup

### Step 1: Sign In to Power Apps and Create Your Environment

1. In the JumpVM, click on **Microsoft Edge** browser which is created on desktop.

   ![](./media/zgr-gt.png)

1. Open a new browser tab and navigate to the Power Apps portal:

   ```
   https://make.powerapps.com/
   ```

1. On the **Sign into Microsoft** tab, enter the provided credentials and click **Next**:

   - Email/Username: **<inject key="AzureAdUserEmail"></inject>**

     ![](./media/gs-lab3-g2.png)

1. Enter your password and click **Sign in**:

   - Password: **<inject key="AzureAdUserPassword"></inject>**

     ![](./media/gs-lab3-g3.png)

     > **Note:** If you see the Action Required dialog box, select **Ask Later**.
     
1. If you see the pop-up **Stay Signed in?**, click **No**.

   ![](./media/gs-4.png)

1. If the **Welcome to Power Apps** pop-up appears, leave the default country/region selection and click **Get started**.

   ![](./media/gs-travel-g1.png)

1. You're now in the Power Apps portal. Keep it open as you'll use it throughout the lab.

   ![](./media/gs-5.png)

### Step 2: Provision Your Copilot Studio Environment

1. Inside the **Power Apps** portal, select **Tables (1)** from the left navigation menu and click **Create with Excel or .CSV file (2)**.

   ![](./media/ex1-travel-g1.png)

   > **Important:** This creates the foundational Dataverse environment that will support your agent with SharePoint knowledge sources and agent flows.

1. In the **Create in new environment?** dialog, click **Create** to provision your environment.

   ![](./media/ex1-travel-g2.png)

1. When the upload screen appears, click **Cancel** (you won't upload any files here).

   ![](./media/zgr-gt3.png)

1. Click the **environment (1)** name in the top bar, expand **Build apps with Dataverse (2)**, and select **ODL_User<inject key="Deployment ID" enableCopy="false"></inject> (3)** to switch to your new environment.

   ![](./media/ex1-travel-g5.png)

1. Navigate to **Microsoft Copilot Studio** by opening a new browser tab and using the link below:

   ```
   https://copilotstudio.microsoft.com
   ```

1. On the **Welcome to Microsoft Copilot Studio** screen, keep the default **country/region** selection and click **Get Started** to continue.

   ![](./media/gs-travel-g2.png)

1. If the **Welcome to Copilot Studio!** pop-up appears, click **Skip** to continue to the main dashboard.

   ![](./media/gs-travel-g3.png)

1. If you are directly taken to the **agent creation** screen, click the **ellipsis (1)** icon beside the **Create** button, then select **Cancel agent creation (2)** to return to the main dashboard.

   ![](./media/gs-travel-g4.png)

1. In Copilot Studio, open the environment picker **(1)**, expand **Supported environments (2)**, and select **ODL_User <inject key="Deployment ID" enableCopy="false"></inject>'s Environment (3)** to switch.

   ![](./media/ex1-travel-g6.png)

1. If you are not able to see the environment under **Supported environments**, follow the below steps.

   ![](./media/cor2-gs-g4.png)

   1. Go back to the **Power Apps** portal, on your **ODL_User <inject key="Deployment ID" enableCopy="false"></inject>’s Environment** copy the **Environment ID** from the browser URL as highlighted.

      ![](./media/cor2-gs-g5.png)
   
   1. Open a **new browser tab**, and paste the copied **Environment ID** at the end of the following URL to verify access:

      ```
      https://copilotstudio.microsoft.com/environments/(Environment ID)
      ```

      ![](./media/cor2-gs-g6.png)

      > **Note:** Replace **(Environment ID)** with the ID you copied in the previous step.
   
   1. You will be navigated to the **Copilot Studio** portal. Verify that **ODL_User <inject key="Deployment ID" enableCopy="false"></inject>’s Environment** is visible and selected under **Supported environments**.

      ![](./media/cor2-gs-g7.png)

1. You are now ready to start building your **Knowledge Navigator Agent**.

### Step 4: Verify Document Folder Access

1. Before starting the challenges, verify you have access to the Contoso documents folder.

1. Open **File Explorer** and navigate to:

   ```
   c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\knowledge-navigator-agent (internal-copilot)\documents\
   ```

1. You should see 40+ company documents including:
   - Contoso_HR_Handbook.docx
   - Contoso_Procurement_Data_With_Policies.docx
   - Contoso-Corp-IT-Governance&Compliance-Policy.docx
   - Employee-Travel-Reimbursement.xlsx
   - And many more business documents

1. Keep this folder path accessible—you'll upload these documents to SharePoint in Challenge 1.

---

## You're Ready to Begin!

Your environment is now fully configured with:
- ✅ Power Apps portal access
- ✅ Copilot Studio environment provisioned
- ✅ Correct environment selected (ODL_User<inject key="Deployment ID" enableCopy="false"></inject>'s Environment)
- ✅ 40+ Contoso documents ready for upload

**What You'll Build:**
- Agent with SharePoint knowledge source (40+ documents)
- 2 Agent Flows (Email Document, Send Request to Teams)
- 4 AI-Generated Topics (DocumentSearch, EmailDocument, SubmitRequest, NewEmployeeOnboarding)
- Deployment to Microsoft Teams

Now, click on the **Next** from lower right corner to move on next page.

## Happy Hacking!!