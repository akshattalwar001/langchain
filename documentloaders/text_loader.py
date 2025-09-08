import os
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)
prompt = PromptTemplate(
    template = "mention name of bad characters with number associated in data. \n {data}",
    input_variables=["data"]
)
parser = StrOutputParser()
loader = TextLoader("D:\Games\langchain\documentloaders\characters_aot_300_lines.txt", encoding="utf-8")
docs=loader.load()
chain = prompt | model | parser

result = chain.invoke({"data": docs[0].page_content})
print(result)

'''Based on the provided descriptions, these characters could be considered "bad" in varying degrees, with some exhibiting more morally ambiguous actions than outright villainy:

* **7. Reiner Braun:**  A major antagonist, driven by ideology and guilt.
* **8. Bertholdt Hoover:**  A key antagonist, complicit in horrific acts.
* **9. Annie Leonhart:**  A cold and calculating antagonist, responsible for significant harm.
* **15. Zeke Yeager:**  A major antagonist, driven by his own twisted vision.
* **17. Gabi Braun:**  Initially an antagonist due to indoctrination and actions, but shows growth and redemption.
* **27. Kenny Ackerman:** A ruthless and morally ambiguous character.
* **28. Rod Reiss:** A manipulative and power-hungry antagonist.
* **32. Floch Forster:** A radicalized antagonist driven by extremist ideology.
* **36. Willy Tybur:**  An antagonist whose actions instigate a major conflict.
* **37. Lara Tybur:** An antagonist who actively fights against the protagonists.
* **40. Kenny Squad Members:**  Elite fighters who are shown to be ruthless and willing to kill.


It's important to note that the "badness" of these characters is subjective and depends on the viewer's perspective. Some characters undergo significant changes and might not be considered "bad" throughout the entire series.
'''