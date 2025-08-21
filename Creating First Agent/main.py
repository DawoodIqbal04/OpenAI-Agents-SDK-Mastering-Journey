from agents import Agent, Runner, trace
from connectivity import config

agent = Agent(
    name = 'Personal Agent',
    instructions= 'You are a helpfull assistant'
)

def main():
    with trace('First Agent'):
        result = Runner.run_sync(
        agent,
        'What is the capital of USA, how to create a calculator app in react',
        run_config= config
    )
    print(result.final_output)


if __name__ == "__main__":
    main()
