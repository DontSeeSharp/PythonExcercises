"""Robot for EX07."""
import random
from random import randint
import simulator


class Robot(simulator.Agent):

    """Main class for robot."""

    def __init__(self, world, x, y, direction):
        """Take variables from simulator.py."""
        simulator.Agent.__init__(self, world, x, y, direction)

    def generate_possible_moves(self):
        """
        Generate a list, which contains a direction depending on the direction.

        For example if robot is faced to north(0), then possible_moves[-1] == 7

        Returns:
        A list which is described earlier
        """
        direction = self.compass()
        print("direction is: " + str(direction))

        possible_moves = []
        straight = direction
        little_right = (direction + 1) % 8
        right = (direction + 2) % 8
        left = (direction - 2) % 8
        little_left = (direction - 1) % 8

        possible_moves.append(straight)
        possible_moves.append(little_right)
        possible_moves.append(right)
        possible_moves.append(left)
        possible_moves.append(little_left)

        return possible_moves

    def decide_right_or_left(self, surroundings, possible_moves, rand_dir):
        """
        Decide if left or right direction is free for robot.

        Takes:
        surroundings (list)
        possible moves (list)
        rand_dir (integer -2 or 2)
        Returns:
        If robot cannot go left or right, return 0
        If robot can got right or left, returns right or left (depending on rand_dir)
        """
        rand_movement = rand_dir
        print(surroundings[possible_moves[rand_dir]])
        if len(surroundings[possible_moves[rand_dir]]) == 3:
            print("left_esimene tingimus taidetud")
            rand_movement = rand_dir

        elif len(surroundings[possible_moves[rand_dir]]) == 1:
            if surroundings[possible_moves[rand_dir]][0] != -1 and surroundings[possible_moves[rand_dir]][0] != -2 and surroundings[possible_moves[rand_dir]] != [-1, -1, -1]:
                rand_movement = rand_dir
            elif surroundings[possible_moves[-rand_dir]][0] != -1 and surroundings[possible_moves[-rand_dir]][0] != -2 and surroundings[possible_moves[-rand_dir]] != [-1, -1, -1]:
                rand_movement = -rand_dir
            else:
                print("NO POSSIBLE WAY TO GO!!!")
                rand_movement = 0
        return rand_movement

    def move_right_or_left(self, surroundings, possible_moves):
        """
        Generate random left or right direction and check if direction is free.

        Returns:
        If direction is free, return direction.
        If it isn't return 0
        """
        print("Got random movement from left_right")
        decision_left_right = random.randint(0, 1)
        if decision_left_right == 0:
            rand_movement = Robot.decide_right_or_left(
                self, surroundings, possible_moves, -2)
        elif decision_left_right == 1:
            rand_movement = Robot.decide_right_or_left(
                self, surroundings, possible_moves, 2)

        return rand_movement

    def decide_if_corner(self, surroundings, possible_moves, move):
        """
        Decide if robot is heading to a corner.

        Returns:
        decide (integer 1 or 0)
        If it is heading to a corner, return 0
        If it isn't heading to a corner, return 1
        """
        decide = 1
        for i in surroundings[possible_moves[move]]:
            if all(i < 0 for i in surroundings[possible_moves[move]]):
                decide = 0
            if i == -3:
                decide = 1
                break
        return decide

    def decide(self):
        """
        Moving algorithm for robot.

        If moving direction is free, robot tries to move in the direction.
        When a corner, obstacle is visible, robot tries to avoid it and then generates a random direction.
        When robot sees a treasure with sensors, it chooses direction of the treasure
        Returns:
        random_movement (integer -2 to 2)
        """
        surroundings = []
        for i in range(8):
            surroundings.append(self.detect(i))
        print(len(surroundings))
        print(surroundings)

        possible_moves = Robot.generate_possible_moves(self)

        rand_movement = randint(-2, 2)

        if len(surroundings[possible_moves[0]]) == 3:
            if surroundings[possible_moves[0]][1] == 111:
                print("Trying to move straight")
                rand_movement = 0

        if Robot.decide_if_corner(self, surroundings, possible_moves, rand_movement) == 0:
            while Robot.decide_if_corner(self, surroundings, possible_moves, rand_movement) == 0 or surroundings[possible_moves[rand_movement]] == -2:
                if Robot.decide_if_corner(self, surroundings, possible_moves, rand_movement) != 0 and surroundings[possible_moves[rand_movement]] != -2:
                    print("Generated new movement!")
                    break
                rand_movement = randint(-2, 2)

        print("Chose direction: " + str(rand_movement))

        for i in range(-2, 3):
            if len(surroundings[possible_moves[i]]) == 1:
                if surroundings[possible_moves[i]][0] == -3:
                    rand_movement = i
                    print(
                        "Got random movement from found treasure from 1! YAY!")
            elif len(surroundings[possible_moves[i]]) == 3:
                for a in range(3):
                    if surroundings[possible_moves[i]][a] == -3:
                        rand_movement = i
                        print(
                            "Got random movement from found treasure from 3! YAY!")

        if surroundings[possible_moves[rand_movement]][0] == -3:
            print("Passed for treasure")
            pass

        elif len(surroundings[possible_moves[rand_movement]]) == 3:
            print("Got random movement from randint!!!")
            for i in surroundings[possible_moves[rand_movement]]:
                print(i)

        else:
            rand_movement = Robot.move_right_or_left(
                self, surroundings, possible_moves)

        print("Rand_movement is: " + str(rand_movement))
        self.turn_and_drive_straight(rand_movement)

if __name__ == "__main__":
    world = simulator.World(
        width=10, height=10, sleep_time=0.1, reliability=1, treasure=(-1, -1), obstacles=[(1, 0)])
    robots = []
    robots.append(Robot(world, 0, 0, 4))  # add more robots here if you like

    for _ in range(100000):  # Simulate 50 ticks
        world.print_state()
        for robot in robots:
            robot.decide()
        world.print_state()
        world.tick()
