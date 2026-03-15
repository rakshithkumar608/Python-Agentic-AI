
from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional, Literal
from groq import Groq
from langgraph.graph import StateGraph, START, END

load_dotenv()

client = Groq()

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]
    
def chatbot(state: State):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": state.get("user_query")
            }
        ]
    )
    
    state["llm_output"] = response.choices[0].message.content
    return state


def evaluate_response(state: State) -> Literal["chatbot_gemini", "endnode"]:
    if True:
        return "endnode"
    
    return "chatbot_gemini"

def chatbot_gemini(state: State):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": state.get("user_query")
            }
        ]
    )
    
    state["llm_output"] = response.choices[0].message.content
    return state 

def endnode(state: State):
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("endnode", endnode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)

graph_builder.add_edge("chatbot_gemini", "endnode")
graph_builder.add_edge("endnode", END)

graph = graph_builder.compile()

updated_state = graph.invoke({
    "user_query": "Hey, What is an LLM and RAG used For?"
})

print(updated_state)