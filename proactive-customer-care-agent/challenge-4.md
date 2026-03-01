# Challenge 04: Create Topics Using Generative AI

## Introduction
Instead of manually building conversation flows from scratch, Microsoft Copilot Studio allows you to create topics using generative AI. Simply describe what you want the topic to do, and AI will generate the conversation flow, trigger phrases, and responses automatically. You'll then connect these topics to your CustomerServiceFlow for ticket escalation.

In this challenge, you will create 4 essential customer care topics using generative AI: Order Tracking Assistance, Product Return Processing, Delivery Delay Management, and Service Quality Complaint Handling. Each topic will call your published CustomerServiceFlow when escalation is needed.

## Challenge Objectives
- Use Copilot Studio's generative AI to create 4 topics
- Connect each topic to your published CustomerServiceFlow
- Map topic variables to flow inputs
- Test topics with flow integration

## Steps to Complete

### Step 1: Navigate to Topics Section

1. In your **Customer Care Copilot Agent**, click **Topics** in the navigation pane.

1. You'll see existing system topics (Conversation Start, Fallback, Error).

1. Click **+ Add a topic**.

1. Select **Add from description with Copilot**.

### Step 2: Create Topic 1 - Order Tracking Assistance

1. In the topic creation dialog, enter the following details:

   - **Name:** `OrderTrackingAssistance`
   - **Description:**

      ```
      Help customers track their orders and provide delivery status updates. Ask the customer for their order number and save it as a variable. Use generative answers to retrieve order status information from the uploaded knowledge sources whenever possible. Provide estimated delivery dates, current shipping status, and tracking links. After sharing the tracking information, ask the customer whether they need additional assistance. If the customer reports an issue with tracking or needs human support, offer to create a support ticket. When creating the ticket, generate a subject line such as "Order Tracking Request - <order number>" and create a detailed description that includes the order number and any specific concerns raised by the customer. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should act as a self-service order tracking helper that uses the knowledge base first and escalates to ticket creation only when needed.
      ```

1. Click on **Create**.

1. Wait for the AI to generate the topic (15-30 seconds).

1. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "Track my order"
     - "Where is my package"
     - "Order status"
     - "Delivery tracking"
     - "Track shipment"

1. Review the conversation flow:
   - Should ask for order number and save as variable
   - Should provide tracking information using knowledge base
   - Should ask if issue is resolved
   - Should offer escalation to ticket creation

1. **Important:** If you see an error about limited scope or variables:
   - Open the **Variables** pane.
   - Click on each variable under **Topic**.
   - Enable the both the checkbox for **Receive values from other topics** or **Return values to original topics** for Variables which shows error.

1. Click **Save** to keep this topic.

### Step 3: Create Topic 2 - Product Return Processing

1. Click **+ Add a topic**.

1. Select **Add from description with Copilot**.

1. Enter the following details:

    - **Name:** `ProductReturnProcessing`
    - **Description:**

        ```
        Assist customers who want to return or exchange products. Ask the customer for their order number and save it as a variable, then ask them to describe the reason for the return and save that as another variable. Use generative answers to provide return policy information, return windows, refund timelines, and return shipping instructions by referring to the uploaded knowledge sources. Provide step-by-step guidance for initiating returns through the customer portal or by mail. After sharing the return process, ask the customer whether they understand the steps or need help proceeding. If the customer requests assistance with processing the return or has questions about eligibility, offer to create a support ticket. When creating the ticket, generate a subject line using the order number, for example "Product Return Request - <order number>," and generate a detailed description that includes the order number and the reason for return provided by the customer. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should handle all return and exchange requests but escalate to human agents when customer needs assistance with processing.
        ```

1. Click **Create** or **Generate**.

1. Review and customize the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
   - "I want to return a product"
   - "Return my order"
   - "Exchange item"
   - "Refund request"
   - "Return policy"

1. Review the conversation flow:
   - Should ask for order number and save as variable
   - Should ask for return reason and save as variable
   - Should provide return policy information using knowledge base
   - Should ask if customer needs assistance
   - Should offer ticket creation with order number in subject

