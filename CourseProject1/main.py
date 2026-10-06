import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("WineDatasets/winequality-white.csv", sep=";")

# Print the first few rows so you can verify it loaded correctly
print(df.head())

# Create a scatter plot
plt.scatter(df["alcohol"], df["quality"])

plt.xlabel("Alcohol")
plt.ylabel("Wine Quality")
plt.title("Alcohol Content vs Wine Quality")

plt.show()