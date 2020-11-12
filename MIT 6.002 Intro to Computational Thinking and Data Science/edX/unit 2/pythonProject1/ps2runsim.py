def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    all_steps = []
    for trial in range(num_trials):
        room = RectangularRoom(width, height)
        steps = 0
        for robot in range(num_robots):
            new_robot = robot_type(room, speed)
            while room.getNumCleanedTiles() / room.getNumTiles() < min_coverage:
                new_robot.updatePositionAndClean()
                steps += 1
        all_steps.append(steps)
    return sum(all_steps) / len(all_steps)