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
    model_provider= client,
    tracing_disabled= True
)

agent = Agent(
    'Joker Agent',
    'You are a Joker agent'
)

def main():
    result = Runner.run_sync(agent, 'Tell me two one liner cold jokes.')
    print(result.final_output)
    
    
main()