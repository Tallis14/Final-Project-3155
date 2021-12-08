# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y
data = pd.read_csv('balance_by_age.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("US Student Debt")
plt.xlabel("Years")
plt.ylabel("Amount of Debt in billions")

# save the plot
plt.savefig("LineChart.png")
