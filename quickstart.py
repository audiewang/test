from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a mean assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Tell a joke"}
  ]
)

print(completion.choices[0].message)

# response = client.embeddings.create(
#   model="text-embedding-ada-002",
#   input="The food was delicious and the waiter..."
# )

# print(response)