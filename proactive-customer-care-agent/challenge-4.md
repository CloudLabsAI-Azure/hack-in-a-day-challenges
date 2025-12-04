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

1. In your **Customer Care Copilot**, click **Topics** in the left navigation pane.

2. You'll see existing system topics (Conversation Start, Fallback, Error).

3. Click **+ Add** or **+ New topic** at the top.

4. Select **Create from description with Copilot** (or similar option for AI-generated topics).

### Step 2: Create Topic 1 - Order Tracking Assistance

1. In the topic creation dialog, enter the following:

    - **Name:** `OrderTrackingAssistance`
    - **Description:**

    ```
    Help customers track their orders and provide delivery status updates. Ask the customer for their order number and save it as a variable. Use generative answers to retrieve order status information from the uploaded knowledge sources whenever possible. Provide estimated delivery dates, current shipping status, and tracking links. After sharing the tracking information, ask the customer whether they need additional assistance. If the customer reports an issue with tracking or needs human support, offer to create a support ticket. When creating the ticket, generate a subject line such as "Order Tracking Request - <order number>" and create a detailed description that includes the order number and any specific concerns raised by the customer. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should act as a self-service order tracking helper that uses the knowledge base first and escalates to ticket creation only when needed.
    ```

2. Click **Create** or **Generate**.

3. Wait for the AI to generate the topic (15-30 seconds).

4. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "Track my order"
     - "Where is my package"
     - "Order status"
     - "Delivery tracking"
     - "Track shipment"

5. Review the conversation flow:
   - Should ask for order number and save as variable
   - Should provide tracking information using knowledge base
   - Should ask if issue is resolved
   - Should offer escalation to ticket creation

6. Click **Save** to keep this topic.

### Step 3: Create Topic 2 - Product Return Processing

1. Click **+ Add** → **Create from description with Copilot**.

2. Enter the following:

    - **Name:** `ProductReturnProcessing`
    - **Description:**

        ```
        Assist customers who want to return or exchange products. Ask the customer for their order number and save it as a variable, then ask them to describe the reason for the return and save that as another variable. Use generative answers to provide return policy information, return windows, refund timelines, and return shipping instructions by referring to the uploaded knowledge sources. Provide step-by-step guidance for initiating returns through the customer portal or by mail. After sharing the return process, ask the customer whether they understand the steps or need help proceeding. If the customer requests assistance with processing the return or has questions about eligibility, offer to create a support ticket. When creating the ticket, generate a subject line using the order number, for example "Product Return Request - <order number>," and generate a detailed description that includes the order number and the reason for return provided by the customer. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should handle all return and exchange requests but escalate to human agents when customer needs assistance with processing.
        ```

3. Click **Create** or **Generate**.

4. Review and customize:

   - **Trigger phrases:** Verify phrases like:
     - "I want to return a product"
     - "Return my order"
     - "Exchange item"
     - "Refund request"
     - "Return policy"

5. Review the conversation flow:
   - Should ask for order number and save as variable
   - Should ask for return reason and save as variable
   - Should provide return policy information using knowledge base
   - Should ask if customer needs assistance
   - Should offer ticket creation with order number in subject

6. Click **Save**.

### Step 4: Create Topic 3 - Delivery Delay Management

1. Click **+ Add** → **Create from description with Copilot**.

2. Enter the following:

    - **Name:** `DeliveryDelayManagement`
    - **Description:**

        ```
        Help customers who are experiencing delayed deliveries or missed delivery windows. Ask the customer for their order number and save it as a variable, then ask them to describe the delivery issue in their own words and save that as another variable. Use generative answers to provide information about common delivery delays, carrier issues, weather impacts, and estimated resolution times by referring to the uploaded knowledge sources. Provide troubleshooting steps such as checking tracking status, verifying delivery address, contacting the carrier, or scheduling redelivery. After providing assistance, ask the customer whether the issue is resolved or if they need further help. If the customer indicates the delay is unacceptable or requests compensation, offer to create a support ticket for priority handling. When creating the ticket, generate a subject line such as "Delivery Delay - <order number>" and create a detailed description that includes the order number, delivery issue details, and customer concerns. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should provide self-service solutions for delivery issues but escalate to human agents when customers need priority assistance or compensation.
        ```

