from crewai import Crew, Agent, Task
from tools import prever_preco_milho_tool
from dotenv import load_dotenv

load_dotenv()
# Define o agente que vai usar a ferramenta
analista = Agent(
    role="Analista de mercado",
    goal="Analisar os preços do milho e gerar um insight útil para decisões de negócios",
    backstory="Você é um especialista em agronegócio, com foco na análise de preços do milho.",
    tools=[prever_preco_milho_tool],  # Aqui usamos a ferramenta
    verbose=True
)

# Define a tarefa
tarefa = Task(
    description="Utilize dados históricos de preços do milho para prever o preço e gerar um insight.",
    expected_output="Um insight claro sobre a tendência futura do preço do milho.",
    agent=analista
)

# Cria e executa a crew
crew = Crew(agents=[analista], tasks=[tarefa], verbose=True)
resultado = crew.kickoff()

print("\nResultado final:")
print(resultado)