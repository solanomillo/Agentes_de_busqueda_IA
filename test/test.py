import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
from graph.graph import Graph

graph = Graph().build_graph()

result = graph.invoke(
    {
        "user_query": "¿Cuál es el impacto de la inteligencia artificial en la educación?"
    }
)

print(result["final_answer"])