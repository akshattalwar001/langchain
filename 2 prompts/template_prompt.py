import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

print('Research Tool')
print("-" * 20)

papers = [
    "Attention is all you need",
    "BERT:Pre-training of Bidirectional Transformers",
    "GPT-3: Language models are few-shot Learners",
    "Diffusion Models Best GANs on Image synthesis"
]

styles = ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
lengths = ["Short (1-2 Paragraphs)", "Medium (3-5 paragraphs)", "Long(detailed explanation)"]

def get_user_choice(title, options):
    print("\n" + title + ":")
    for i, option in enumerate(options, 1):
        print(str(i) + ". " + option)
    choice = int(input("Select number (1-" + str(len(options)) + "): ")) - 1
    return options[choice]

paper_input = get_user_choice("Available Papers", papers)
style_input = get_user_choice("Available Styles", styles)
length_input = get_user_choice("Available Lengths", lengths)

template = """
You are an AI assistant that explains research papers.

Paper Title: "{paper_title}"
Explanation Style: {explanation_style}
Explanation Length: {explanation_length}

Please provide the explanation accordingly.
"""

prompt = PromptTemplate.from_template(template)
chain = prompt | llm

print("\nGenerating Explanation...\n")
result = chain.invoke({
    "paper_title": paper_input,
    "explanation_style": style_input,
    "explanation_length": length_input
})

print("Explanation:")
print(result.content)