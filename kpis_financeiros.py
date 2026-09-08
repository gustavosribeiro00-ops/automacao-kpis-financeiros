import pandas as pd

# 1. Carregar base de dados
df = pd.read_csv("vendas_filiais.csv")

# 2. Engenharia de Recursos (KPIs Financeiros)
df["Lucro"] = df["Receita"] - df["Custo"]
df["Margem_Lucro_%"] = (df["Lucro"] / df["Receita"]) * 100

# 3. Consolidação Geral
receita_total = df["Receita"].sum()
lucro_total = df["Lucro"].sum()
margem_media = df["Margem_Lucro_%"].mean()

# 4. Relatório Executivo
print("=" * 45)
print("      DASHBOARD FINANCEIRO DE FILIAIS      ")
print("=" * 45)
print(f"Receita Total: R$ {receita_total:,.2f}")
print(f"Lucro Total:   R$ {lucro_total:,.2f}")
print(f"Margem Média:  {margem_media:.2f}%")
print("=" * 45)
print("\n--- Desempenho por Unidade ---")
print(df[["Filial", "Receita", "Lucro", "Margem_Lucro_%"]].to_string(index=False))

# 5. Exportar dados consolidados
df.to_csv("relatorio_kpis.csv", index=False)