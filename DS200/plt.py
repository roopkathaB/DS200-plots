import numpy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np

N = 8
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)
colors = np.random.rand(N)
area = (20)**2


def line(data):
    fig, ax = plt.subplots()
    data = data[data["Area"] == "Rural"]
    data = data[data["Gender"] == "Female"].iloc[0, :]
    data = pd.DataFrame(data)
    plt.title("Employment Per 1000 Persons: Type wise till June 2012 (Rural/Female)")
    plt.xlabel("Years")
    plt.ylabel("Employment Per 1000 Persons")
    years = [1978, 1983, 1988, 1994, 2000, 2005, 2010, 2012]
    data = [data.iloc[i] for i in range(3, 11)]
    plt.plot(years, data, color='magenta', marker='*', markersize=10)
    plt.grid()
    plt.legend()
    plt.savefig("line.jpg", dpi=300)
    plt.show()

def scatter(data):
    fig, ax = plt.subplots()
    data = data[data["Area"] == "All"]
    data = data[data["Gender"] == "Total"].iloc[0, :]
    data = pd.DataFrame(data)
    plt.title("Employment Per 1000 Persons: Type wise till June 2012")
    plt.xlabel("Years")
    plt.ylabel("Employment Per 1000 Persons")
    years = [1978, 1983, 1988, 1994, 2000, 2005, 2010, 2012]
    data = [data.iloc[i] for i in range(3, 11)]
    plt.scatter(years, data, marker='o', c=colors, s=area)
    plt.grid()
    plt.legend()
    plt.savefig("scatter.jpg", dpi=300)
    plt.show()


def box(data):
    sikkim_data = data[data["State"] == "Sikkim"]
    districts = sikkim_data["District"].unique()
    filtered_data = sikkim_data[["District", "Avg_rainfall"]]
    x = filtered_data[filtered_data["District"] == "East"]["Avg_rainfall"]
    plot_data = []
    for district in districts:
        plot_data.append(filtered_data[filtered_data["District"] == district]["Avg_rainfall"].to_numpy())
    numpy.asarray(plot_data)
    fig, ax = plt.subplots()
    plt.title("Box Plots - Avg Rainfall Sikkim Districts")
    plt.xlabel("Districts")
    plt.ylabel("Average Rainfall")
    plt.boxplot(plot_data)
    plt.grid()
    plt.setp(ax, xticks=[y + 1 for y in range(len(plot_data))],
             xticklabels=districts)
    plt.savefig("box.jpg", dpi=300)
    plt.show()



if __name__ =="__main__":
    data = pd.read_csv("./data/Employment_Participation_Per_1000_Persons_typewise_1.csv")
    box_data = pd.read_csv("./data/rainfall.csv")
    # scatter(data)
    # line(data)
    box(box_data)