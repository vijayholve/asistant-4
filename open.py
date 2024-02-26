import openai
import os 

api_key = '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'  

openai.api_key = api_key

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Once upon a time",
    max_tokens=50
)
    
print(response.choices[0].text.strip())