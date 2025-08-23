from agents import Agent, Runner, trace
from connectivity import config
import asyncio


chemistry_agent = Agent(
    name="Chemistry Instructor",
    instructions="You are a Chemistry subject instructor, teacher and helper. Answer the questions or help queries about Chemistry related topics.",
)
biology_agent = Agent(
    name="Biology Instructor",
    instructions="You are a Biology subject instructor, teacher and helper. Answer the questions or help queries about Biology related topics.",
)
physics_agent = Agent(
    name="Pyhsics Instructor",
    instructions="You are a Pyhsics subject instructor, teacher and helper. Answer the questions or help queries about Pyhsics related topics.",
)


agent = Agent(
    name="Assistant Agent",
    instructions=(
        "You are a study helper, questions answerer, and study instructor."
        "Use tools given to you to anwer that related content and if query is about multiple subjects or topic you have option to call multiple tools."
    ),
    tools=[
        chemistry_agent.as_tool(
            tool_name="chemistry_resolver",
            tool_description="Answer and help with chemistry related queries.",
        ),
        biology_agent.as_tool(
            tool_name="biology_resolver",
            tool_description="Answer and help with biology related queries.",
        ),
        physics_agent.as_tool(
            tool_name="physics_resolver",
            tool_description="Answer and help with physics related queries.",
        ),
    ],
)


async def main():
    with trace("Agents as Tools"):
        result = await Runner.run(
            agent,
            input("Question any thing about your study."),
            run_config=config,
        )
    print(result.final_output)
    print('\n========================================\n')
    print(result.last_agent)
    print('\n========================================\n')
    print(result.last_agent.name)


if __name__ == "__main__":
    asyncio.run(main())