1. **Important:** If you see an error about limited scope or variables:
   - Open the **Variables** pane.
   - Click on each variable under **Topic**.
   - Enable the both the checkbox for **Receive values from other topics** or **Return values to original topics** for Variables which shows error.

1. Click **Save**.

### Step 4: Create Topic 3 - Delivery Delay Management

1. Click **+ Add a topic**.

1. Select **Add from description with Copilot**.

1. Enter the following details:

   - **Name:** `DeliveryDelayManagement`
   - **Description:**

      ```
      Help customers who are experiencing delayed deliveries or missed delivery windows. Ask the customer for their order number and save it as a variable, then ask them to describe the delivery issue in their own words and save that as another variable. Use generative answers to provide information about common delivery delays, carrier issues, weather impacts, and estimated resolution times by referring to the uploaded knowledge sources. Provide troubleshooting steps such as checking tracking status, verifying delivery address, contacting the carrier, or scheduling redelivery. After providing assistance, ask the customer whether the issue is resolved or if they need further help. If the customer indicates the delay is unacceptable or requests compensation, offer to create a support ticket for priority handling. When creating the ticket, generate a subject line such as "Delivery Delay - <order number>" and create a detailed description that includes the order number, delivery issue details, and customer concerns. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should provide self-service solutions for delivery issues but escalate to human agents when customers need priority assistance or compensation.
      ```

1. Click **Create** or **Generate**.

1. Review and customize the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
   - "My delivery is late"
   - "Order not delivered"
   - "Delayed shipment"
   - "Package not arrived"
   - "Missed delivery"

1. Review the conversation flow:
   - Should ask for order number and save as variable
   - Should ask about delivery issue and save as variable
   - Should provide delay information using knowledge base
   - Should ask if issue is resolved
   - Should offer ticket creation with order number in subject

1. **Important:** If you see an error about limited scope or variables:
   - Open the **Variables** pane.
   - Click on each variable under **Topic**.
   - Enable the both the checkbox for **Receive values from other topics** or **Return values to original topics** for Variables which shows error.

1. Click on **Save**.

### Step 5: Create Topic 4 - Service Quality Complaint Handling

1. Click **+ Add a topic**.

1. Select **Add from description with Copilot**.

1. Enter the following details:

   - **Name:** `ServiceQualityComplaintHandling`
   - **Description:**

      ```
      Handle customer complaints about service quality, product defects, poor customer service experiences, or other issues. Begin by asking the customer to describe their complaint or concern in detail and save this as a variable. Ask if the complaint is related to a specific order, and if yes, ask for the order number and save it as another variable. Use generative answers to acknowledge the complaint empathetically and provide relevant company policies, quality standards, or resolution processes from the uploaded knowledge sources. Offer immediate solutions such as replacement, refund, discount codes, or service credits when appropriate based on knowledge base guidance. After presenting potential solutions, ask the customer whether they are satisfied with the proposed resolution. If the customer is not satisfied or requests to escalate the complaint to management, offer to create a priority support ticket. When creating the ticket, generate a subject line such as "Service Quality Complaint - <order number if provided, otherwise Customer Concern>" and create a detailed description that includes all complaint details, order information if applicable, and resolution attempts already made. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should handle complaints professionally with empathy while offering immediate solutions, and escalate to human agents only when the customer is not satisfied with automated resolution options.
      ```

1. Click **Create** or **Generate**.

1. Review and customize the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
   - "I have a complaint"
   - "Poor service"
   - "Product quality issue"
   - "Unsatisfied with service"
   - "Speak to manager"
   - "File a complaint"

1. Review the conversation flow:
   - Should ask for complaint details and save as variable
   - Should ask for order number if applicable and save as variable
   - Should provide empathetic response and solutions using knowledge base
   - Should ask if customer is satisfied
   - Should offer ticket creation for escalation

1. **Important:** If you see an error such as **PowerFxError** or a limited scope issue:
   - Click the ellipsis (**...**) on the affected node.
   - Select **Delete**.

1. Click on **Save**.

### Step 6: Review All Topics

1. In the **Topics** list, verify you now have 4 custom topics:

   - OrderTrackingAssistance
   - ProductReturnProcessing
   - DeliveryDelayManagement
   - ServiceQualityComplaintHandling

