"""Robi module."""
__author__ = "Hendrig"


def decide(sensor_data, current_state):
    """
    Decide in which direction should robot move using sensor_data and current_state.

    Robi can move up to one index to left or right.

    Args:
        List of blocking objects in specific direction.
        0  - Free
        -1  - Object
        sensor_data - [n, ne, e, se, s, sw, w, nw]

    Return:
    One of the possible directions.
    """
    if len(sensor_data) != 8:
        return None

    state_dict = {
        "N": 0, "NE": 1, "E": 2,
        "SE": 3, "S": 4, "SW": 5,
        "W": 6, "NW": 7
    }
    try:
        current_state = state_dict[current_state]
    except KeyError:
        return None

    if current_state != 0:
        new_sensor_data = [0, 0, 0, 0, 0, 0, 0, 0]
        new_sensor_data[0: (8 - current_state)] = sensor_data[current_state:]
        new_sensor_data[(8 - current_state):] = sensor_data[0: current_state]
    else:
        new_sensor_data = sensor_data

    check_list = [-1, 0, 1]

    for i in check_list:
        if new_sensor_data[i] == 0:
            return i

    return None
