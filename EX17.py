"""EX17."""
import alienutils
import bisect
import timeit
import matplotlib.pyplot as plt
import math


def wrapper(func, *args, **kwargs):
    """Wrap function."""
    def wrapped():
        """Function for timeit."""
        return func(*args, **kwargs)
    return wrapped


def linear_search(alien_list, alien_to_search):
    """
    Search alien using linear search algorithm.

    Args:
    alien_list - a list of aliens to search from
    alien_to_search - alien to search
    Returns:
    found alien
    """
    for alien in alien_list:
        if alien == alien_to_search:
            return alien


def binary_search(alien_list, alien_to_search):
    """
    Search alien using binary search algorithm.

    Args:
    alien_list - a sorted alien list
    alien_to_search - alien to search
    Returns:
    Found alien
    """
    found_alien = 0
    alien_index = bisect.bisect_left(alien_list, str(alien_to_search))
    if str(alien_list[alien_index]) == str(alien_to_search):
        found_alien = alien_to_search
    return found_alien


def sort_list(unsorted_alien_list):
    """Sort unsorted_alien_list alphabetically."""
    return str(sorted(unsorted_alien_list, key=lambda alien: alien.name))


def sorting_binary_search(alien_list, alien_to_search):
    """
    Sort alien list and then use binary search algorithm to find the alien.

    Args:
    alien_list - an unsorted alien list
    alien_to_search - alien to search
    Returns:
    found_alien - alien that was found
    """
    found_alien = None

    alien_list = sorted(alien_list)

    alien_index = bisect.bisect_left(alien_list, alien_to_search)

    if alien_list[alien_index] == alien_to_search:
        found_alien = alien_to_search

    return found_alien


def test_alien_amounts(alien_amount, test_amount=100):
    """
    Test linear, sorting+binary search and sorting+ multiple binary search algorithms.

    Args:
    alien_amount - number of aliens to sesarch from
    test_amount - number of times to test each algorithm.
    Returns:
    linear_time - time of performing all linear searches
    sorting_binary_time - time of performing sorting + binary search algorithms
    binary_time + sorting time - time of performing binary searches + the first sort time
    """
    gen = alienutils.AlienGenerator()
    aliens = gen.get_aliens(alien_amount)

    linear_time = 0
    sorting_binary_time = 0
    binary_time = 0
    sorting_time1 = 0

    wrapped = wrapper(sort_list, aliens)
    sorting_time = timeit.timeit(wrapped, number=1)

    str_aliens = []
    for alien in aliens:
        str_aliens.append(str(alien))

    for _ in range(test_amount):
        search_alien = next(gen.get_search_aliens())

        wrapped1 = wrapper(linear_search, str_aliens, str(search_alien))
        linear_time += timeit.timeit(wrapped1, number=1)

        wrapped2 = wrapper(
            sorting_binary_search,
            str_aliens,
            str(search_alien))
        sorting_binary_time += timeit.timeit(wrapped2, number=1)

        wrapped3 = wrapper(
            binary_search, sort_list(aliens), search_alien)
        binary_time += (timeit.timeit(wrapped3, number=1))

    gen.reset()

    return linear_time, sorting_binary_time, binary_time + \
        sorting_time, sorting_time1


def draw_graph(alien_amounts, test_amount=100):
    """Perform test_amount timeit tests on alien search from a list of alient_amounts aliens and draw the results on a graph."""
    times = []
    for i in alien_amounts:
        times.append(test_alien_amounts(i, test_amount=100))

    x_axis = []

    for i in alien_amounts:
        x_axis.append(math.log(i, 2))

    y_axis1 = []
    for i in times:
        y_axis1.append(i[0])

    y_axis2 = []
    for i in times:
        y_axis2.append(i[1])

    y_axis3 = []
    for i in times:
        y_axis3.append(i[2])

    plt.plot(x_axis, y_axis1, 'r', label="linear")

    plt.plot(x_axis, y_axis2, 'y', label="sorting_search")

    plt.plot(x_axis, y_axis3, 'b', label="binary_search")

    plt.legend(bbox_to_anchor=(0.05, 1), loc=2, borderaxespad=0.)

    plt.ylabel("time(seconds)")
    plt.xlabel(
        "Logarithm of aliens")
    plt.show()
    return 0

if __name__ == "__main__":
    draw_graph([1, 10, 100, 1000], 100)
