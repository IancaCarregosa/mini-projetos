import json

dados_faturamento = """
[
    {"dia": 1, "faturamento": 1000.0},
    {"dia": 2, "faturamento": 2000.0},
    {"dia": 3, "faturamento": 0.0},
    {"dia": 4, "faturamento": 500.0},
    {"dia": 5, "faturamento": 0.0},
    {"dia": 6, "faturamento": 3000.0},
    {"dia": 7, "faturamento": 4000.0}
]
"""

faturamento_diario = json.loads(dados_faturamento)
faturamento_valores = [dia["faturamento"] for dia in faturamento_diario if dia["faturamento"] > 0]

menor_faturamento = min(faturamento_valores)
maior_faturamento = max(faturamento_valores)
media_mensal = sum(faturamento_valores) / len(faturamento_valores)
dias_acima_media = sum(1 for valor in faturamento_valores if valor > media_mensal)

print(f"Menor faturamento diário: {menor_faturamento}")
print(f"Maior faturamento diário: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
