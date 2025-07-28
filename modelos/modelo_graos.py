import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Simulando base de dados de grãos
dados = {
    'peso': [15.2, 14.7, 13.5, 16.8, 18.0, 20.1, 22.5, 23.0],
    'tamanho': [5.1, 4.9, 4.5, 5.8, 6.0, 6.3, 6.9, 7.1],
    'umidade': [12, 14, 13, 11, 10, 9, 8, 7],
    'tipo_grao': ['soja', 'soja', 'soja', 'milho', 'milho', 'milho', 'trigo', 'trigo']
}

# Convertendo pra DataFrame
df = pd.DataFrame(dados)

# Separando features e rótulos
X = df[['peso', 'tamanho', 'umidade']]
y = df['tipo_grao']

# Dividindo treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de Random Forest
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Avaliação
y_pred = modelo.predict(X_test)
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

# Salvando o modelo treinado
joblib.dump(modelo, 'modelo_classificacao_graos.pkl')