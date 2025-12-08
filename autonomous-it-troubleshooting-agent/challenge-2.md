# Challenge 02: Setup Freshdesk & Get API Credentials

## Introduction
When the copilot cannot resolve an issue automatically, it needs to create a support ticket in your helpdesk system. Freshdesk is a popular cloud-based helpdesk solution that integrates seamlessly with Copilot Studio through its API connector.

In this challenge, you will activate your Freshdesk free trial, configure your account, and obtain the API credentials needed to connect Copilot Studio to Freshdesk for automated ticket creation.

## Challenge Objectives
- Activate Freshdesk free trial account
- Configure Freshdesk profile and settings
- Obtain API Key and Account URL
- Prepare credentials for Copilot Studio integration

## Steps to Complete

### Step 1: Start Freshdesk Free Trial

1. Open **Microsoft Edge** browser in your lab VM.

2. Navigate to **Freshworks Portal**:

   ```
   https://www.freshworks.com/freshdesk/
   ```

3. Click **Start free trial** to begin the free trial registration.

### Step 2: Provide Registration Details

1. In the registration pane, provide these details:

   - **First name:** `ODL`
   - **Last name:** `User`
   - **Work email:** <inject key="AzureAdUserEmail"></inject>
   - **Company name:** `Contoso`

2. Click **Try it free**.

### Step 3: Complete Setup Questions

1. In the next pane, provide these details:

   - **What industry are you from?:** From the list, select **Software and internet**
   - **How many employees are there in your company?:** Select **1-10**
   - Check the box: **I'm trying customer service software for the first time**

### Step 4: Activate Your Account via Email

1. Open a new tab and navigate to **Outlook**:

   ```
   https://outlook.office.com
   ```

2. Sign in with your lab credentials if prompted.

3. In your inbox, look for the **Freshworks verification email**.

   > **Note:** If you're unable to locate the activation email from Freshworks, please wait a few minutes, as there might be a delay in email delivery. Check your spam or junk folder as well.

4. Open the email and click **Activate Account**.

### Step 5: Set Your Password

1. In the activation pane, provide:

   - **Enter password:** Create a strong password (e.g., `Freshdesk@2025`)
   - **Confirm password:** Re-enter the same password

2. Click **Activate your account**.

3. Wait for the Freshdesk portal to load.

### Step 6: Access Profile Settings

1. Once logged into the Freshdesk portal, click on the **Profile** icon in the top-right corner.

2. Select **Profile settings** from the dropdown menu.

### Step 7: Retrieve API Key

1. In the profile page, scroll down and click **View API Key**.

   > **Note:** If you're unable to find this option, minimize the screen size using **Ctrl + -** to zoom out.

2. In the next pane, complete the **CAPTCHA** verification.

3. Once verified, you'll see your API Key displayed.

4. **Copy the API Key** and paste it into a Notepad file for safekeeping.

   > **Important:** You will need this API Key to connect Copilot Studio to Freshdesk in the next challenge.

### Step 8: Copy Account URL

1. From the browser address bar, copy the **Account URL**.

2. The URL format is typically:
   ```
   https://your-company-name.freshdesk.com
   ```

3. **Copy this full URL** and paste it into the same Notepad file alongside your API Key.

4. Your Notepad should now contain:
   ```
   Account URL: https://your-account.freshdesk.com
   API Key: [Your API Key Here]
   ```

## Success Criteria
- Freshdesk free trial successfully activated
- Account verified via email activation
- Profile settings accessed successfully
- API Key retrieved and saved securely
- Account URL copied and documented

## Additional Resources
- [Freshdesk Documentation](https://support.freshdesk.com/)  
- [Freshdesk API Overview](https://developers.freshdesk.com/api/)  
- [Freshdesk Getting Started Guide](https://freshdesk.com/resources/getting-started)

Now, click **Next** to continue to **Challenge 03: Create Freshdesk Ticket Flow**.
