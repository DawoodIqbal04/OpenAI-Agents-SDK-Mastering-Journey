from agents import Agent, Runner, function_tool ,trace
from connectivity import config
import asyncio

@function_tool
def weather_tool():
    return 'Rainy'

@function_tool
def calculator_tool(num1: int, num2: int):
    return num1 + num2

agent = Agent(
    name= 'Assistant Agent',
    instructions= 'You are a helpfull assistant, answer user query politely.',
    tools= [weather_tool, calculator_tool]
)


async def main():
    with trace('Tool Calling'):
        result = await Runner.run(
            agent,
            'what is the weather of Lyari. What is the sum of 44 and 2094',
            run_config= config
        )
    print(result.final_output)
    


if __name__ == '__main__':
    asyncio.run(main())
