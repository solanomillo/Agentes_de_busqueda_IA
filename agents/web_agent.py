"""
Agente de Búsqueda en la web
"""
from .agent_factory import build_agents
from tools.tavily_tools import tavily_tool

CONTENT_AGENT_PROMPT = """
  Actúa como un asistente útil y especializado en investigación para responder la consulta del usuario.
  -tavily_tool : realiza busqueda en la web y retorna los resultados.
  Siempre que el usuario pregunte sobre un tema especifico:
  1. Analiza los resultados.
  2. Devuelve una respuesta clara.
  3. Incluye enlaces de las fuentes utilizadas.
"""

# Construye el agente de contenido con la herramienta de búsqueda web
def get_web_agent():
    web_agent = build_agents(
        name="WebAgent",
        tools=[tavily_tool],
        system_prompt=CONTENT_AGENT_PROMPT
        )
    return web_agent 
