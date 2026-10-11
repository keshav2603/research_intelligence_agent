from typing import TypedDict


class ChatState(TypedDict):
    query: str
    response: str
    retrieved_info: list[dict]