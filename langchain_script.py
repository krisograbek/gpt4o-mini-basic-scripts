from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke(
    "Explain concisely like I was 12 what are artificial neural networks?"
)

print(response.content)
