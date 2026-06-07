"""
Interfaz principal de Agentes de Búsqueda IA.
"""

import streamlit as st
from graph.graph import Graph


@st.cache_resource
def load_graph():
    """
    Carga el grafo una sola vez.
    """
    return Graph().build_graph()


def initialize_session():
    """
    Inicializa variables de sesión.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []


def clear_chat():
    """
    Limpia la conversación actual.
    """

    st.session_state.messages = []


def render_sidebar():
    """
    Renderiza barra lateral.
    """

    with st.sidebar:

        st.title("🔎 Search AI")

        st.markdown(
            """
            Sistema multiagente para búsquedas web y científicas.
            """
        )

        st.divider()

        if st.button(
            "🗑️ Nueva conversación",
            use_container_width=True
        ):
            clear_chat()
            st.rerun()

        st.divider()

        st.subheader("🤖 Agentes")

        st.markdown(
            """
            **Router Agent**
            - Decide qué agente utilizar.

            **Web Search Agent**
            - Realiza búsquedas generales.

            **Scientific Search Agent**
            - Consulta artículos científicos.
            """
        )

        st.divider()

        st.subheader("📊 Estadísticas")

        st.metric(
            label="Mensajes",
            value=len(st.session_state.messages)
        )

        st.divider()

        st.subheader("⚙️ Sistema")

        st.success("Estado: Operativo")

        st.caption("Versión 1.0.0")


def render_chat():
    """
    Renderiza historial de mensajes.
    """

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(
                message["content"]
            )


def process_query(graph, user_query):
    """
    Procesa consulta.
    """

    result = graph.invoke(
        {
            "user_query": user_query
        }
    )

    return result["final_answer"]


def run():

    st.set_page_config(
        page_title="Agentes de Búsqueda IA",
        page_icon="🔎",
        layout="wide"
    )

    initialize_session()

    render_sidebar()

    graph = load_graph()

    st.title("🔎 Agentes de Búsqueda IA")

    st.markdown(
        """
        Consulta información mediante agentes especializados
        en búsquedas web y científicas.
        """
    )

    render_chat()

    user_query = st.chat_input(
        "Escribe tu pregunta..."
    )

    if user_query:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_query
            }
        )

        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):

            placeholder = st.empty()

            try:

                with st.spinner(
                    "Analizando consulta..."
                ):

                    response = process_query(
                        graph,
                        user_query
                    )

                placeholder.markdown(
                    response
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                error_message = (
                    f"❌ Error: {str(e)}"
                )

                placeholder.error(
                    error_message
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )