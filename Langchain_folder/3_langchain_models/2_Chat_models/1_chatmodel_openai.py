
#temperature is something that determines LLM output,

#if the values are 0.0-0.3 -- more deterministic and predictable
#if between 0.5-0.7 -- balanced response(general QA, explanations)
#if between 0.9-1.2 -- creative writing, storytelling
#if 1.5+ -- wild ideas, brainstorming

# max_completion_tokens is how many tokens or words we want in output

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)
