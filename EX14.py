"""Create matplotlib graphs of Estonian population from 1965-2015."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import csv


def get_series(series):
    """
    Return dictionary (key=year, value=population) according to "series".

    Possible arguments are "Vanuseruhmad kokku", "15-19", "20-24", "25-29"
    """
    with open(series + '.csv', 'r', encoding='latin-1') as f:
        reader = csv.reader(f)
        counter = 0
        return_data = []
        for row in reader:
            if counter == 4:
                return_data.append(row[0][21::])
            elif counter > 4 and counter < 55:
                return_data.append(row[0][6::])
            counter += 1
    return return_data


def save_plot(series_axis1, series_axis2, filename):
    """
    Save graph made from data, which name is given with "filename".

    Args:
    series_axis1 - dictionary containing keys (1965-2015) and values according
    to population at current year
    filename - name of the file to save the graph as

    Returns  -1
    """
    if series_axis1 is None:
        return None
    if series_axis2 is None:
        return None

    fig, fig1 = plt.subplots()

    fig2 = fig1.twinx()

    year_list = []
    for i in range(1965, 2016):
        year_list.append(i)

    population_list = []
    for i in range(0, 51):
        population_list.append(int(series_axis1[i]))

    population_list2 = []
    for i in range(0, 51):
        population_list2.append(int(series_axis2[i]))

    fig1.plot(year_list, population_list, "b-")
    fig2.plot(year_list, population_list2, "r-")

    fig1.axis([min(year_list),
               max(year_list),
               int(min(population_list)),
               int(max(population_list))])

    fig2.axis([min(year_list),
               max(year_list),
               int(min(population_list2)),
               int(max(population_list2))])

    fig1.set_ylabel("population", color="b")
    fig2.set_ylabel("population", color="r")

    fig1.set_xlabel("year")

    plt.savefig(filename, bbox_inches='tight')

if __name__ == '__main__':
    save_plot(get_series("Vanuseruhmad kokku"), get_series("15-19"), "c")
