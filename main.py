import pandas as pd
import matplotlib.pyplot as plt


despesas = pd.DataFrame(columns=["Data", "Descrição", "Valor", "Categoria"])

def adicionar_despesa(data, descricao, valor, categoria):
    global despesas
    despesa = {"Data": data, "Descrição": descricao, "Valor": valor, "Categoria": categoria}
    despesas = despesas.append(despesa, ignore_index=True)

def resumo_gastos_por_categoria():
    global despesas
    return despesas.groupby("Categoria")["Valor"].sum()

def gerar_grafico():
    resumo = resumo_gastos_por_categoria()
    resumo.plot(kind="bar")
    plt.xlabel("Categoria")
    plt.ylabel("Valor")
    plt.title("Gastos por Categoria")
    plt.show()

adicionar_despesa("2022-10-25", "Compras de supermercado", 850.0, "Alimentação")
adicionar_despesa("2022-10-26", "Combustível", 502.0, "Transporte")
gerar_grafico()
