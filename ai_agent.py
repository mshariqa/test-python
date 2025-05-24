from agents import Agent, Runner, trace
from dotenv import load_dotenv
import asyncio

load_dotenv(override=True)

agent = Agent(name="Jockester", instructions="Tell a funny joke", model="gpt-4o-mini")

async def main():
    with trace("Telling a joke about cats"):
        result = await Runner.run(agent, "Tell me a joke about cats")
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