3. Click **Create** or **Generate**.

4. Review and customize:
   - **Trigger phrases:** Verify phrases like:
     - "My delivery is late"
     - "Order not delivered"
     - "Delayed shipment"
     - "Package not arrived"
     - "Missed delivery"

5. Review the conversation flow:
   - Should ask for order number and save as variable
   - Should ask about delivery issue and save as variable
   - Should provide delay information using knowledge base
   - Should ask if issue is resolved
   - Should offer ticket creation with order number in subject

6. Click **Save**.

### Step 5: Create Topic 4 - Service Quality Complaint Handling

1. Click **+ Add** → **Create from description with Copilot**.

2. Enter the following:

    - **Name:** `ServiceQualityComplaintHandling`
    - **Description:**

        ```
        Handle customer complaints about service quality, product defects, poor customer service experiences, or other issues. Begin by asking the customer to describe their complaint or concern in detail and save this as a variable. Ask if the complaint is related to a specific order, and if yes, ask for the order number and save it as another variable. Use generative answers to acknowledge the complaint empathetically and provide relevant company policies, quality standards, or resolution processes from the uploaded knowledge sources. Offer immediate solutions such as replacement, refund, discount codes, or service credits when appropriate based on knowledge base guidance. After presenting potential solutions, ask the customer whether they are satisfied with the proposed resolution. If the customer is not satisfied or requests to escalate the complaint to management, offer to create a priority support ticket. When creating the ticket, generate a subject line such as "Service Quality Complaint - <order number if provided, otherwise Customer Concern>" and create a detailed description that includes all complaint details, order information if applicable, and resolution attempts already made. Map these values to the CustomerServiceFlow inputs for Subject and Description so the flow receives the correct variables. This topic should handle complaints professionally with empathy while offering immediate solutions, and escalate to human agents only when the customer is not satisfied with automated resolution options.
        ```

3. Click **Create** or **Generate**.

4. Review and customize:
   - **Trigger phrases:** Verify phrases like:
     - "I have a complaint"
     - "Poor service"
     - "Product quality issue"
     - "Unsatisfied with service"
     - "Speak to manager"
     - "File a complaint"

5. Review the conversation flow:
   - Should ask for complaint details and save as variable
   - Should ask for order number if applicable and save as variable
   - Should provide empathetic response and solutions using knowledge base
   - Should ask if customer is satisfied
   - Should offer ticket creation for escalation

6. Click **Save**.

### Step 6: Review All Topics

1. In the **Topics** list, verify you now have 4 custom topics:
   - OrderTrackingAssistance
   - ProductReturnProcessing
   - DeliveryDelayManagement
   - ServiceQualityComplaintHandling

2. Ensure all topics are **enabled** (toggle should be on).

### Step 7: Connect Topics to CustomerServiceFlow

Now connect each topic to your published **CustomerServiceFlow**. The AI-generated topics should already have the conversation flow with variables captured. You'll add the action to call the CustomerServiceFlow when escalation is needed.

#### For OrderTrackingAssistance Topic:

1. Open **OrderTrackingAssistance** topic in the editor.

2. Locate the point in the conversation where the customer indicates they need assistance (after providing tracking information).

3. At that escalation point, add a new node:
   - Click **+** → **Call an action** → Select **CustomerServiceFlow** flow.

4. Map the flow inputs using the variables captured in the topic:
   - **Subject:** `"Order Tracking Request - " & Topic.OrderNumber`
   - **Description:** `"Customer needs assistance with order tracking. Order Number: " & Topic.OrderNumber & ". Additional details: " & Topic.TrackingIssue`

   > **Note:** Variable names may differ based on AI generation. Use the actual variable names from your generated topic (e.g., `Topic.ordernumber`, `Topic.OrderNum`, etc.).

