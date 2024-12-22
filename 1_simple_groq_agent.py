from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Create an instance of the Agent and assign it to a variable
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

# Use the assigned variable to call the method
agent.print_response("Write 2 sentence poem for the love between dosa and samosa")
