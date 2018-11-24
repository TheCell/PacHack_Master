from app.dto.ReturnDirections import ReturnDirections

class Strategy:
    def __init__(self, game_field, my_player, my_position):
        self.game_field = game_field
        self.my_player = my_player
        self.my_position = my_position
        self.choice = ReturnDirections.random()

    def get_move(self):
        print(str(self.my_player))
        return self.choice
