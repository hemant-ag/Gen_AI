from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #used for loading the .env file as it stores the OPENAPI_API_KEY

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)
