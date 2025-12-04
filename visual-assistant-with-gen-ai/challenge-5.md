# Challenge 05: Deploy Foundry Resource and GPT-4.1-Mini Model  

## Introduction
With the surface defect model successfully predicting image anomalies, Contoso now wants to generate natural-language inspection commentary using Generative AI.  
To support this, you will deploy an **Azure Foundry resource** and configure a **GPT-4.1-Mini** model endpoint. This model will later receive defect prediction results and generate human-readable inspection summaries.

## Challenge Objectives
- Deploy an Azure Foundry resource.  
- Deploy the **GPT-4.1-Mini** model inside the Foundry workspace.  
- Record endpoint and key details for later integration.

## Steps to Complete
1. In the Azure Portal, search for **Foundry** and click **Create**.
2. Configure the resource using the values below:  
   - **Subscription:** Use your sandbox subscription.  
   - **Resource Group:** **challenge-rg-<inject key="DeploymentID"></inject>** 
   - **Name:** **surface-detection-<inject key="DeploymentID"></inject>**
   - **Region:** <inject key="Region"></inject> 
   - **Default Project Name:** `surface-detection-project`  
3. Click **Review + Create**, then **Create**.
4. After deployment completes, navigate to the **Foundry Portal**.
5. From the left-hand menu, select **Models + Endpoints**.
6. Click **Create Deployment** or **Deploy Base Model**.
7. From the model list, choose **gpt-4.1-mini**.
8. Configure deployment settings:  
   - **Deployment Type:** `Global Standard`  
   - **Rate Limit:** `20K TPM`  
9. Click **Deploy** and wait for the deployment to complete.
10. Once deployed, collect the following from the deployment details:  
    - **Model Deployment Name**  
    - **AZURE_OPENAI_ENDPOINT**  
    - **AZURE_OPENAI_KEY**
11. Save all three values in a notepad — they will be required for the application integration challenge.

## Success Criteria
- The Foundry resource is deployed successfully.  
- A **GPT-4.1-Mini** model deployment is created and active.  
- Deployment name, endpoint, and key are recorded for later use.

## Additional Resources
- [Azure Foundry Overview](https://learn.microsoft.com/azure/)  
- [Deploy Models in Foundry](https://learn.microsoft.com/azure/ai-services/openai/how-to/deploy-models)

---

Now, click **Next** to continue to **Challenge 06: Generate Inspection Commentary Using GPT-4.1-Mini**.
