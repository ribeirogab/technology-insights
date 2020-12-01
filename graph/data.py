import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (15,7)

file = pd.ExcelFile("../data/data.xlsx")
tabs = []
tabs.append(file.sheet_names)

def choose_tab():
    for i in range(len(tabs[0])):
        print(f'{i} - {tabs[0][i]}')

    print("\nEscolha a opção a ser mostrada (número): ")
    option_tab = int(input())

    print("\n1 - Barra\n2 - Pizza\n3 - Linha")
    print("\nEscolha o gráfico desejado (número): ")
    option_graph = int(input())

    show_graphic(option_tab, option_graph)

def show_graphic(option_tab, option_graph):
    df = pd.read_excel(file, option_tab)
    tech = []
    percentage = []

    for row in df.iterrows():
        tech.append(row[1].tech)
        percentage.append(row[1].percentage)

    for i in range(len(tabs[0])):
        if(i == option_tab):
            title = tabs[0][i]

    if option_graph == 1:
        plt.bar(tech, percentage, color="blue")

        plt.xticks(tech)
        plt.ylabel("Porcentagem")
        plt.xlabel("Tecnologias")
        plt.title(title)
        plt.show()
    
    elif option_graph == 2:
        pass # fazer

    elif option_graph == 3:
        pass # fazer
    
    else:
        print("Opção inválida, tente novamente!\n")
        choose_tab()

choose_tab()