import random

responses = {
    "hello": ["Hello! How can I help you?", "Hi there!", "Hey!"],
    "ai": ["AI stands for Artificial Intelligence.", "AI is the simulation of human intelligence in machines."],
    "robotics": ["Robotics combines AI, engineering, and mechanics to build intelligent machines."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"]
}

print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input:
        print("Bot:", random.choice(responses["hello"]))

    elif "ai" in user_input:
        print("Bot:", random.choice(responses["ai"]))

    elif "robot" in user_input:
        print("Bot:", random.choice(responses["robotics"]))

    elif "bye" in user_input:
        print("Bot:", random.choice(responses["bye"]))
        break

    else:
        print("Bot: I am still learning. Please ask something else.")
