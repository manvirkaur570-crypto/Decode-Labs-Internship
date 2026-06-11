print("Welcome to Simple Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I am fine, thank you.")

    elif user_input == "your name":
        print("Bot: I am a simple chatbot.")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")