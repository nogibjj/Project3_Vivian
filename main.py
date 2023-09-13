import matplotlib.pyplot as plt
import polars as pl
import pandas as pd

def f():
    df = pl.read_csv("california_housing_train.csv")

    print(df.shape)
    print(len(df))
    print(df.describe())

    # Bottom 3 house price
    sorted_by_value = df.sort("median_house_value").limit(3)
    # Calculate the median/mean/standard deviation for the 2022 numbers
    median = df.select("median_house_value").drop_nulls().median()
    mean = df.select("median_house_value").drop_nulls().mean()
    sd = df.select("median_house_value").drop_nulls().std()
    print("Bottom 3 house price:")
    print(sorted_by_value)
    print("median is: " + str(median))
    print("mean is: " + str(mean))
    print("standard deviation is: " + str(sd))

    # Plot a histogram for the house value
    data = pd.read_csv("california_housing_train.csv")['median_house_value'].dropna()

    # Create histogram
    plt.hist(data, bins=5, edgecolor="k")

    # Add labels and title
    plt.xlabel('median_house_value')
    plt.ylabel('Frequency')
    plt.title('Histogram of median house price')

    # Show plot
    plt.show()

if __name__ == "__main__":
    f()

