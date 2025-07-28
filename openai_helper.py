import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_insight(prompt):
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um especialista em mercado agrícola."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta['choices'][0]['message']['content']