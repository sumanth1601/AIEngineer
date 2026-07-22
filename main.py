from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

question = input("Ask me anything: ")

response = client.responses.create(
    model="gpt-4.1",
    input=question
)

print(response.output_text)