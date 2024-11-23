def chatbot():
    print("Hello! I'm your friendly chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase to make it case-insensitive
        
        # Exit condition
        if 'bye' in user_input or 'exit' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Responding to specific queries
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing great, thank you for asking! How about you?")
        
        elif 'name' in user_input:
            print("Chatbot: I'm a chatbot, I don't have a name, but you can call me Chatbot.")
        
        elif 'help' in user_input:
            print("Chatbot: Sure! I can help with the following queries: \n1. How are you? \n2. What is your name? \n3. Type 'bye' or 'exit' to end the chat.")
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase your question or ask something else?")
    
# Run the chatbot
chatbot()
