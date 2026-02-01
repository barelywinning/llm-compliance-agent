import os
import chainlit as cl
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("GITHUB_TOKEN"),
        base_url="https://models.inference.ai.azure.com",
        temperature=0.3,
    )

@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Hello. I’m the AI aditya made. How can I help?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    llm = get_llm()

    response = await llm.ainvoke(message.content)

    await cl.Message(content=response.content).send()