from langchain.prompts import ChatPromptTemplate
import os

with open('app/prompts/ask_prompt.txt', 'r') as f:
    ask_template = f.read()

with open('app/prompts/summarize_prompt.txt', 'r') as f:
    summarize_template = f.read()

ask_prompt = ChatPromptTemplate.from_template(ask_template)
summarize_prompt = ChatPromptTemplate.from_template(summarize_template)