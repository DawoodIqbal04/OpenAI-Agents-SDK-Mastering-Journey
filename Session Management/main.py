from agents import Agent, SQLiteSession ,Runner, trace
from connectivity import config
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

chat_agent = Agent(
    name= 'Assistant Agent',
    instructions= 'You are a helpfull assistant, answer user query politely.'
)

session = SQLiteSession('Conversaion_101', 'Conversaton_101.db') # Creating Session

async def main():
    while True: # Looping for conversation
        user_input = input('User: ')
        
        if user_input.lower() in ['quit', 'exit']:
            print('Exiting .....')
            break
        with trace('Learning Session'):
            result = await Runner.run(
                chat_agent,
                input= user_input,
                run_config= config,
                session= session
            )
        print('Bot: ',result.final_output)


if __name__ == '__main__':
    asyncio.run(main())
