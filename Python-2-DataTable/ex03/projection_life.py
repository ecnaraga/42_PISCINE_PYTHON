from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Program that displays the projection of life expectancy in relation to the
    gross national product of the year 1900 for each country
    """
    try:
        df_gdp = (
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
        df_le = load("life_expectancy_years.csv")
        # Keep only year 1900
        df_gdp = df_gdp.truncate(before="1900", after="1900", axis="columns")
        df_le = df_le.truncate(before="1900", after="1900", axis="columns")
        # Use df_gdp for x axe and df_le for y_axe
        plt.plot(df_gdp, df_le, 'o')  # 'o' for points
        # Titles
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        # Axe scale
        plt.xscale('log')  # More space to 1e0-1e1 than 1e1-1e2 than 1e2-1e3...
        plt.xticks([300, 1.e3, 1.e4], ['300', '1k', '10k'])
        plt.show()
    except Exception as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
