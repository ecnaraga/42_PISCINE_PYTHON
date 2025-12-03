from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Program that generate a graph for
    """
    try:
        df = load("population_total.csv")
        df = df.truncate(after="2050", axis="columns")
        # Transforme the data str->float and supress the last char(M)
        df.loc["Belgium"] = df.loc["Belgium"].apply(lambda x: float(x[:-1])
                                                    if x[-1] == "M"
                                                    else
                                                    (float(x[:-1]) * 0.001
                                                     if x[-1] in "Kk"
                                                     else float(x) * 0.000001)
                                                    )
        df.loc["France"] = df.loc["France"].apply(lambda x: float(x[:-1])
                                                  if x[-1] == "M"
                                                  else
                                                  (float(x[:-1]) * 0.001
                                                   if x[-1] in "Kk"
                                                   else float(x) * 0.000001)
                                                  )
        # Create 2 curves(1 for each country)
        plt.plot(df.columns, df.loc["Belgium"], label='Belgium')
        plt.plot(df.columns, df.loc["France"], label='France', color='green')
        plt.legend(loc='lower right')
        # Titles
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.margins(x=0.025, y=0.05)
        # Axes scale apparence
        plt.xticks(df.columns[::40])
        plt.yticks([20, 40, 60], ["20M", "40M", "60M"])
        plt.show()
    except Exception as e:
        print("AssertionError", e)


if __name__ == "__main__":
    main()

# Explanation : lambda x: float(x[:-1]) if x[-1] == "M" else (float(x[:-1]) * 0.001 if x[-1] in "Kk" else float(x) * 0.000001)
# def function(x: str) -> float:
#     if x[-1] == "M":
#         x = float(x[:-1])
#     elif x[-1] == "K" or x[-1] == "k":
#         x = float(x[:-1])*0.001
#     else:
#         x = float(x)*0.000001
#     return x
