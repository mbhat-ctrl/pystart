import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def chat_with_groq(user_message: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

def main():
    print("Welcome! Ask me anything. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if not user_input:
            continue
        response = chat_with_groq(user_input)
        print(f"\nGroq: {response}\n")

if __name__ == "__main__":
    main()
