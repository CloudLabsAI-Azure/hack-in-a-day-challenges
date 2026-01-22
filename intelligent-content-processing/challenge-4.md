# Challenge 04: Human-in-the-Loop (HITL) Validation with Queue Storage

## Introduction

AI systems are powerful but not always 100% accurate.
In enterprise environments, **low-confidence AI results must be reviewed by humans** to ensure quality, compliance, and trust.

In this challenge, participants will implement a **Human-in-the-Loop (HITL)** workflow using **Azure Queue Storage**, where documents with low confidence are routed for manual review before final approval.

## Challenge Objectives

* Create an **Azure Queue Storage** queue for human review.
* Route low-confidence documents to the queue.
* Simulate a **human validation step**.
* Update document status based on human approval.
* Complete the AI + human collaboration loop.

## Steps to Complete

### Create Azure Queue Storage

1. In the **Azure Portal**, open your existing **Storage account**.

2. In the left menu, select **Queues**.

3. Click **+ Queue**.

4. Provide:

   * **Name:** `human-review-queue`

5. Click **Create**.

### Identify Documents for Human Review

6. From **Challenge 03**, review your processed JSON documents.

7. Apply the confidence rule:

   * If `confidence < 0.85` → send to human review
   * Otherwise → skip HITL

8. Identify at least one document with **low confidence** (e.g., handwritten note).

    Reminder example:

    ```json
    {
    "id": "doc-002",
    "confidence": 0.78,
    "status": "PENDING"
    }
    ```

### Add a Message to the Queue (Simulated)

9. Open the `human-review-queue`.

10. Click **+ Add message**.

11. Paste the following JSON (update values if needed):

    ```json
    {
    "documentId": "doc-002",
    "documentType": "Patient Note",
    "confidence": 0.78,
    "reason": "Low confidence extraction"
    }
    ```

12. Click **OK**.

---

### Simulate Human Review

13. View the message in the queue.

14. Assume a human reviews the document and confirms the data is correct.

15. Update the document JSON locally by changing:

* `status` → `APPROVED`
* Optionally increase confidence

    Example:

    ```json
    {
    "id": "doc-002",
    "documentType": "HandwrittenNote",
    "referenceId": "John Doe",
    "amount": 0,
    "currency": "",
    "confidence": 0.90,
    "status": "APPROVED"
    }
    ```

### Remove Message from Queue

16. After “human approval,” delete the message from the queue.

    - This simulates:

        > “Human has completed review.”

### Success Criteria

You have successfully completed the Challenge 4:

* Queue Storage is created
* Low-confidence document is added to the queue
* Human review is simulated
* Document status is updated to APPROVED

### Additional Resources

- [Azure Queue Storage – Overview](https://learn.microsoft.com/azure/storage/queues/storage-queues-introduction)

- [Create and Manage Azure Queues (Azure Portal)](https://learn.microsoft.com/azure/storage/queues/storage-quickstart-queues-portal)

- [Designing Message-Based Workflows in Azure](https://learn.microsoft.com/azure/architecture/guide/architecture-styles/message-based)

- [Human-in-the-Loop Patterns for AI Systems](https://learn.microsoft.com/azure/architecture/guide/ai/human-in-the-loop)

Now, click **Next** to continue to **Challenge 05**.
