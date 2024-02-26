import openai
import os

openai.api_key ="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"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)