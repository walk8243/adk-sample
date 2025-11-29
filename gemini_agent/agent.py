from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='gemini_agent',
    description='A helpful assistant for user questions using Gemini API.',
    instruction='Answer user questions to the best of your knowledge',
)
