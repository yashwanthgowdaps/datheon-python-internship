# Task 4: Basic Rule-Based Chatbot
# Datheon Python Programming Internship

import random
from datetime import datetime


def chatbot_response(user_input):
    """Generate responses using predefined rules."""

    message = user_input.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "good morning",
                   "good afternoon", "good evening"]:
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you?"
        ])

    # Chatbot name
    elif message in ["name", "what is your name",
                     "what's your name", "who are you"]:
        return "My name is PyBot. I am a rule-based chatbot."

    # How are you?
    elif "how are you" in message:
        return "I am doing well! Thank you for asking."

    # Time
    elif message in ["time", "what is the time",
                     "what time is it"]:
        return "Current time: " + datetime.now().strftime("%I:%M %p")

    # Date
    elif message in ["date", "what is the date",
                     "what is today's date", "today's date"]:
        return "Today's date: " + datetime.now().strftime("%d-%m-%Y")

    # Help
    elif message == "help":
        return (
            "Here are some things you can ask me:\n"
            "- Say hello or hi\n"
            "- Ask my name\n"
            "- Ask how I am\n"
            "- Ask for the time\n"
            "- Ask for today's date\n"
            "- Say thank you\n"
            "- Type bye to exit"
        )

    # Thanks
    elif "thank" in message:
        return "You're welcome! Happy to help."

    # Simple conversation
    elif "your favourite colour" in message:
        return "I like blue! What is your favourite colour?"

    elif "i am fine" in message or "i'm fine" in message:
        return "That's great to hear!"

    elif "what can you do" in message:
        return "I can respond to greetings, tell the date and time, and answer simple questions."

    # Exit commands
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    # Unknown message
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    """Run the chatbot."""

    print("=" * 40)
    print("       WELCOME TO PYBOT")
    print("=" * 40)
    print("I am a simple rule-based chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to end the conversation.")

    while True:
        user_input = input("\nYou: ").strip()

        # Handle empty input
        if user_input == "":
            print("PyBot: Please enter a message.")
            continue

        response = chatbot_response(user_input)
        print("PyBot:", response)

        # End the conversation
        if user_input.lower().strip() in [
            "bye", "goodbye", "exit", "quit"
        ]:
            break

    print("\nChatbot session ended. Thank you!")


if __name__ == "__main__":
    main()
  
