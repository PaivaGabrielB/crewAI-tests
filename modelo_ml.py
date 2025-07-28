import joblib
import os

MODELO_PATH = "modelos/modelo_preco_milho.pkl"

def prever_preco(dados):
    if not os.path.exists(MODELO_PATH):
        raise FileNotFoundError(f"Modelo não encontrado em {MODELO_PATH}. Execute o script de treinamento primeiro.")
    
    modelo = joblib.load(MODELO_PATH)
    previsao = modelo.predict(dados)
    return previsao[0]