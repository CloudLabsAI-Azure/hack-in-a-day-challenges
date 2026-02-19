# Getting Started with the Lab

## Accessing Your Lab Environment

1. Once the environment is provisioned, a virtual machine (JumpVM/LabVM) and lab guide will be loaded in your browser. Use this virtual machine throughout the workshop to perform the lab.

1. To get the lab environment details, select the **Environment** tab. The credentials will also be emailed to your registered email address. You can open the Lab Guide on a separate, full window by selecting the **Split Window** icon at the bottom right corner.

   ![](media/getting-started-1.png)

## Login to Azure Portal

1. In the JumpVM, click on the **Azure Portal** shortcut of the Microsoft Edge browser, which is created on the desktop.

   ![](media/getting-started-2.png)

1. On the **Sign in to Microsoft Azure** tab, you will see the login screen. Enter the following email/username, and click **Next**.

   - **Email/Username:** <inject key="AzureAdUserEmail" />

   ![](media/getting-started-3.png)

1. Now enter the following password and click **Sign in**.

   - **Password:** <inject key="AzureAdUserPassword" />

   ![](media/getting-started-4.png)

1. If you see the pop-up **Stay Signed in?**, click **No**.

1. If a **Welcome to Microsoft Azure** pop-up window appears, click **Cancel** to skip the tour.

1. Now you will see the Azure Portal Dashboard. Click on **Resource groups** from the Navigate panel to see the resource groups.

   ![](media/getting-started-5.png)

1. Confirm that you have a resource group named **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**. This resource group contains the pre-provisioned resources for this hackathon.

   ![](media/getting-started-6.png)

## Pre-provisioned Resources

Your lab environment includes the following resources:

| Resource | Name | Purpose |
|----------|------|---------|
| **Resource Group** | challenge-rg-<inject key="DeploymentID" enableCopy="false"/> | Contains all hackathon resources |
| **Azure Subscription** | Azure subscription with Owner access | Full permissions for resource creation |
| **Virtual Machine** | JumpVM with Python 3.11, VS Code, Azure CLI pre-installed | Your development workstation |

## Important Notes

- Use the credentials provided in the **Environment** tab for all Azure operations.
- Your Azure region is: **<inject key="Region" />**
- Your Deployment ID is: **<inject key="DeploymentID" enableCopy="false"/>** — use this to keep resource names unique.
- If you encounter any issues, reach out to the support team via the **Help** tab or email cloudlabs-support@spektrasystems.com.

## Tips for Success

- **Read each challenge fully** before starting — understanding the big picture helps.
- **Test incrementally** — verify each step before moving to the next.
- **Use the playground** — Azure AI Foundry's playground is your best friend for testing agents.
- **Check Success Criteria** — each challenge ends with a checklist. Make sure you can tick every box.
- **Don't skip the validation steps** — they confirm your progress and unlock the next challenge.

Click **Next** to begin **Challenge 1: Set Up Azure Infrastructure**.
