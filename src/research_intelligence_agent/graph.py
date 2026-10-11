from langgraph.graph import START,END,StateGraph
from .state import ChatState
from .nodes import web_search_node,chat_node


graph=StateGraph(ChatState)

graph.add_node("search_web",web_search_node)
graph.add_node("chat_node",chat_node)

graph.add_edge(START,"search_web")
graph.add_edge("search_web","chat_node")
graph.add_edge("chat_node",END)


workflow=graph.compile()

# result=workflow.invoke({"query":"corrective-rag crag in 2026 vs normal rag"})
# print(result)