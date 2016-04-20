__author__ = 'Hendrig Sellik'
"""
Create a  minefield from given mine postisions and field size.

Input:
mines - (a list of tuples containing mine position for example [(0, 1), (2, 3)])
layers - an integers

Output:
A list of 1*layers lists[a,a,a,a] with a's marked with 0(nothing) or X's(mines).
"""


def assign_mines(mines, layers):
    """
    Make a list where mines are marked with 'X' and empty places with 0.

    Input:
    mines - (a list of tuples containing mine position for example [(0, 1), (2, 3)])
    layers - an integers

    Output:
    A list of 1*layers lists[a,a,a,a] with a's marked with 0(nothing) or X's(mines).
    """
    if layers <= 0:
        return []

    else:
        mine_list = [[0, 0, 0, 0] for x in range(layers + 1)]

        for i in range(len(mines)):
            a = mines[i][0]
            b = mines[i][1]
            if a >= 0 and a <= layers and b >= 0 and b <= 3:
                mine_list[a][b] = 'X'

    return mine_list


def create_mine_map(mines, layers):
    """
    Create a polar_map of mines marked with x's and numbers that represent the number of nearby mines.

    Input:
    mines - (a list of tuples containing mine position for example [(0, 1), (2, 3)])
    layers - an integers

    Output:
    A list of n*layer element, each holding 4 elements. Mines are marked with X's and other elements
    with the number of mines that are nearby.
    """
    polar_map = assign_mines(mines, layers)
    if polar_map != []:
        for numbers, values in enumerate(polar_map):         # Numbers equals the count of layers and values equals to the value of the layer
            for numbers1, values1 in enumerate(values):      # Numbers1 equals the element of layers and values1 equals to the value of values[numbers1]
                if values1 == 'X':
                    value_number = numbers1
                    next_layer = numbers + 1
                    previous_layer = numbers - 1

                    # Adds to sides of current layer
                    if (value_number + 1) == 4:
                        if polar_map[numbers][0] != 'X':
                            polar_map[numbers][0] += 1
                    else:
                        if polar_map[numbers][value_number + 1] != 'X':
                            polar_map[numbers][value_number + 1] += 1

                    if (value_number - 1) == -1:
                        if polar_map[numbers][3] != 'X':
                            polar_map[numbers][3] += 1
                    else:
                        if polar_map[numbers][value_number - 1] != 'X':
                            polar_map[numbers][value_number - 1] += 1

                    # Add to side of next layer
                    if next_layer < layers:
                        if (value_number + 1) == 4:
                            if polar_map[next_layer][0] != 'X':
                                polar_map[next_layer][0] += 1
                        else:
                            if polar_map[next_layer][value_number + 1] != 'X':
                                polar_map[next_layer][value_number + 1] += 1

                        if (value_number - 1) == -1:
                            if polar_map[next_layer][3] != 'X':
                                polar_map[next_layer][3] += 1
                        else:
                            if polar_map[next_layer][value_number - 1] != 'X':
                                polar_map[next_layer][value_number - 1] += 1

                    # Add to side of previous layer
                    if previous_layer >= 0:
                        if (value_number + 1) == 4:
                            if polar_map[previous_layer][0] != 'X':
                                polar_map[previous_layer][0] += 1
                        else:
                            if polar_map[previous_layer][value_number + 1] != 'X':
                                polar_map[previous_layer][value_number + 1] += 1

                        if (value_number - 1) == -1:
                            if polar_map[previous_layer][3] != 'X':
                                polar_map[previous_layer][3] += 1
                        else:
                            if polar_map[previous_layer][value_number - 1] != 'X':
                                polar_map[previous_layer][value_number - 1] += 1

                    # Adds to corners of next and previous layer
                    if numbers + 1 < layers:
                        if polar_map[numbers + 1][numbers1] != 'X':
                            polar_map[numbers + 1][numbers1] += 1
                    if numbers - 1 >= 0:
                        if polar_map[numbers - 1][numbers1] != 'X':
                            polar_map[numbers - 1][numbers1] += 1

                    # Adds to the corners of the 0 layer
                    if numbers == 0:
                        if value_number == 0:
                            if polar_map[0][2] != 'X':
                                polar_map[0][2] += 1

                        if value_number == 1:
                            if polar_map[0][3] != 'X':
                                polar_map[0][3] += 1

                        if value_number == 2:
                            if polar_map[0][0] != 'X':
                                polar_map[0][0] += 1

                        if value_number == 3:
                            if polar_map[0][1] != 'X':
                                polar_map[0][1] += 1
    if polar_map != []:
        del polar_map[-1]
    return polar_map
