from google.generativeai import GenerativeModel
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

chat_history = [
    SystemMessage(content='You are a helpful assistant')
]

# Convert LangChain messages into a list of strings for Gemini
def convert_to_text_messages(history):
    return [msg.content for msg in history if isinstance(msg, (HumanMessage, AIMessage, SystemMessage))]

...

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))

    # Send only plain strings to Gemini
    result = model.generate_content(convert_to_text_messages(chat_history))

    # Extract response safely
    ai_reply = result.candidates[0].content.parts[0].text
    chat_history.append(AIMessage(content=ai_reply))

    print("AI:", ai_reply)

print(chat_history)