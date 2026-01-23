"""
Secure AI Chatbot - Using Managed Identity (No API Keys!)
This app demonstrates passwordless authentication to Azure OpenAI
"""

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI
import sys

def main():
    print("=" * 70)
    print("🔒 SECURE AI CHATBOT - Managed Identity Authentication")
    print("=" * 70)
    
    # Initialize managed identity
    print("\n🔐 Authenticating with Managed Identity...")
    credential = DefaultAzureCredential()
    
    # Connect to Key Vault
    kv_name = "kv-secureai-2036950"  # Replace with your Key Vault name
    kv_url = f"https://{kv_name}.vault.azure.net"
    
    print(f"🔑 Retrieving secrets from Key Vault: {kv_name}")
    secret_client = SecretClient(vault_url=kv_url, credential=credential)
    
    try:
        # Get configuration from Key Vault (no hardcoded values!)
        openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value
        deployment_name = secret_client.get_secret("OpenAIDeployment").value
        api_version = secret_client.get_secret("OpenAIApiVersion").value
        
        print(f"✅ Endpoint: {openai_endpoint}")
        print(f"✅ Deployment: {deployment_name}")
        print(f"✅ API Version: {api_version}")
        
    except Exception as e:
        print(f"❌ Error retrieving secrets: {e}")
        print("Make sure:")
        print("  1. You're running on the VM with managed identity")
        print("  2. Managed identity has 'Key Vault Secrets User' role")
        print("  3. Key Vault name is correct")
        sys.exit(1)
    
    # Create OpenAI client with managed identity token
    print("\n🤖 Initializing OpenAI client with managed identity...")
    
    try:
        client = AzureOpenAI(
            azure_endpoint=openai_endpoint,
            api_version=api_version,
            azure_ad_token_provider=lambda: credential.get_token(
                "https://cognitiveservices.azure.com/.default"
            ).token
        )
        print("✅ OpenAI client ready (using managed identity - no API key!)")
        
    except Exception as e:
        print(f"❌ Error creating OpenAI client: {e}")
        sys.exit(1)
    
    # Chat loop
    print("\n" + "=" * 70)
    print("💬 Chat started! Type 'exit' or 'quit' to end the conversation.")
    print("=" * 70 + "\n")
    
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Call OpenAI
        try:
            print("AI: ", end="", flush=True)
            
            response = client.chat.completions.create(
                model=deployment_name,
                messages=conversation_history,
                temperature=0.7,
                max_tokens=500
            )
            
            assistant_message = response.choices[0].message.content
            print(assistant_message + "\n")
            
            # Add assistant response to history
            conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
        except Exception as e:
            print(f"\n❌ Error calling OpenAI: {e}")
            print("Make sure:")
            print("  1. Managed identity has 'Cognitive Services OpenAI User' role")
            print("  2. OpenAI resource is accessible from your network")
            print("  3. Model deployment exists and is running")
            break

if __name__ == "__main__":
    main()
