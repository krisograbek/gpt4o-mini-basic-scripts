from dotenv import load_dotenv

load_dotenv()


from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4o-mini")

messages = [
    ChatMessage(
        role="system",
        content="You specialize in concisely explaining complex topics to 12yo.",
    ),
    ChatMessage(role="user", content="What's an artificial neural network?"),
]
response = llm.chat(messages)


print(response)
