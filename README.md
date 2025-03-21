# Análise Financeira de Ações

Este repositório contém um script em Python que realiza uma análise financeira de ações utilizando a biblioteca `yfinance`. O script baixa os dados históricos de preços de algumas empresas, calcula estatísticas relevantes e gera arquivos de saída para auxiliar na tomada de decisão.

## Funcionalidades
- Download de dados históricos de preço das ações da Apple (AAPL), Microsoft (MSFT) e Tesla (TSLA) utilizando `yfinance`.
- Cálculo de retornos diários e estatísticas descritivas.
- Cálculo da volatilidade anualizada das ações.
- Geração de um gráfico de preços ajustados.
- Exporta os dados para arquivos CSV e Excel.

## Requisitos
Para rodar o script, é necessário ter Python instalado e as seguintes bibliotecas:

```bash
pip install pandas yfinance matplotlib openpyxl
```

## Como Rodar o Script

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```
2. Instale as dependências conforme indicado na seção de requisitos.
3. Execute o script:
   ```bash
   python nome_do_script.py
   ```

## Saídas Geradas
Após a execução, os seguintes arquivos serão gerados no diretório:
- `dados_acoes.csv` - Contém os preços históricos das ações.
- `analise_financeira.xlsx` - Arquivo Excel com abas para preços históricos, retornos diários, estatísticas e volatilidade.
- `precos_acoes.png` - Gráfico dos preços ajustados das ações.



