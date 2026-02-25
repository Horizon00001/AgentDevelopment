from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

def call_ai(messages) -> str:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
    )
    result = response.choices[0].message.content
    if result:
        return result