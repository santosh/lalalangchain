from dataclasses import dataclass
from typing import Callable
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage
from langchain.agents.middleware import ModelRequest, ModelResponse, wrap_model_call
from langchain_ollama import ChatOllama

load_dotenv()

basic_model = ChatOllama(model="llama3.1:8b")
advanced_model = ChatOllama(model="qwen3:14b")
vision_model = ChatOllama(model="gemma3:12b")

@wrap_model_call
def dynamic_model_selector(
    request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]
) -> ModelResponse:
    text = request.messages[-1].text.lower()

    if "advanced" in text:
        model = advanced_model
    elif "vision" in text:
        model = vision_model
    else:
        model = basic_model

    return handler(request.override(model=model))

def main():
    agent = create_agent(
        model=basic_model,
        middleware=[dynamic_model_selector],
        tools=[],
    )

    response = agent.invoke({
        "messages": [
            SystemMessage("You are a helpful assistant."),
            HumanMessage("advanced What is 1 + 1?"),
        ]
    })

    print(response['messages'][-1].content)
    print(response['messages'][-1].response_metadata['model_name'])

if __name__ == "__main__":
    main()
