from previsao_milho import prever_preco_e_gerar_insight

if __name__ == "__main__":
    # Exemplo de dado para previsão (ajuste conforme seu modelo espera)
    dados = [[120.5]]  # Pode ser uma lista de listas para scikit-learn

    insight = prever_preco_e_gerar_insight(dados)
    print("Insight gerado pela IA:")
    print(insight)