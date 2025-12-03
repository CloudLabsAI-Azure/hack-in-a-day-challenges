# Challenge 01: Create Your IT Support Copilot in Copilot Studio

## Introduction
IT support teams at enterprises handle hundreds of repetitive requests daily—password resets, VPN connection issues, slow laptop complaints, and printer problems. Manual responses to these common issues consume 60-70% of helpdesk time, leading to long wait times and frustrated employees.

To solve this, your organization plans to implement an **AI-powered IT Support Copilot** using **Microsoft Copilot Studio**.  
This intelligent assistant will provide instant, 24/7 support by answering questions from knowledge base documents, guiding users through troubleshooting steps, and automatically notifying IT teams when issues are resolved.

In this challenge, you'll create the **IT Support Copilot** in Microsoft Copilot Studio — the foundation for your intelligent IT support solution.

## Accessing the Lab Environment

Please ensure you have access to the following resources:
- **Microsoft 365 Credentials:** `<inject key="AzureAdUserEmail"></inject>`
- **Password:** `<inject key="AzureAdUserPassword"></inject>`
- **Copilot Studio Portal:** [https://copilotstudio.microsoft.com](https://copilotstudio.microsoft.com)

## Challenge Objectives
- Create a new **Copilot** in Microsoft Copilot Studio.
- Configure copilot identity, description, and conversation starters.
- Test basic conversation flow and verify system topics are active.
- Understand the copilot authoring interface and navigation.

## Steps to Complete

### Step 1: Sign in to Microsoft Copilot Studio
1. Open **Microsoft Edge** browser in your lab VM.
2. Navigate to **Microsoft Copilot Studio**: `https://copilotstudio.microsoft.com`
3. Click **Sign in**.
4. Enter the provided credentials:
   - **Email/Username:** `<inject key="AzureAdUserEmail"></inject>`
   - **Password:** `<inject key="AzureAdUserPassword"></inject>`
5. If prompted with **"Stay signed in?"**, click **No**.
6. Wait for the Copilot Studio home page to load.

### Step 2: Create a New Copilot
1. On the Copilot Studio home page, click **+ Create** in the left navigation pane.
2. Select **New copilot** from the options.
3. In the creation dialog, you may see options to describe your copilot or start from blank:
   - Choose **Skip to configure** or **Create from blank** to manually configure.

### Step 3: Configure Basic Copilot Settings
1. In the copilot configuration screen, provide the following details:
   - **Name:** `IT Support Copilot - <inject key="DeploymentID"></inject>`
   - **Description:** `Your intelligent assistant for common IT support issues including password resets, VPN problems, slow laptop troubleshooting, and printer issues`
   - **Language:** English (or your preferred language)
   - **Environment:** Select the default environment or **Dev-<inject key="DeploymentID"></inject>** if available
2. Click **Create** to initialize your copilot.
3. Wait for the copilot to be created (this may take 30-60 seconds).

### Step 4: Customize Copilot Icon and Identity
1. Once the copilot is created, you'll see the authoring canvas.
2. Click on **Settings** (gear icon) in the top-right corner.
3. Navigate to **Generative AI** section (if available) or **Details**.
4. Under **Icon** or **Avatar**, select an appropriate icon for IT support (e.g., headset, computer, or help icon).
5. Click **Save** to apply changes.

### Step 5: Add Conversation Starters
1. In the copilot authoring canvas, look for **Topics** in the left navigation.
2. Find the **Conversation Start** system topic or the main overview page.
3. Add **Conversation starters** (suggested prompts for users):
   - `I forgot my password`
   - `VPN not connecting`
   - `My laptop is running slow`
   - `Printer not working`
4. These will appear as buttons when users first interact with your copilot.
5. **Save** your changes.

### Step 6: Review Default System Topics
1. In the left navigation, click **Topics**.
2. You'll see several **System** topics that come pre-configured:
   - **Conversation Start** - Greets users when they first interact
   - **Fallback** - Handles questions the copilot doesn't understand
   - **Error** - Manages error scenarios gracefully
3. Click on **Conversation Start** to see how it's structured.
4. Notice the message nodes and flow logic—this is how copilot conversations are designed.
5. Keep these system topics **enabled** for now (toggle should be on).

### Step 7: Test Your Copilot
1. Look for the **Test your copilot** button or pane (usually on the right side or bottom-right corner).
2. Click to open the **Test** pane.
3. Type **"Hello"** in the test chat and press Enter.
4. Observe the copilot's response—it should greet you based on the Conversation Start topic.
5. Try typing **"What can you help me with?"**
6. The copilot should display the conversation starters you configured.
7. If the test pane works and responds, your copilot is functioning correctly.

### Step 8: Explore the Copilot Studio Interface
Take a moment to familiarize yourself with the interface:
- **Topics:** Where you create conversation flows
- **Entities:** Define data types (dates, numbers, custom values)
- **Actions:** Connect to Power Automate flows or APIs
- **Analytics:** (available after publishing) View usage metrics
- **Publish:** Deploy your copilot to channels like Teams, website, etc.
- **Settings:** Configure generative AI, authentication, and other options

## Success Criteria
✅ Microsoft Copilot Studio is accessible with provided credentials.  
✅ A new copilot named **IT Support Copilot - <inject key="DeploymentID"></inject>** is created.  
✅ Copilot has a description and appropriate IT support icon.  
✅ Four conversation starters are configured and visible.  
✅ Test pane shows the copilot responding to "Hello" and "What can you help me with?".  
✅ Default system topics (Conversation Start, Fallback, Error) are present and enabled.  

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)  
- [Create Your First Copilot](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-get-started)  
- [Conversation Design Best Practices](https://learn.microsoft.com/microsoft-copilot-studio/guidance/design-overview)  
- [System Topics Documentation](https://learn.microsoft.com/microsoft-copilot-studio/authoring-system-topics)

---

Now, click **Next** (bottom right corner) to continue to **Challenge 02: Upload IT Support Knowledge Base Documents**.