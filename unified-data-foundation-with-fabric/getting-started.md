## Getting Started with Challenge

Welcome to Hack in a Day: Unified Data Foundation with Fabric challenge! We've prepared a seamless environment for you to explore and learn. Let's begin by making the most of this experience.

### Accessing Your Challenge Environment

Once you're ready to dive in, your virtual machine and challenge guide will be right at your fingertips within your web browser.

![](./media/gs1.png)

### Exploring Your Challenge Resources

To get a better understanding of your challenge resources and credentials, navigate to the Environment tab.

![](./media/gs-leave-2.png)

### Utilizing the Split Window Feature

For convenience, you can open the challenge guide in a separate window by selecting the Split Window button from the Top right corner

![](./media/gs-leave-3.png)

### Managing Your Virtual Machine

Feel free to start, stop, or restart your virtual machine as needed from the Resources tab. Your experience is in your hands!

![](./media/gs-leave-4.png)

> **Note:** If the VM is not in use, please **deallocate** it to avoid unnecessary resource consumption.

## Let's Get Started with Unified Data Foundation

1. In the JumpVM, click on **Microsoft Edge** browser shortcut which is created on desktop.

   ![](./media/gs-up1.png)

1. Navigate to the **Microsoft Fabric portal**:

   ```
   https://app.fabric.microsoft.com/
   ```

1. On the **Sign into Microsoft** tab, you will see the login screen. Enter the provided email or username, and click **Next** to proceed.

   - Email/Username: <inject key="AzureAdUserEmail"></inject>

     ![](./media/gs-lab3-g2.png)

1. Now, enter the following password and click on **Sign in**.

   - Password: <inject key="AzureAdUserPassword"></inject>

     ![](./media/gs-lab3-g3.png)

     >**Note:** If you see the Action Required dialog box, then select Ask Later option.
     
1. If you see the pop-up **Stay Signed in?**, click No.

   ![](./media/gs-4.png)

1. Welcome to **Microsoft Fabric**! You're now ready to start building your data lakehouse solution using Microsoft Fabric, OneLake, and the Medallion architecture for data engineering with flight loyalty and transaction data.

1. Before proceeding with the challenges, you need to deploy a **Microsoft Fabric capacity** from the Azure portal:

   - Navigate to the **Azure Portal**: https://portal.azure.com
   - Sign in with the provided credentials: <inject key="AzureAdUserEmail"></inject>
   - In the search bar, type **Microsoft Fabric** and select **Microsoft Fabric (preview)**
   - Click **+ Create**
   - Configure the Fabric capacity:
     - **Subscription**: Select your subscription
     - **Resource Group**: Create new or select existing
     - **Capacity name**: **fabric-capacity-<inject key="DeploymentID"></inject>**
     - **Region**: Select the same region as your resources
     - **Size**: Select **F2** SKU (2 vCores, 4 GB RAM)
     - Click **Review + Create**, then **Create**
   - Wait for the deployment to complete (approximately 2-3 minutes)
   - Once deployed, note down the **capacity name** as you'll need it when creating your Fabric workspace

   > **Important:** This lab requires a paid Fabric capacity (F2 SKU). Free trial capacity is not supported for this challenge.

1. The lab environment includes:
   - Dataset files in **C:\LabFiles\fabric-kyndr-uc1\dataset\**
   - Access to create Lakehouses, Notebooks, and Data Science experiments

Now, click on the **Next** from lower right corner to move on next page.

## Happy Hacking!