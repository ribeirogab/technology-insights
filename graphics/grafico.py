import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (15,7)

xls = pd.ExcelFile('data.xls)
df1 = pd.read_excel(xls, "ABA1")
df2 = pd.read_excel(xls, 'ABA2')