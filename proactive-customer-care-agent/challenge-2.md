# Challenge 02: Setup Freshdesk & Get API Credentials

## Introduction
When the agent cannot resolve an issue automatically, it needs to create a support ticket in your helpdesk system. Freshdesk is a popular cloud-based helpdesk solution that integrates seamlessly with Copilot Studio through its API connector.

In this challenge, you will activate your Freshdesk free trial, configure your account, and obtain the API credentials needed to connect Copilot Studio to Freshdesk for automated ticket creation.

## Challenge Objectives
- Activate Freshdesk free trial account
- Configure Freshdesk profile and settings
- Obtain API Key and Account URL
- Prepare credentials for Copilot Studio integration

## Steps to Complete

### Step 1: Setup Freshdesk Free Trial Account

1. Open **Microsoft Edge** browser in your lab VM.

1. Navigate to the **Freshworks Portal** by entering the following URL in the browser:

   ```
   https://www.freshworks.com/freshdesk/
   ```

1. On the Freshdesk homepage, select **Try it free** to start creating your trial account.

1. Fill in the registration form with the following details, accept the **Terms & Conditions**.

   | Field | Value |
   |-------|-------|
   | First name | **ODL User** |
   | Last name | **<inject key="DeploymentID"></inject>** |
   | Work email | **<inject key="AzureAdUserEmail" enableCopy="false"/>** |
   | Company name | **Contoso** |
   | Organization size | **11-50** |
   | Terms & Conditions | **Checked** |

1. Click **Try it free**.

1. If prompted with a CAPTCHA challenge, complete the verification, and then choose **VERIFY** to proceed.

1. Open a new tab and navigate to **Outlook** by entering the following URL:

   ```
   https://outlook.office.com
   ```

1. Sign in with your lab credentials if prompted.

1. In your inbox, look for the **Freshworks verification email**.

   > **Note:** If you are unable to locate the email from Freshworks, wait a few minutes as there might be a delay in email delivery. Also check your spam or junk folder.

1. Open the email. Depending on the email you received, follow **one** of the paths below:

   **Path A - Verification Code (most common):**

   1. Copy the **six-digit verification code** from the email.

   1. Go back to the Freshworks sign-up tab and enter the code in the **Enter your verification code** fields.

   1. Complete the CAPTCHA verification by selecting the required images, and then click **VERIFY**.

   1. Enter the password **<inject key="AzureAdUserPassword"></inject>** in the **Password** field, and then click **Start my trial**.

   **Path B - Activation Link:**

   > **Note:** If you received an activation link instead of a verification code, follow these steps.

   1. In the email, click **Activate Account**.

   1. On the activation page, enter **<inject key="AzureAdUserPassword"></inject>** in both the **Enter password** and **Confirm password** fields.

   1. Click **Activate your account**.

1. On the personalization page, confirm **Software and Internet** as the industry, select **I'm trying customer service software for the first time**, and then click **Next**.

1. Wait for the Freshdesk portal to load. You should now be logged in to your Freshdesk dashboard.

### Step 2: Retrieve API Key and Account URL

1. Once logged into the Freshdesk portal, click on the **Profile** icon in the top-right corner.

1. Select **Profile settings** from the dropdown menu.

1. In the profile page, scroll down and click **View API Key**.

   > **Note:** If you're unable to find this option, minimize the screen size using **Ctrl + -** to zoom out.

1. In the next pane, complete the **CAPTCHA** verification.

1. Once verified, you'll see your API Key displayed.

1. **Copy the API Key** and paste it into a Notepad file for safekeeping.

   > **Important:** You will need this API Key to connect Copilot Studio to Freshdesk in the next challenge.

1. From the browser address bar, copy the **Account URL**.

1. The URL format is typically as follows:
   ```
   https://your-company-name.freshdesk.com
   ```

1. **Copy this full URL** and paste it into the same Notepad file alongside your API Key.

1. Your Notepad should now contain something like the following:
   ```
   Account URL: https://cloudlabssandboxonmicrosoft<numeric>.freshdesk.com
   API Key: [Your API Key Here]
   ```

## Success Criteria
- Setup Freshdesk Free Trial Account
- Retrieve API Key and Account URL

## Additional Resources
- [Freshdesk Documentation](https://support.freshdesk.com/)
- [Freshdesk API Overview](https://developers.freshdesk.com/api/)
- [Freshdesk Getting Started Guide](https://freshdesk.com/resources/getting-started)

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g18.png)
