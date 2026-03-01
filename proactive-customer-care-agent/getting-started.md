## Getting Started with Challenge

Welcome to Hack in a Day: Build a Proactive Customer Care Agent challenge! We've prepared a seamless environment for you to explore and learn. Let's begin by making the most of this experience.

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

## Let's Get Started with Copilot Studio and Microsoft 365

1. In the JumpVM, click on the **Microsoft Edge** browser shortcut on the desktop.

   ![](./media/zgr-gt.png)

1. Open a new browser tab and navigate to the Power Apps portal by entering the following URL:

   ```
   https://make.powerapps.com/
   ```

1. On the **Sign into Microsoft** tab, enter the following email **(1)** in the email field, and then click **Next (2)** to proceed.

   - Email: **<inject key="AzureAdUserEmail"></inject>**

     ![](./media/gs-lab3-g2.png)

1. On the **Enter Temporary Access Pass** screen, enter the following **Temporary Access Pass**, and then click **Sign in (2)**.

   - Temporary Access Pass: **<inject key="AzureAdUserPassword"></inject>**

     ![](./media/gs-lab3-g3.png)
     
1. If you see the pop-up **Stay Signed in?**, click **No**.

   ![](./media/gs-4.png)

1. If the **Welcome to Power Apps** pop-up appears, leave the default country/region selection and click **Get started**.

   ![](./media/gs-travel-g1.png)

1. You have now successfully logged in to the Power Apps portal. Keep the portal open.

   ![](./media/gs-5.png)

   > **Note:** We are signing in to the Power Apps portal because it automatically assigns a Developer license, which is required to create and use a Developer environment in the next steps.

1. Open a new browser tab and navigate to the Power Platform admin center by entering the following URL:

   ```
   https://admin.powerplatform.microsoft.com
   ```

1. In the **Power Platform admin center**, select **Manage** from the left navigation pane.

   ![](./media/nd-d2-cor-g-1.png)

1. In the Power Platform admin center, select **Environments (1)** from the left navigation pane, and then choose **New (2)** to create a new environment.

   ![](./media/d2-coor-gs-g2.png)

1. In the **New environment** pane, configure the environment with the following settings, and then select **Next (3)**:

   - Enter **ODL_User <inject key="DeploymentID" enableCopy="false"></inject>'s Environment** in the **Name (1)** field.
   - Select **Developer (2)** from the **Type** dropdown.

      ![](./media/nimg25.png)

1. In the **Add Dataverse** pane, leave all settings as default, and then select **Save**.

   ![](./media/d2-coor-gs-g4.png)

   > **Environment Foundation:** This step creates the foundational environment that will support your agents with company-specific data and knowledge sources.

   > **Note:** Environment provisioning may take 10-15 minutes to complete. Wait until the status shows as ready before proceeding.

   > **Note:** If you see an error stating that the environment list cannot be displayed, this is expected while the environment is being created in the background. After 10-15 minutes, refresh the browser and the environment should appear.

1. In the **Power Platform admin center**, select **Manage (1)**, choose **Environments (2)**, and then click **ODL_User <inject key="DeploymentID" enableCopy="false"/>'s Environment (3)**.

   ![](./media/uppowadminimg1.png)

1. In the environment page, click on **See all** under **S2S apps**.

   ![](./media/pro-activ-gg-g3.png)

1. In the next pane, click on **+ New app user**.

   ![](./media/uppowadminimg3.png)

1. In the create a new app user pane, under **App**, click on **+ Add an app**.

   ![](./media/pro-activ-gg-g4.png)

1. In the **Add an app from Microsoft Entra ID** pane, enter `https://cloudlabssandbox.onmicrosoft.com/cloudlabs.ai/` in the search box **(1)**, select the app from the results **(2)**, and then click **Add (3)**.

   ![](./media/pro-activ-gg-g5.png)

1. Under **Business unit**, enter **org (1)** in the search box, and then select the available business unit from the list **(2)**.

   ![](./media/pro-activ-gg-g6.png)

1. Beside **Security roles** click on **Edit** icon.

   ![](./media/pro-activ-gg-g7.png)

1. In the **Sync Permissions** pane, select **System Administrator (1)**, and then click **Save (2)**.

   ![](./media/pro-activ-gg-g8.png)

1. In the pop-up window, select **save**.

   ![](./media/pro-activ-gg-g9.png)

1. Review all the details and click on **Create**.

   ![](./media/pro-activ-gg-g10.png)

1. Navigate to **Microsoft Copilot Studio** by opening a new browser tab and entering the following URL:

   ```
   https://copilotstudio.microsoft.com
   ```

1. On the **Welcome to Microsoft Copilot Studio** screen, keep the default **country/region** selection and click **Get Started** to continue.

   ![](./media/pro-activ-gg-g11.png)

1. If the **Welcome to Copilot Studio!** pop-up appears, click **Skip** to continue to the main dashboard.

   ![](./media/gs-travel-g3.png)

1. If the **We've updated you to the latest version of Microsoft Copilot Studio** pop-up appears, click **Got it!**.

   ![](./media/pro-activ-gg-g12.png)

1. If the **What's new in Copilot Studio** pop-up appears, click the **Close (X)** icon to dismiss it.

   ![](./media/pro-activ-gg-g13.png)

1. In Copilot Studio, open the environment picker **(1)**, expand **Supported environments (2)**, and select **ODL_User <inject key="Deployment ID" enableCopy="false"></inject>'s Environment (3)** to switch.

   ![](./media/ex1-travel-g6.png)

1. You are now ready to start building your **Proactive Customer Care Agent** using Microsoft Copilot Studio! This agent will help customers with order tracking, product returns, delivery delays, and service complaints, and will integrate with Freshdesk for automated ticket creation.

   ![](./media/pro-activ-gg-g14.png)

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g16.png)

## Happy Hacking!!
