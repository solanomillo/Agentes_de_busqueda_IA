from schemas.state import AgentState
from agents import scientific_agent, web_agent
from langchain.agents import create_agent
from config.llm import get_llm
from langgraph.graph import StateGraph, START, END


class Graph:

    def extract_text(self, result) -> str:
        """
        Extrae texto de la respuesta del agente.
        """

        ultimo_mensaje = result["messages"][-1]

        if isinstance(ultimo_mensaje.content, str):
            return ultimo_mensaje.content

        if isinstance(ultimo_mensaje.content, list):
            textos = []

            for bloque in ultimo_mensaje.content:
                if isinstance(bloque, dict):
                    textos.append(bloque.get("text", ""))

            return "\n".join(textos)

        return str(ultimo_mensaje.content)

    def funcion_agente_web(self, state: AgentState) -> dict:

        user_query = state["user_query"]

        agente_web = web_agent.get_web_agent()

        resultado = agente_web.invoke(
            {
                "messages": [
                    ("user", user_query)
                ]
            }
        )

        respuesta_final = self.extract_text(resultado)

        return {
            "web_answer": respuesta_final
        }

    def funcion_agente_cientifico(self, state: AgentState) -> dict:

        user_query = state["user_query"]

        agente_cientifico = scientific_agent.get_scientific_agent()

        resultado = agente_cientifico.invoke(
            {
                "messages": [
                    ("user", user_query)
                ]
            }
        )

        respuesta_final = self.extract_text(resultado)

        return {
            "scientific_answer": respuesta_final
        }

    def supervisor_node(self, state: AgentState) -> dict:

        web_result = state.get(
            "web_answer",
            "No se realizó ninguna búsqueda web."
        )

        scientific_result = state.get(
            "scientific_answer",
            "No se realizó ninguna búsqueda científica."
        )

        final_answer = f"""
# Resultados de la búsqueda

## Búsqueda Web

{web_result}

---

## Búsqueda Científica

{scientific_result}
"""

        return {
            "final_answer": final_answer
        }

    def router_agent(self, state: AgentState) -> dict:

        router_prompt = """
Eres un agente ruteador.

Tu tarea es decidir qué agente debe responder.

Opciones:

- web_search
- scientific_search

Usa:

web_search:
Preguntas generales, actualidad, noticias,
definiciones o búsquedas en internet.

scientific_search:
Preguntas académicas, investigaciones,
papers científicos o artículos de Arxiv.

Responde únicamente:

web_search

o

scientific_search
"""

        router = create_agent(
            model=get_llm(),
            tools=[],
            system_prompt=router_prompt
        )

        response = router.invoke(
            {
                "messages": [
                    ("user", state["user_query"])
                ]
            }
        )

        decision = (
            response["messages"][-1]
            .content
            .strip()
            .lower()
        )

        if "scientific_search" in decision:
            return {
                "router_decision": "scientific_search"
            }

        return {
            "router_decision": "web_search"
        }

    def build_graph(self):

        workflow = StateGraph(AgentState)

        workflow.add_node(
            "router",
            self.router_agent
        )

        workflow.add_node(
            "web_search",
            self.funcion_agente_web
        )

        workflow.add_node(
            "scientific_search",
            self.funcion_agente_cientifico
        )

        workflow.add_node(
            "supervisor",
            self.supervisor_node
        )

        workflow.add_edge(
            START,
            "router"
        )

        workflow.add_conditional_edges(
            "router",
            lambda state: state["router_decision"],
            {
                "web_search": "web_search",
                "scientific_search": "scientific_search",
            }
        )

        workflow.add_edge(
            "web_search",
            "supervisor"
        )

        workflow.add_edge(
            "scientific_search",
            "supervisor"
        )

        workflow.add_edge(
            "supervisor",
            END
        )

        return workflow.compile()