from dotenv import load_dotenv
import os
from IPython.display import Markdown,display

from openai import OpenAI 

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI()
question = "Pick a business area that might be worth exploring for an Agentic AI oppurtunity. summarise in 2-3 sentences "
messages = [{"role": "user", "content": question}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
answer=(response.choices[0].message.content)
print(answer)
pain_point= "present a pain-point in that industry -something challenging that might be ripe for an Agentic solution in "+ response.choices[0].message.content +" summarise in 2-3 sentences"
messages = [{"role": "user", "content": pain_point}]
response1 = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
print("\n")
answer1=(response1.choices[0].message.content)
print(answer1)
agentic_solution= "build agentic soluting using"+response1.choices[0].message.content+response.choices[0].message.content
messages = [{"role": "user", "content": agentic_solution}]
response2 = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
print("\n")
answer2=response2.choices[0].message.content
print((answer2))
