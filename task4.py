# TASK 4: Basic Chatbot
import random

def get_response(user_input):
    """Return chatbot response based on user input"""
    user_input = user_input.lower().strip()
    
    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        responses = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Nice to meet you!",
            "Hello! I'm here to chat with you."
        ]
        return random.choice(responses)
    
    # How are you
    elif any(phrase in user_input for phrase in ["how are you", "how do you do", "what's up"]):
        responses = [
            "I'm doing great, thanks for asking! How about you?",
            "I'm fine! How are you doing today?",
            "I'm good! Thanks for checking in.",
            "I'm doing well! What about yourself?"
        ]
        return random.choice(responses)
    
    # Name questions
    elif any(phrase in user_input for phrase in ["your name", "who are you", "what are you"]):
        responses = [
            "I'm a simple chatbot! You can call me Bot.",
            "I'm your friendly chatbot assistant!",
            "I'm a basic AI chatbot created to chat with you!",
            "I'm just a simple chatbot here to help."
        ]
        return random.choice(responses)
    
    # Help/capabilities
    elif any(word in user_input for word in ["help", "what can you do", "capabilities"]):
        return "I can chat with you! Try saying hello, asking how I am, or just talk to me about anything."
    
    # Thanks
    elif any(word in user_input for word in ["thank you", "thanks", "thank"]):
        responses = [
            "You're welcome!",
            "Happy to help!",
            "No problem!",
            "Glad I could help!"
        ]
        return random.choice(responses)
    
    # Jokes
    elif any(word in user_input for word in ["joke", "funny", "laugh"]):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!"
        ]
        return random.choice(jokes)
    
    # Weather (simple response since we can't check real weather)
    elif any(word in user_input for word in ["weather", "temperature", "rain", "sunny"]):
        responses = [
            "I can't check the weather, but I hope it's nice where you are!",
            "I don't have weather data, but I hope you're having a good day!",
            "I wish I could tell you about the weather! How's it looking outside?"
        ]
        return random.choice(responses)
    
    # Time (simple response)
    elif any(word in user_input for word in ["time", "date", "day"]):
        import datetime
        now = datetime.datetime.now()
        return f"It's currently {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d, %Y')}"
    
    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "see you", "exit", "quit"]):
        responses = [
            "Goodbye! It was nice chatting with you!",
            "See you later! Have a great day!",
            "Bye! Thanks for the conversation!",
            "Farewell! Come back anytime!"
        ]
        return random.choice(responses)
    
    # Default responses for unrecognized input
    else:
        responses = [
            "That's interesting! Tell me more.",
            "I'm not sure I understand, but I'm listening!",
            "Can you tell me more about that?",
            "Hmm, that's something new! What do you think about it?",
            "I'd love to learn more about what you're saying.",
            "That sounds intriguing! Can you explain more?"
        ]
        return random.choice(responses)

def chatbot():
    """Main chatbot function"""
    print("=== Simple Chatbot ===")
    print("Hello! I'm a basic chatbot. Type 'bye' to exit.")
    print("-" * 40)
    
    while True:
        user_input = input("\nYou: ")
        
        if not user_input.strip():
            print("Bot: I'm here when you want to chat!")
            continue
        
        # Check for exit commands
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            response = get_response(user_input)
            print(f"Bot: {response}")
            break
        
        # Get and display response
        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()