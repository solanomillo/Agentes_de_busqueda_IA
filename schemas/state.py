from typing import TypedDict

class AgentState(TypedDict, total=False):
    user_query: str
    router_decision: str
    web_answer: str
    scientific_answer: str
    final_answer: str