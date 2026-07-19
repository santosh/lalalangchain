import time
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain_ollama import ChatOllama

load_dotenv()

class HooksDemo(AgentMiddleware):
    def __init__(self):
        super().__init__()
        self.start_time = 0.0

    def before_agent(self, state: AgentState, runtime):
        self.start_time = time.time()
        print("Starting agent execution...")

    def before_model(self, state: AgentState, runtime):
        print("Before model call...")

    def after_model(self, state: AgentState, runtime):
        print("After model call...")

    def after_agent(self, state: AgentState, runtime):
        elapsed_time = time.time() - self.start_time
        print(f"Agent execution completed in {elapsed_time:.2f} seconds.")


def main():
    model = ChatOllama(model='qwen3:14b', temperature=0.3, reasoning=False)


    agent = create_agent(model, middleware=[HooksDemo()])

    response = agent.invoke({
        'messages': [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content="What is the capital of France?"),
        ]
    })

    print(response["messages"][-1].content)

if __name__ == "__main__":
    main()
