from dotenv import load_dotenv

load_dotenv()


from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You specialize in concisely explaining complex topics to 12yo.",
        },
        {
            "role": "user",
            "content": "What's artificial neural network?",
        },
    ],
)

print(completion.choices[0].message.content)
