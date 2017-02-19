from ship_old_new import iterate_until_valid, field_to_str

# play = Player("Luka")
# print(play._name)
# field1 = iterate_until_valid()
# field2 = iterate_until_valid()
# print(field1)
# print(field2)agi


class Player:

    def __init__(self, name):
        self.name = name

    def read_position(self):
        while True:
            move = input("Please make your move, (example: A1): ")
            if 106 >= ord(move[0].lower()) >= 97 and int(move[1:]) <= 10:
                moves = (int(move[1:]) - 1, ord(move[0].lower()) - 97)
                break
            else:
                print("You entered wrong coordinates")
        return moves


class Ship:

    def __init__(self, bow=(0, 0), horizontal=False, length=0):
        self.bow = bow
        self.horizontal = horizontal
        self.length = length
        self.hit = [None for _ in range(self.length)]




# ship = Ship()
# print(ship)
# print(ship)


class Field:

    def __init__(self):
        self.ships = [iterate_until_valid(), iterate_until_valid()]
        self.shooted = []

    def shoot_at(self, coors):
        self.shooted.append(coors)
        shot = self.ships[0][coors[0]][coors[1]]
        # if shot == '*':
        #     print("you've injured a ship")
        #     print(shot)
        #     print(self.ships[0][coors[0]])
        # elif shot == ' ':
        #     print("missed")
        #     field_to_str(self.ships[0])
        return self.ships[coors[0] - 1][coors[1] - 1].shoot_at(coors)  #

    def get_ships(self):  #
        return self.ships  #



# print(play.name)


class Game:
    """ (list, list, int) ->
    The mother of all classes
    """

    def __init__(self):
        print("WELCOME TO THE NEW GAME")
        player_1_name = input("Player 1, enter your name: ")
        player_2_name = input("Player 2, enter your name: ")
        self.players = [Player(player_1_name), Player(player_2_name)]
        self.fields = Field().ships  # creates random fields for players
        self.ships_alive = [10, 10]
        # print("Player 1, this is your field:")
        # field_to_str(fields[0])
        # print("Player 2, this is your field:")
        # field_to_str(fields[1])
        # self.current_player = 0

    def field_without_ships(self, index):  #
        return self.fields[index].field_without_ships()  #

    def field_with_ships(self, index):  #
        return self.fields[index].field_with_ships()  #



game = Game()
game.play()
# print(game.read_position())
# coordinates = game.read_position()
# Field.shoot_at(coordinates)s

# Game.field_without_ships()
