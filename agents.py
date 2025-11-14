
from agno.agent import Agent
from agno.team import Team
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

# Agent 1: Data Analysis Agent
data_agent = Agent(
    name="Data Analyst",
    role="Analyze financial data and calculate metrics",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=Groq(id="llama-3.1-8b-instant"),
    # model=Groq(id="mixtral-8x7b-32768") ,
    tools=[YFinanceTools()],
    instructions=[
        "Calculate key financial metrics",
        "Identify trends in data",
        "Use tables to display numbers"
    ],
    markdown=True
)

# Agent 2: Risk Assessment Agent
risk_agent = Agent(
    name="Risk Analyst",
    role="Evaluate financial risks",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=Groq(id="llama-3.1-8b-instant"),
    # model=Groq(id="mixtral-8x7b-32768") ,
    tools=[YFinanceTools()],
    instructions=[
        "Calculate risk metrics and volatility",
        "Identify potential risks",
        "Rate risk level from 1-10"
    ],
    markdown=True
)

# Agent 3: Strategy Agent
strategy_agent = Agent(
    name="Strategy Advisor",
    role="Provide strategic recommendations",
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=Groq(id="llama-3.1-8b-instant"),
    # model=Groq(id="mixtral-8x7b-32768") ,
    tools=[YFinanceTools(), DuckDuckGoTools()],
    instructions=[
        "Synthesize insights from other agents",
        "Provide actionable recommendations",
        "Always justify with evidence"
    ],
    markdown=True
)

# Multi-Agent Team using Team class

financial_team = Team(
    name="Financial Analysis Team",
    members=[data_agent, risk_agent,strategy_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    # model=Groq(id="llama-3.1-8b-instant"),
   
    instructions=[
        "Coordinate with team members to provide comprehensive financial analysis",
        "Delegate tasks based on the user's request"
    ],
    markdown=True
)