from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import joblib
import os

PASTA_MODELOS = "modelos"
ARQUIVO_MODELO = os.path.join(PASTA_MODELOS, "modelo_preco_milho.pkl")

def treinar_e_salvar_modelo():
    if not os.path.exists(PASTA_MODELOS):
        os.makedirs(PASTA_MODELOS)

    X, y = make_regression(n_samples=100, n_features=1, noise=10)
    modelo = LinearRegression()
    modelo.fit(X, y)
    joblib.dump(modelo, ARQUIVO_MODELO)
    print(f"Modelo salvo em {ARQUIVO_MODELO}")

if __name__ == "__main__":
    treinar_e_salvar_modelo()