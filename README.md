[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/solanomillo/Agentes_de_busqueda_IA/blob/main/Agentes_Langgraph_busquedas.ipynb)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-1.3+-green.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-1.2+-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red.svg)
![Gemini](https://img.shields.io/badge/Gemini-API-yellow.svg)

# 🔎 Agentes de Búsqueda IA

Sistema multiagente desarrollado con **LangGraph**, **LangChain**, **Gemini** y **Streamlit** para realizar búsquedas especializadas en internet y fuentes científicas.

## ▶️ Ejecución rápida en Google Colab

1. Haz clic en el badge **Open in Colab**.
2. Ejecuta todas las celdas desde **Runtime → Run all**.
3. Explora los resultados directamente en el notebook.
4. Haz una copia en tu Drive (File → Save a copy in Drive).

> ✅ No se requiere instalación local ni configuración adicional.

## 🚀 Descripción

Este proyecto implementa una arquitectura basada en **agentes inteligentes** capaces de analizar una consulta, decidir qué estrategia de búsqueda utilizar y generar una respuesta estructurada para el usuario.

El sistema utiliza un **agente ruteador** que determina automáticamente cuál agente especializado debe responder la consulta.

### Actualmente soporta:

- 🌐 **Búsquedas web generales** (mediante Tavily)
- 📚 **Búsquedas científicas** mediante ArXiv
- 🤖 **Enrutamiento inteligente** de consultas
- 💬 **Interfaz conversacional** con Streamlit

## 🛠️ Tecnologías utilizadas

| Tecnología | Propósito |
|------------|-----------|
| **LangChain** | Orquestación de cadenas y agentes |
| **LangGraph** | Gestión del flujo multiagente y estados |
| **Tavily** | Búsqueda web optimizada para IA |
| **ArXiv API** | Búsqueda de papers científicos |
| **Gemini (Google)** | Modelo LLM para razonamiento y generación |
| **Streamlit** | Interfaz de usuario interactiva |
| **Visual Studio Code** | Entorno de desarrollo |

## 🏗️ Arquitectura

```text
Usuario
   │
   ▼
Router Agent
   │
   ├─────────────► Web Search Agent (Tavily)
   │
   └─────────────► Scientific Search Agent (ArXiv)
                         │
                         ▼
                  Supervisor Node
                         │
                         ▼
                   Respuesta Final
```

## 🤖 Agentes

### Router Agent
Responsable de analizar la consulta del usuario y determinar qué agente especializado debe procesarla.

### Web Search Agent
Encargado de realizar búsquedas generales utilizando herramientas de búsqueda web.

**Casos de uso:**
- Noticias
- Definiciones
- Conceptos generales
- Tendencias
- Información pública

### Scientific Search Agent
Especializado en consultas académicas y científicas mediante ArXiv.

**Casos de uso:**
- Artículos científicos
- Papers académicos
- Investigaciones
- Revisiones sistemáticas
- Estado del arte

### Supervisor Node
Responsable de formatear y consolidar la respuesta final entregada al usuario.

## 🛠️ Tecnologías

| Tecnología | Versión / Uso |
|------------|---------------|
| Python | 3.13+ |
| LangChain | Orquestación de agentes |
| LangGraph | Flujo multiagente |
| Google Gemini | LLM principal |
| Tavily Search | Búsqueda web |
| ArXiv | Búsqueda científica |
| Streamlit | Interfaz de usuario |
| python-dotenv | Gestión de variables de entorno |

## 📂 Estructura del Proyecto
```text
Agentes_de_busqueda_IA/
│
├── agents/
│   ├── agent_factory.py
│   ├── scientific_agent.py
│   ├── web_agent.py
│   └── __init__.py
│
├── config/
│   ├── llm.py
│   ├── settings.py
│   └── __init__.py
│
├── graph/
│   ├── graph.py
│   └── __init__.py
│
├── schemas/
│   ├── state.py
│   └── __init__.py
│
├── tools/
│   ├── arxiv_tools.py
│   ├── tavily_tools.py
│   └── __init__.py
│
├── ui/
│   ├── app.py
│   └── __init__.py
│
├── test/
│   └── test.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Instalación
1. Clonar el repositorio
```bash
git clone https://github.com/solanomillo/Agentes_de_busqueda_IA.git
```
2. Crear entorno virtual
```bash
python -m venv .venv
```
Windows
```bash
.venv\Scripts\activate
```
Linux / macOS
```bash
source .venv/bin/activate
```
4. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 🔑 Variables de Entorno

Crear un archivo .env en la raíz del proyecto:
```tect
GOOGLE_API_KEY=tu_api_key
TAVILY_API_KEY=tu_api_key
```
## ▶️ Ejecutar la Aplicación
```text
streamlit run main.py
```

La aplicación estará disponible en:
```bash
http://localhost:8501
```
## 🧪 Ejecutar Pruebas
```text
python test/test.py
```

---

## 📈 Estado Actual

### ✅ Implementado

| Feature | Estado |
|---------|--------|
| Arquitectura multiagente | ✅ |
| Router Agent | ✅ |
| Web Search Agent | ✅ |
| Scientific Search Agent | ✅ |
| Supervisor Node | ✅ |
| Interfaz Streamlit | ✅ |
| Gestión básica de estado | ✅ |
| Historial en sesión | ✅ |

### 🔜 Próximas Mejoras

| Feature | Estado |
|---------|--------|
| Persistencia de conversaciones | ⏳ |
| Base de datos SQLite | ⏳ |
| Memoria conversacional | ⏳ |
| Streaming de respuestas | ⏳ |
| Exportación de conversaciones | ⏳ |
| Soporte para múltiples modelos | ⏳ |
| Panel de métricas | ⏳ |
| Sistema de evaluación de respuestas | ⏳ |
| Búsqueda híbrida (Web + Científica) | ⏳ |
| Autenticación de usuarios | ⏳ |

## 🎯 Objetivos de Aprendizaje

Este proyecto fue desarrollado con fines educativos para practicar:

- Diseño de sistemas multiagente
- LangGraph
- LangChain
- Integración con LLMs
- Arquitecturas orientadas a agentes
- Desarrollo de aplicaciones con Streamlit

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

## 👨‍💻 Autor
**Julio Solano**

- 🔗 GitHub: [https://github.com/solanomillo](https://github.com/solanomillo)
- 🔗 LinkedIn: [https://www.linkedin.com/in/julio-cesar-solano](https://www.linkedin.com/in/julio-cesar-solano)
- 📧 Email: solanomillo144@gmail.com
- 
Desarrollado como proyecto de aprendizaje y experimentación en sistemas multiagente utilizando LangGraph y Gemini.
