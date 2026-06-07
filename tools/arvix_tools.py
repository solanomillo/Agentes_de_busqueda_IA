"""
Herramienta Articulos cientificos
"""
from langchain_core.tools import tool
import arxiv

@tool
def buscar_arxiv(query: str) -> str:
    """
    Busca artículos cientificos en arXiv.
    """
    try:
        # Crear cliente
        client = arxiv.Client()

        # Configurar búsqueda
        search = arxiv.Search(
            query=query,
            max_results=3,
            sort_by=arxiv.SortCriterion.Relevance
        )

        # Obtener resultados - FORMA CORRECTA
        resultados = []

        for paper in client.results(search):  # Usar client.results()
            # Limpiar resumen
            abstract = paper.summary.replace('\n', ' ').strip()
            if len(abstract) > 300:
                abstract = abstract[:300] + "..."

            resultados.append(
                f"""**{paper.title}**
                  Año: {paper.published.year}
                  Autores: {', '.join(a.name for a in paper.authors[:3])}{', ...' if len(paper.authors) > 3 else ''}
                  Resumen: {abstract}
                  URL: {paper.entry_id}
                  """
            )

        if not resultados:
            return f"No se encontraron artículos en arXiv para: '{query}'"

        return "\n---\n".join(resultados)

    except Exception as e:
        return f"Error en búsqueda de arXiv: {str(e)}"