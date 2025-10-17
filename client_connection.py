import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_KEY")

if not api_key:
    raise ValueError("API key not found.")

client = anthropic.Anthropic(api_key=api_key)
messages = []

def chat_with_claude(user_input):
    # Append user message to conversation history
    messages.append({"role": "user", "content": user_input})

    # Call Claude API
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens = 1024,
        system="You are a helpful assistant.",
        messages=messages
    )

    # Get Claude's reply
    assistant_reply = response.content[0].text

    # Append assistant's reply to conversation history
    messages.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

# Terminal loop for multiturn conversation
print("Chat with Claude! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Ending conversation.")
        break
    reply = chat_with_claude(user_input)
    print("Claude:", reply)
