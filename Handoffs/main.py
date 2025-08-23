from agents import Agent, Runner, trace
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from connectivity import config
import asyncio

medicine_uses_agent = Agent(
    name= 'Medicine Uses Agent',
    instructions= 'You are a medicine uses teller agent. You have to give user uses of medicine he asks about where you can search on internet for the medicine and fulfill user query. NOTE: You will not respond with "I am not doctor or ask with doctor or a link" ',
    handoff_description= 'Medicine uses teller agent'
)

recipe_chef_agent = Agent(
    name= 'Recipies Guide Chef',
    instructions= 'You are a chef agent. Your task is to give a proper recipe guide of user`s desired recipe',
    handoff_description= 'Recipe Guide Chef agent'
)


agent = Agent(
    name="Assistant Agent",
    instructions= 'You are a triage/ Parent/ Orechestration agent. use given handoffs to fulfill user queries',
    handoffs= [medicine_uses_agent, recipe_chef_agent] # Agent handoffs task to only one agent at a time
)


async def main():
    with trace("Handoffs"):
        result = await Runner.run(
            agent,
            input("User: "),
            run_config=config,
        )
    print("Bot: " ,result.final_output)
    print('\n========================================\n')
    print(result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())
