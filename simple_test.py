from dotenv import load_dotenv
from agents import data_agent, risk_agent, strategy_agent

load_dotenv()

print("Testing individual agents...\n")

#Test Data Agent
print("1️⃣ Testing Data Agent:")
print("-" * 50)
data_agent.print_response("What is Apple's current stock price?", stream=True)
print("\n")
#Test Strategy Agent
print("2️⃣ Testing Strategy Agent:")
print("-" * 50)
strategy_agent.print_response("What are the latest market Strategy of Apple?", stream=True)
print("\n")
# Test Risk Agent  
print("3️⃣ Testing Risk Agent:")
print("-" * 50)
risk_agent.print_response("Evaluate the risk level of investing in Apple stock", stream=True)
print("\n")



print("All agents working!")