5. After the flow action, add a **Message** node:
   - Type: `"I've created a support ticket for your order tracking request. Our customer service team will contact you shortly with an update."`

6. Save the topic.

#### For ProductReturnProcessing Topic:

1. Open **ProductReturnProcessing** topic.

2. Locate the point where the customer requests assistance with processing the return.

3. Add **Call an action** node at the escalation point → Select **CustomerServiceFlow**.

4. Map inputs using the variables captured in the topic:
   - **Subject:** `"Product Return Request - " & Topic.OrderNumber`
   - **Description:** `"Customer requesting return assistance. Order Number: " & Topic.OrderNumber & ". Return Reason: " & Topic.ReturnReason`

   > **Note:** Use the actual variable names from your generated topic.

5. Add a **Message** node:
   - Type: `"I've created a priority support ticket for your delivery issue. Our logistics team will investigate and contact you shortly."`

6. Save the topic.

#### For ServiceQualityComplaintHandling Topic:

1. Open **ServiceQualityComplaintHandling** topic.

2. Locate the point where the customer is not satisfied or requests escalation.

3. Add **Call an action** node → Select **Customer Service Request** flow.

4. Map inputs using the variables captured in the topic:
   - **Subject:** `"Service Quality Complaint - " & Topic.OrderNumber`
   - **Description:** `"Customer complaint regarding service quality. Order Number: " & Topic.OrderNumber & ". Complaint Details: " & Topic.ComplaintDetails`

   > **Note:** Use the actual variable names from your generated topic. If no order number, use a generic identifier.

5. Add a **Message** node:
   - Type: `"I've escalated your complaint to our management team. A senior customer service representative will contact you shortly to address your concerns."`

6. Save the topic.

### Step 8: Test Topics with Flow Integration

1. Open the **Test your copilot** pane.

2. Test **OrderTrackingAssistance** topic:
   - Type: "Track my order"
   - Provide order number when asked
   - Review the tracking information
   - Indicate you need assistance
   - Verify ticket creation confirmation message

3. Test **ProductReturnProcessing** topic:
   - Type: "I want to return a product"
   - Provide order number
   - Describe return reason
   - Request assistance with processing
   - Verify ticket is created with order number in subject

4. Test **DeliveryDelayManagement** topic:
   - Type: "My delivery is late"
   - Provide order number
   - Describe the delay issue
   - Indicate issue is not resolved
   - Verify ticket is created with order number in subject

5. Test **ServiceQualityComplaintHandling** topic:
   - Type: "I have a complaint"
   - Describe the complaint
   - Provide order number if asked
   - Indicate not satisfied with resolution
   - Verify ticket is created for escalation

6. For each test, ensure:
   - Topic triggers correctly
   - Variables are captured properly
   - Knowledge base information is provided
   - Flow is called with proper inputs when escalated
   - Confirmation message is displayed

## Success Criteria
- Created 4 topics using generative AI (OrderTrackingAssistance, ProductReturnProcessing, DeliveryDelayManagement, ServiceQualityComplaintHandling)
- All topics have relevant trigger phrases configured
- Topics capture customer input in variables (order numbers, issues, complaints, etc.)
- Connected each topic to your Customer Service Request flow via "Call an action"
- Mapped flow inputs (Subject and Description) correctly using topic variables
- Test pane successfully creates tickets through topics with dynamic subject lines
- Confirmation messages are displayed to customers

## Additional Resources
- [Create topics with Copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)
- [Use generative AI for topic creation](https://learn.microsoft.com/microsoft-copilot-studio/nlu-authoring)
- [Call flows from topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-call-action)

---

Now, click **Next** to continue to **Challenge 05: Test Your Customer Care Copilot End-to-End**.
