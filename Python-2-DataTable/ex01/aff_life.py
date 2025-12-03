from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Program that generate a graph for life expectancy in France
    """
    try:
        data = load("life_expectancy_years.csv")
        # # To print the infos of the DataFrame
        # data.info()
        # # If you want to create a new dataFrame with a particular row
        # data_france = data.filter(["France"], axis=0)
        # Select columns on axe x and the row, indexed France, values on axe y
        plt.plot(data.columns, data.loc["France"])
        plt.title("France Life expectancy Projections")
        plt.xticks(data.columns[::40])  # Print a colums on 40 in the x'axe
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