1. Ensure all topics are **enabled** (toggle should be on).

### Step 7: Connect Topics to CustomerServiceFlow

Now connect each topic to your published **CustomerServiceFlow**. The AI-generated topics should already have the conversation flow with variables captured. You'll add the action to call the CustomerServiceFlow when escalation is needed.

#### Connect OrderTrackingAssistance Topic to Flow:

1. Open **OrderTrackingAssistance** topic in the editor.

1. Navigate through the topic flow and find the appropriate place where escalation to ticket creation should happen.

1. Add the **CustomerServiceFlow** tool immediately after the message where you inform the user that a support ticket will be created:
   - Click the **+** icon.
   - Select **Add a tool**.
   - Select **CustomerServiceFlow**.

1. Map the flow inputs using the **(...)** icon:
   - **Subject:** Select the appropriate variable from your topic
   - **Description:** Select the relevant variables that capture the tracking issue details

   > **Note:** If your topic doesn't have all the required variables, add **Question** nodes to collect missing information before calling the flow.

1. Add a confirmation message after the flow action and click **Save**.

#### Connect ProductReturnProcessing Topic to Flow:

1. Open **ProductReturnProcessing** topic in the editor.

1. Navigate through the topic flow and find the appropriate place for ticket creation.

1. Add the **CustomerServiceFlow** tool immediately after the message where you inform the user that a support ticket will be created:
   - Click the **+** icon.
   - Select **Add a tool**.
   - Select **CustomerServiceFlow**.

1. Map the flow inputs using the (...) icon:
   - **Subject:** Select the appropriate variable from your topic
   - **Description:** Select the relevant variables about the return request

   > **Note:** If your topic doesn't capture all necessary information, add **Question** nodes to collect missing details before calling the flow.

1. Add a confirmation message after the flow action and click **Save**.

#### For DeliveryDelayManagement Topic:

1. Open **DeliveryDelayManagement** topic in the editor.

1. Locate the point where the customer indicates the issue is not resolved.

1. Delete any existing message node at the escalation point by clicking **three dots (...)** → **Delete**.

1. Click the **+** button, then select **Add a tool**.

1. Search for and select **CustomerServiceFlow** from the tool list.

1. Map the flow inputs using the (...) icon:
   - **Subject:** Select the delivery-related variable from your topic
   - **Description:** Select the variables that describe the delivery delay

   > **Note:** If your topic doesn't have the necessary variables, add **Question** nodes to gather the required information before calling the flow.

1. Add a confirmation message after the flow action and click **Save**.

#### Connect ServiceQualityComplaintHandling Topic to Flow:

1. Open **ServiceQualityComplaintHandling** topic in the editor.

1. Navigate through the topic flow and find the escalation point.

1. Add the **CustomerServiceFlow** tool immediately after the message where you inform the user that a support ticket will be created:
   - Click the **+** icon.
   - Select **Add a tool**.
   - Select **CustomerServiceFlow**.

1. Map the flow inputs using the (...) icon:
   - **Subject:** Select the complaint category variable from your topic
   - **Description:** Select the variables that capture the complaint details

   > **Note:** If your topic doesn't have the necessary variables, add **Question** nodes to gather the required information before calling the flow.

1. Add a confirmation message after the flow action and click **Save**.

<validation step="24fd297d-a83d-4d8c-bba8-4c73427a95f7" />
 
> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Created 4 topics using generative AI (OrderTrackingAssistance, ProductReturnProcessing, DeliveryDelayManagement, ServiceQualityComplaintHandling)
- All topics have relevant trigger phrases configured
- Topics capture customer input in variables (order numbers, issues, complaints, etc.)
- Connected each topic to your CustomerServiceFlow via "Call an action"
- Mapped flow inputs (Subject and Description) correctly using topic variables
- Test pane successfully creates tickets through topics with dynamic subject lines
- Confirmation messages are displayed to customers

## Additional Resources
- [Create topics with Copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)
- [Use generative AI for topic creation](https://learn.microsoft.com/microsoft-copilot-studio/nlu-authoring)
- [Call flows from topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-call-action)

---

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g20.png)
