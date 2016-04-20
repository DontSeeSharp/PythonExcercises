"""Module for MonteCarloSimulation."""
from MockService import MockService

import random


class MonteCarloSimulation(object):

    """Class for MonteCarloSimulation."""

    def __init__(self, service):
        """
        Constructor for the simulation.

        Arguments:
            Input service
        Returns:
            Output service
        """
        self.service = service

    def get_area(self):
        """
        Monte Carlo simulation.

        Return:
        Dictionary where first part is number of the shape
        and second number is the area.
        """
        tries = self.service.tries_left()
        width = self.service.get_width()
        height = self.service.get_height()
        dict_answer = {}

        area = width * height

        for i in range(tries):
            rand_width = random.randint(0, width - 1)
            rand_height = random. randint(0, height - 1)

            info = self.service.info(rand_width, rand_height)

            if info in dict_answer:
                dict_answer[info] += 1
            else:
                dict_answer[info] = 1

        for key in dict_answer.keys():
            dict_answer[key] = (area * (dict_answer[key] / tries))

        return dict_answer

if __name__ == "__main__":
    service1 = MockService('circle_10.txt')
    service2 = MockService('circle_100.txt')
    service3 = MockService('circle_20.txt')
    service4 = MockService('circle_200.txt')
    service5 = MockService('squares.txt')

    sim1 = MonteCarloSimulation(service1)
    sim2 = MonteCarloSimulation(service2)
    sim3 = MonteCarloSimulation(service3)
    sim4 = MonteCarloSimulation(service4)
    sim5 = MonteCarloSimulation(service5)

    print(sim1.get_area())
    print(sim2.get_area())
    print(sim3.get_area())
    print(sim4.get_area())
    print(sim5.get_area())
