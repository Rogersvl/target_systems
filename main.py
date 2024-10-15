import json
import pandas as pd
""" first question """

indi = 13
k = 0
soma = 0
while k < indi:
    k = k + 1
    soma = soma + k
#print(soma)

"""end of first question"""


"""Fibonacci question"""


def fibonacci(n):
    fibo_sequence = []
    a = 0
    b = 1
    c = 0
    while c <= n:
        fibo_sequence.append(c)
        c = a + b
        a = b
        b = c
    if n in fibo_sequence:
        print(f" {n} faz parte da sequencia")
    else:
        print(f" {n} não faz parte da sequencia")


fibonacci(5)


df = pd.read_json("dados.json")
df = df[(df[['dia', 'valor']] != 0).all(axis=1)]
new_df = df.set_index("dia")
month_sum = sum(new_df["valor"]) / len(new_df)
n_days = 0

for valor in new_df["valor"]:
    if valor > month_sum:
        n_days += 1

print(f" Menor valor faturado em um mês: {round(min(new_df[f'valor']), 2)}\n Maior valor faturado em um mês "
      f"{round(max(new_df['valor']), 2)}\n Número de dias em que faturamento diário maior que a média mensal: {n_days}")






