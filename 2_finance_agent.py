from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

# Create an instance of the Agent and assign it to a variable
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True)
    ],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use table to display data."],
    # debug_mode=True
)

# Use the assigned variable to call the method
agent.print_response("Summarize and compare analyst recommandations and fundamentals for TSLA and NVDA")