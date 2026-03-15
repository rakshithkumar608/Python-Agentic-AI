from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(
    model="llama-3.1-8b-instant",
    model_provider="groq"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}



graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)


graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


graph = graph_builder.compile()

def complie_graph_with_checkpointer():
    DB_URI = "mongodb://admin:admin@localhost:27017/lg"
    with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
        graph_builder.compile(checkpointer=checkpointer)
        return graph
    
graph_with_checkpointer = complie_graph_with_checkpointer()

config = {
    "configurable":{
        "thread_id": "Rakshith"
    }
}

updated_state = graph.invoke({"messages": ["Hi, My name is Rakshith"]})

print("\n\nUpdated_state:", updated_state)