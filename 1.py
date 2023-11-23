
from openai import OpenAI
client = OpenAI(api_key='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')

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "user", "content": "Bugun gunlerden ne Tarih ne."}
  ]
)

print(completion.choices[0].message)