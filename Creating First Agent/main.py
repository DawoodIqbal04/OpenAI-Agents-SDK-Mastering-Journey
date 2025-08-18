from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

gemini_api_key = os.getenv('GEMINI_API_KEY')

client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= 'https://generativelanguage.googleapis.com/v1beta/openai/'
)

model = OpenAIChatCompletionsModel(
    model= 'gemini-2.0-flash',
    openai_client= client
)
run_config = RunConfig(
    model= model,
    model_provider= client
)

assistant_agent = Agent(
    name= 'Personal Assistant Agent',
    instructions= 'You are a usefull assistant. Donot use reasoning just give answer.'
)

def main():
    results = Runner.run_sync(
        assistant_agent,
        input= 'what is the history of Baloch.',
        run_config= run_config
    )
    
    print(results.final_output)


if __name__ == '__main__':
    main()