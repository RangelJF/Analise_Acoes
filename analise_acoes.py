import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Definição dos tickers das ações para análise
tickers = ["AAPL", "MSFT", "TSLA"]

# Baixando os dados históricos do Yahoo Finance com auto_adjust=False
data = yf.download(tickers, start="2020-01-01", end="2024-03-20", auto_adjust=False)

# Verificando as colunas do DataFrame para garantir que 'Adj Close' existe
print(data.columns)

# Verificando se a coluna 'Adj Close' está presente
if 'Adj Close' in data.columns.levels[0]:
    data = data['Adj Close']
else:
    # Se 'Adj Close' não estiver disponível, usaremos 'Close'
    data = data['Close']

# Salvando os dados em CSV para inclusão no repositório
data.to_csv("dados_acoes.csv")

# Calculando os retornos diários das ações
returns = data.pct_change().dropna()

# Estatísticas básicas
stats = returns.describe()

# Calculando volatilidade anualizada
volatility = returns.std() * (252 ** 0.5)

# Gerando um gráfico de preços ajustados
plt.figure(figsize=(12, 6))
for ticker in tickers:
    plt.plot(data[ticker], label=ticker)
plt.legend()
plt.title("Preços Ajustados das Ações")
plt.xlabel("Data")
plt.ylabel("Preço ($)")
plt.grid()
plt.savefig("precos_acoes.png")

# Salvando estatísticas em Excel
with pd.ExcelWriter("analise_financeira.xlsx") as writer:
    data.to_excel(writer, sheet_name="Precos Historicos")
    returns.to_excel(writer, sheet_name="Retornos Diarios")
    stats.to_excel(writer, sheet_name="Estatisticas")
    volatility.to_frame(name="Volatilidade").to_excel(writer, sheet_name="Volatilidade")

print("Análise concluída! Arquivos gerados: dados_acoes.csv, analise_financeira.xlsx, precos_acoes.png")
