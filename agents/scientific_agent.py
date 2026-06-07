"""
Agente Científico buscando información en la web
"""
from .agent_factory import build_agents
from tools.arxiv_tools import buscar_arxiv

CONTENT_AGENT_PROMPT ="""
Actúa como un asistente útil y especializado en investigación.
  -buscar_arxiv : realiza busqueda en la web y retorna los resultados.
  cuando el usuario pregunte sobre un tema especifico:
  1. Usa la herramienta buscar_articulos
  2. Analiza los resultados.
  3. Devuelve una respuesta clara.
  4. Incluye enlaces de las fuentes utilizadas.
"""

def get_scientific_agent():
    scientific_agent = build_agents(
        name="ScientificAgent",
        tools=[buscar_arxiv],
        system_prompt=CONTENT_AGENT_PROMPT
        )
    return scientific_agent