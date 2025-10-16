import anthropic

# Initialize Claude API client
client = anthropic.Anthropic(api_key="ANTHROPIC_KEY")

# Initialize conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat_with_claude(user_input):
    # Append user message to conversation history
    messages.append({"role": "user", "content": user_input})

    # Call Claude API
    response = client.messages.create(
        model="claude-3.5",
        messages=messages,
        max_tokens_to_sample=300
    )

    # Get Claude's reply
    assistant_reply = response["completion"]

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
