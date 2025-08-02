from langgraph.graph import StateGraph, START, END
from src.models.state import ToolState
from src.nodes.determine_intent import determine_intent
from src.nodes.call_weather import call_weather
from src.nodes.call_news import call_news
from src.nodes.call_user_info import call_user_info  # 👈 new import
from src.nodes.generate_response import generate_response
from src.nodes.router import intent_router

def build_graph():
    graph = StateGraph(ToolState)

    # Add nodes
    graph.add_node("determine_intent", determine_intent)
    graph.add_node("weather_node", call_weather)
    graph.add_node("news_node", call_news)
    graph.add_node("user_info_node", call_user_info)  # 👈 new node
    graph.add_node("generate_response", generate_response)

    # Set flow
    graph.set_entry_point("determine_intent")
    graph.add_conditional_edges("determine_intent", intent_router)

    # Edges based on intent
    graph.add_edge("weather_node", "generate_response")
    graph.add_edge("news_node", "generate_response")
    graph.add_edge("user_info_node", "generate_response")  # 👈 new edge

    # Final edge
    graph.add_edge("generate_response", END)

    return graph.compile()
