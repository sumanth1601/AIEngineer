
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

response = client.responses.create(
    model="gpt-4.1",
    input="Say Hello!"
)

print(response.output_text)