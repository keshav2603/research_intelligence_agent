from langchain_tavily import TavilySearch
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

search_clint=TavilySearch(max_results=7)

@tool
def search_web_tool(query:str):
    """ search the web for relevant information about the querry"""
    result=search_clint.invoke({"query":query})
    return result["results"]

# tool testing

# result = search_web_tool.invoke({"query": "how was the performance of india in Asian Games 2026"})
# print(result)
# print("Output type:", type(result))
# print("Top-level keys:", result.keys())

# print("\nNumber of results:", len(result["results"]))

# for i, item in enumerate(result["results"], start=1):
#     print(f"\nResult {i}\n\n")
#     print("Title:", item["title"])
#     print("URL:", item["url"])
#     print("Score:", item["score"])
#     print("Content:", item["content"])