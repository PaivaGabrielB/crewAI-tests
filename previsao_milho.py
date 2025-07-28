from modelo_ml import prever_preco
from openai_helper import gerar_insight

def prever_preco_e_gerar_insight(dados):
    preco_previsto = prever_preco(dados)
    prompt = f"O preço previsto do milho é R${preco_previsto:.2f}. Gere um insight de mercado com base nesse valor."
    insight = gerar_insight(prompt)
    return insight