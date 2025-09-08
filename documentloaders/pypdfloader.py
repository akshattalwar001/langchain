import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)
prompt = PromptTemplate(
    template = "summary of plot \n {data}",
    input_variables=["data"]
)
parser = StrOutputParser()
loader = PyPDFLoader(r"D:\Games\langchain\documentloaders\A Comprehensive Guide.pdf")
docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({"data": docs[0].page_content})
print(result)


'''Attack on Titan follows Eren Yeager and his companions as they fight for survival against giant humanoid creatures called Titans, who have driven humanity to 
the brink of extinction.  Humanity lives within three concentric walls—Maria, Rose, and Sina—as a last bastion of defense.  The story begins as a survival str
uggle but evolves into a complex exploration of themes like racism, nationalism, historical trauma, and the cost of freedom.  Eren, fueled by revenge after wi
tnessing his mother's death, joins the military to eradicate the Titans, undergoing significant character development throughout the series.  The military is 
divided into three branches: the Garrison, Military Police, and Survey Corps, each playing a role in the struggle for survival and the uncovering of the world's mysteries.
'''