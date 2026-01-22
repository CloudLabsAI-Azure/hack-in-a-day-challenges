"""Debug message structure"""
import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import MessageRole
import json

load_dotenv()

project = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=os.getenv("AGENT_API_ENDPOINT")
)

# Create a quick test
thread = project.agents.threads.create()
project.agents.messages.create(
    thread_id=thread.id,
    role="user",
    content="SELECT * FROM employees WHERE ROWNUM <= 5;"
)

run = project.agents.runs.create_and_process(
    thread_id=thread.id,
    agent_id=os.getenv("AGENT_ID")
)

print(f"Run status: {run.status}")

messages_list = list(project.agents.messages.list(thread_id=thread.id))
print(f"\nTotal messages: {len(messages_list)}")

for i, msg in enumerate(messages_list):
    print(f"\n=== Message {i+1} ===")
    print(f"Role: {msg.role}")
    print(f"Role type: {type(msg.role)}")
    print(f"Is AGENT?: {msg.role == MessageRole.AGENT}")
    print(f"Content type: {type(msg.content)}")
    print(f"Content length: {len(msg.content) if msg.content else 0}")
    
    if msg.content:
        for j, content_item in enumerate(msg.content):
            print(f"\n  Content item {j+1}:")
            print(f"    Type: {type(content_item)}")
            if isinstance(content_item, dict):
                print(f"    Keys: {content_item.keys()}")
                print(f"    Content: {json.dumps(content_item, indent=6)[:300]}")
            else:
                print(f"    Has 'type' attr?: {hasattr(content_item, 'type')}")
                print(f"    Has 'text' attr?: {hasattr(content_item, 'text')}")
                if hasattr(content_item, 'type'):
                    print(f"    type: {content_item.type}")
                if hasattr(content_item, 'text'):
                    print(f"    text: {content_item.text}")
                    if hasattr(content_item.text, 'value'):
                        print(f"    text.value: {content_item.text.value[:100]}")
