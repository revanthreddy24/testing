# First let's do an import. If you get an Import Error, double check that your Kernel is correct..

from dotenv import load_dotenv
import os
from IPython.display import Markdown, display

from openai import OpenAI

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")


openai = OpenAI()
question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question "
messages = [{"role": "user", "content": question}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

print(response.choices[0].message.content)

answer = "answer to this "+response.choices[0].message.content

messages = [{"role": "user", "content": answer}]
response2 = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
print("\n")
print(response2.choices[0].message.content)

