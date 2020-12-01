import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['figure.figsize'] = (15,7)

file = pd.ExcelFile(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', './data/data.xlsx')))
tabs = []
tabs.append(file.sheet_names)

def choose_tab():
    for i in range(len(tabs[0])):
        print(f'{i + 1} - {tabs[0][i]}')

    option_tab = int(input("\nEscolha a opção a ser mostrada (número): ")) - 1

    while option_tab >= len(tabs[0]) or option_tab < 0:
      print("\nOpção inválida!")
      option_tab = int(input("\nEscolha a opção a ser mostrada (número): ")) - 1

    print("\n1 - Barra (RECOMENDADO)\n2 - Pizza\n3 - Linha")
    option_graph = int(input("\nEscolha o gráfico desejado (número): "))

    while option_graph > 3 or option_graph <= 0:
      print("\nOpção inválida!\n\n1 - Barra (RECOMENDADO)\n2 - Pizza\n3 - Linha")
      option_graph = int(input("\nEscolha a opção a ser mostrada (número): ")) - 1

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
        plt.barh(tech, percentage, color="blue")

        plt.xlabel("Porcentagem")
        plt.title(title)
        plt.show()

    elif option_graph == 2:
        plt.rcParams ['axes.titlepad'] = 30
        plt.pie(percentage, labels=tech, autopct='%1.1f%%', shadow=False)
        plt.title(title)
        plt.axis('equal')
        plt.show()

    elif option_graph == 3:
        plt.plot(percentage, tech)
        plt.title(title)
        plt.show()

    else:
        print("Opção inválida, tente novamente!\n")
        choose_tab()
