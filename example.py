import dotenv
dotenv.load_dotenv()


from chatbot_api.src.agents.hospital_rag_agent import hospital_rag_agent_executor

response = hospital_rag_agent_executor.invoke(
    {"input": "What is the wait time at Wallace-Hamilton?"}
)
print(response.get("output"))

response = hospital_rag_agent_executor.invoke(
    {"input": "Which hospital has the shortest wait time?"}
)
print(response.get("output"))