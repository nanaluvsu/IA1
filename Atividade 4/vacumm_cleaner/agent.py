class VaccumCleaner:
    def __init__(self):
        self.side_to_move = 0  # 0 - left, 1 - right

    def act(self, environment):
        # decide which direction to move
        if environment.agent_location == 0:
            self.side_to_move = 1
        elif environment.agent_location == len(environment.room) - 1:
            self.side_to_move = 0

        # perform action: move or clean
        if environment.room[environment.agent_location] == 0:
            new_location = None
            if self.side_to_move:
                print("MOVE TO THE RIGHT")
                new_location = environment.agent_location + 1
            else:
                print("MOVE TO THE LEFT")
                new_location = environment.agent_location - 1
            environment.agent_location = new_location
        elif environment.room[environment.agent_location] == 1:
            print("CLEAN")
            environment.room[environment.agent_location] = 0
        return environment
