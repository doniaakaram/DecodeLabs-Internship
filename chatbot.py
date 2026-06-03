print("AI Chatbot Started!")

responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing well!",
    "bye": "Goodbye!",
    "thanks": "You're welcome!",
    "what is your name": "I'm DecodeBot."
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    reply = responses.get(
        user_input,
        "I don't understand."
    )

    print("Bot:", reply)