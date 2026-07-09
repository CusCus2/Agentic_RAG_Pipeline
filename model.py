from transformers import pipeline
from langchain_ollama import ChatOllama

def model():
    # llm = pipeline(
    #     "text2text-generation",
    #     model = "google/flan-t5-base",
    #     max_new_tokens = 150
    # )
    return ChatOllama(model="llama3")