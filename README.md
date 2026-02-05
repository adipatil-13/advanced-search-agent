# Multi-Source AI Research Agent

An advanced, autonomous research assistant built with **LangGraph** and **Llama 3**. This agent performs parallel internet research across multiple sources (Google, Bing, Reddit), analyzes community discussions, and synthesizes a comprehensive report on any topic.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-orange)
![Groq](https://img.shields.io/badge/Groq-Llama%203-purple)
![Tavily](https://img.shields.io/badge/Tavily-Search-green)

## 🚀 Features

* **Parallel Research Execution:** Simultaneously queries Google, Bing, and Reddit to gather diverse perspectives.
* **Deep Reddit Analysis:** specifically targets Reddit threads to extract authentic user experiences, discussions, and community consensus.
* **Intelligent Synthesis:** Uses **Llama 3.3 (via Groq)** to read, analyze, and combine scattered information into a structured final answer.
* **Cost-Effective:** Fully optimized to run on **free tier** APIs (Groq for LLM inference, Tavily for search & extraction).
* **Stateful Architecture:** Built on **LangGraph** to manage the research state and workflow reliability.

## 🛠️ Tech Stack

* **Orchestration:** [LangGraph](https://langchain-ai.github.io/langgraph/)
* **LLM Inference:** [Groq Cloud](https://groq.com/) (Llama-3.3-70b)
* **Search & Extraction:** [Tavily AI](https://tavily.com/)
* **Framework:** Python, LangChain

## 📋 Prerequisites

Before running the project, ensure you have the following:

1.  **Python 3.10+** installed.
2.  **Groq API Key:** Get a free key at [console.groq.com](https://console.groq.com/).
3.  **Tavily API Key:** Get a free key at [tavily.com](https://tavily.com/).

## ⚡ Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/advances-ai-agent.git](https://github.com/yourusername/advances-ai-agent.git)
    cd advances-ai-agent
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install .
    # OR
    pip install -r pyproject.toml
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory and add your keys:
    ```env
    GROQ_API_KEY=gsk_your_groq_api_key_here
    TAVILY_API_KEY=tvly-your_tavily_api_key_here
    ```

## 🖥️ Usage

Run the main agent script:

```bash
python main.py
