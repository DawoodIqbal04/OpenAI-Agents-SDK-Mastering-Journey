from agents import Agent, Runner, trace
from connectivity import config
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

agent = Agent(
    name= 'Joker Agent',
    instructions= 'You are a funny joker'
)

async def main():
    # Run Async Method
    with trace('Runner Methods'):
        result = await Runner.run( # Runs asynchronusly
            agent,
            'tell me three two liner cold and funny jokes',
            run_config= config
        )
    print(result.final_output)
    
def sync():
    # Run Sync Method
    with trace('Runner Methods'):
        result2 = Runner.run_sync( # Runs synchronusly without async await keywords
            agent,
            'tell me a short funny story',
            run_config= config
        )
    print(result2.final_output)
    
async def stream():
    # Run Stream Method
    result3 = Runner.run_streamed( # Run streamly and gives response in form of chunks
        agent,
        'Tell me a 150 words funny horror story',
        run_config= config
    )
    async for e in result3.stream_events():
        if e.type == 'raw_response_event' and isinstance(e.data, ResponseTextDeltaEvent):
            print(e.data.delta, end='', flush=True)
    

if __name__ == '__main__':
    asyncio.run(stream())
    asyncio.run(main())
    sync()
