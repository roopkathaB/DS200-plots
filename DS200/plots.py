import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)


def countries_population_trends_plot(data: pd.DataFrame, country_name: str) -> None:
    country_data = data[data["Country"] == country_name]
    years = [1980, 1990, 2000, 2010, 2015, 2020, 2022]
    plot_data = [country_data[f"{i} Population"].iloc[0] for i in years]
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.plot(years, plot_data, "ob-", markersize=10)
    plt.xlabel("Year", fontsize=20)
    plt.ylabel("Population", fontsize=20)
    plt.grid()
    plt.title(f"Population Over Years ({country_name})", fontsize=20)
    plt.savefig(f"./plots/{country_name}.jpg", dpi=300)
    plt.show()


def country_vs_country_population_plot(data: pd.DataFrame, country_1: str, country_2: str = "India") -> None:
    country_1_data = data[data["Country"] == country_1]
    country_2_data = data[data["Country"] == country_2]
    years = [1980, 1990, 2000, 2010, 2015, 2020, 2022]
    plot_1_data = [country_1_data[f"{i} Population"].iloc[0] for i in years]
    plot_2_data = [country_2_data[f"{i} Population"].iloc[0] for i in years]
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.plot(years, plot_1_data, "ob-", label=f"{country_1}", markersize=10)
    plt.plot(years, plot_2_data, "or-", label=f"{country_2}", markersize=10)
    plt.xlabel("Year", fontsize=20)
    plt.ylabel("Population", fontsize=20)
    plt.grid()
    plt.title(f"Population Over Years - {country_1} vs {country_2}", fontsize=20)
    plt.savefig(f"./plots/{country_1}vs{country_2}.jpg", dpi=300)
    plt.legend()
    plt.show()
    pass



def continents_population_plot(data: pd.DataFrame) -> None:
    pass


if __name__ == "__main__":
    csv_data = pd.read_csv("./data/world_population.csv")
    # countries_population_trends_plot(data=csv_data, country_name="Italy")
    country_vs_country_population_plot(data=csv_data, country_1="China")

