from crewai.tools import tool



@tool
def prever_preco_milho_tool(dados: list) -> dict:
    """
    Prevê preço do milho e gera insight
    """
    from previsao_milho import prever_preco_e_gerar_insight
    insight = prever_preco_e_gerar_insight(dados)
    return {"insight": insight}