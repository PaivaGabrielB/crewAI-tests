# Previsão de Preço do Milho com CrewAI

Este projeto utiliza a biblioteca [CrewAI](https://docs.crewai.com/) com agentes de IA para prever o preço do milho e gerar insights automatizados a partir de dados de entrada.

## 🚀 Tecnologias utilizadas

- Python 3.10+
- [CrewAI](https://docs.crewai.com/)
- [LangChain](https://www.langchain.com/)
- [LiteLLM](https://docs.litellm.ai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- OpenAI GPT-4o (via API)

## 🔧 Instalação

1. Clone o repositório:

git clone https://github.com/PaivaGabrielB/crewAI-tests.git

cd seu-projeto

2. Crie um ambiente virtual e ative:

python -m venv venv

source venv/bin/activate   # Linux/macOS

venv\Scripts\activate      # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Crie um arquivo .env com a sua chave da API da OpenAI:

OPENAI_API_KEY=sua_chave_aqui

🧠 Como funciona
A CrewAI cria agentes que colaboram entre si. Um deles usa uma ferramenta personalizada (prever_preco_milho_tool) que chama a função:


from previsao_milho import prever_preco_e_gerar_insight
Ela processa os dados fornecidos (ex: preços históricos, clima, etc) e retorna um insight.

Exemplo de ferramenta:

from crewai.tools import tool

@tool(name="prever_preco_milho", description="Prevê preço do milho e gera insight")
def prever_preco_milho_tool(dados: list) -> dict:
    from previsao_milho import prever_preco_e_gerar_insight
    insight = prever_preco_e_gerar_insight(dados)
    return {"insight": insight}


▶️ Execução
Para rodar o script principal:

python crew_ai_script.py

O script irá carregar os dados, criar os agentes e executar a previsão.

📌 Observações
Certifique-se de que sua chave da OpenAI esteja correta no .env.

Você pode adaptar a lógica da função prever_preco_e_gerar_insight conforme os dados disponíveis.
