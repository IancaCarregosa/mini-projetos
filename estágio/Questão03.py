import json

with open('dados.json', 'r') as file:
    faturamento_diario = json.load(file)
faturamento_valores = [dia["valor"] for dia in faturamento_diario if dia["valor"] > 0]
menor_faturamento = min(faturamento_valores)
maior_faturamento = max(faturamento_valores)
media_mensal = sum(faturamento_valores) / len(faturamento_valores)
dias_acima_media = sum(1 for valor in faturamento_valores if valor > media_mensal)
print(f"Menor faturamento diário: {menor_faturamento}")
print(f"Maior faturamento diário: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
