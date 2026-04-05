import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history = []

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
        
    chat_history.append(HumanMessage(content=user_input))
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    
    print("AI:", result.content)

print(chat_history)