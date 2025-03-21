# Análise Financeira de Ações com Python

Este projeto realiza uma análise financeira de ações utilizando dados históricos de preços do Yahoo Finance. O código coleta os preços ajustados das ações, calcula os retornos diários, gera gráficos e salva as estatísticas em arquivos CSV e Excel para análise posterior.

## Funcionalidades

- **Coleta de Dados**: Baixa os dados históricos das ações selecionadas diretamente do Yahoo Finance.
- **Cálculo de Retornos Diários**: Calcula os retornos diários das ações com base nos preços ajustados.
- **Estatísticas Básicas**: Exibe estatísticas básicas dos retornos diários, como média, desvio padrão, entre outros.
- **Volatilidade Anualizada**: Calcula a volatilidade anualizada dos retornos diários.
- **Gráficos**: Gera um gráfico com os preços ajustados das ações ao longo do tempo.
- **Armazenamento de Resultados**: Salva os dados, as estatísticas e o gráfico gerado em arquivos CSV e Excel para análise posterior.

## Como Utilizar

### Requisitos

- Python 3.x
- Bibliotecas Python: `pandas`, `yfinance`, `matplotlib`
  
Você pode instalar as bibliotecas necessárias usando o `pip`:

```bash
pip install pandas yfinance matplotlib
