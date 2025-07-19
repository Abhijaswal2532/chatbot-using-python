import random

def greet_user():
    greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
    print("🤖", random.choice(greetings), "Welcome to Smart Support Assistant!")

def get_user_query():
    return input("You: ").strip().lower()

def process_query(query):
    help_topics = {
        "greeting": ["hi", "hello", "hey", "greetings"],
        "order": ["order", "track", "status", "cancel", "delivery"],
        "refund": ["refund", "money", "return"],
        "technical": ["issue", "problem", "error", "technical"],
        "payment": ["payment", "method", "pay", "mode"],
        "warranty": ["warranty", "guarantee"],
        "contact": ["contact", "email", "phone", "support"],
        "hours": ["timing", "hours", "working"],
        "thanks": ["thank you", "thanks", "thx"],
        "exit": ["bye", "exit", "goodbye", "see you"]
    }

    responses = {
        "greeting": "Hello again! How can I assist you today?",
        "order": "For order-related queries, please provide your order ID.",
        "refund": "Refunds are processed within 5-7 business days. Can you share your order details?",
        "technical": "Please explain your technical issue briefly so I can help.",
        "payment": "We support all major payment modes including UPI, cards, and wallets.",
        "warranty": "All our products have a minimum 1-year warranty.",
        "contact": "You can contact us at 1800-999-4567 or email help@support.com.",
        "hours": "Our service is active from 9 AM to 6 PM, Monday to Saturday.",
        "thanks": "You're most welcome! Let me know if you need more help.",
        "exit": "It was a pleasure assisting you. Have a great day! 👋"
    }

    for category, keywords in help_topics.items():
        if any(word in query for word in keywords):
            return responses[category], category

    return "I'm not sure I understand. Would you like me to connect you with a human agent?", "unknown"

def confirm_exit():
    confirm = input("Bot: Would you like to end the chat? (yes/no): ").strip().lower()
    if confirm == "yes":
        print("Bot: Goodbye! Take care. 👋")
        return True
    else:
        print("Bot: Glad to keep helping!")
        return False

def run_chatbot():
    greet_user()
    while True:
        query = get_user_query()
        reply, category = process_query(query)
        print(f"Bot: {reply}")

        if category == "exit":
            if confirm_exit():
                break
        elif category == "unknown":
            human = input("Would you like a callback from our support team? (yes/no): ").strip().lower()
            if human == "yes":
                print("Bot: Noted. Our team will reach out to you shortly. 📞")
                break


if __name__ == "__main__":
    run_chatbot()

