
distribuidora_data = {
    "sp": 67836.43,
    "rs": 36678.36,
    "mg": 29229.88,
    "es": 27165.48,
    "outros": 19849.53
}

"""Calculo do percentual de representação. """

total = 0

for value in distribuidora_data.items():
    total += value[1]

for state, percentage in distribuidora_data.items():
    print(f"{state}: {round((percentage/total) * 100, 2)} %")

