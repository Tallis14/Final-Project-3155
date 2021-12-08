import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv ('US_Debt.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("US Expenditure")
plt.xlabel("Years")
plt.ylabel("Amount money spent in billions")

plt.savefig("Graph2.png")

