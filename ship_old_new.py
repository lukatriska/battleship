# IMPORTANT: for the following functions to work properly make sure that the field.txt file is in the format as given.
# Letters have to be in UPPERCASE format.
import random


def has_ship(field, coors):
    """
    (data, tuple) -> (bool)
    Based on the read file returns True if there is a ship on the given coordinates, False if not.
    """
    col_num = ord(coors[0]) - 65
    row_num = field[int(coors[1]) - 1]
    if row_num[col_num] == '*':
        return True
    return False


def ship_size(field, coors):
    """
    (data, tuple) -> (tuple)
    Returns the size of a ship (integer), part of which is located on the coordinates given, if there is such a part.
    If not, returns None.
    """
    size = 0
    if has_ship(field, coors):
        size += 1
        if coors[1] + 1 <= 10 and has_ship(field, (coors[0], coors[1] + 1)):
            size += 1
            if coors[1] + 2 <= 10:
                if has_ship(field, (coors[0], coors[1] + 2)):
                    size += 1
                    if coors[1] + 3 <= 10:
                        if has_ship(field, (coors[0], coors[1] + 3)):
                            size += 1
        if coors[1] - 1 >= 1 and has_ship(field, (coors[0], coors[1] - 1)):
            size += 1
            if coors[1] - 2 >= 1:
                if has_ship(field, (coors[0], coors[1] - 2)):
                    size += 1
                    if coors[1] - 3 >= 1:
                        if has_ship(field, (coors[0], coors[1] - 3)):
                            size += 1
        if coors[0] != 'j' and coors[0] != 'J' and has_ship(field, (chr(ord(coors[0]) + 1), coors[1])):
            size += 1
            if chr(ord(coors[0]) + 1) != 'j' and chr(ord(coors[0]) + 1) != 'J':
                if has_ship(field, (chr(ord(coors[0]) + 2), coors[1])):
                    size += 1
                    if chr(ord(coors[0]) + 2) != 'j' and chr(ord(coors[0]) + 2) != 'J':
                        if has_ship(field, (chr(ord(coors[0]) + 3), coors[1])):
                            size += 1
        if coors[0] != 'a' and coors[0] != 'A' and has_ship(field, (chr(ord(coors[0]) - 1), coors[1])):
            size += 1
            if chr(ord(coors[0]) - 1) != 'a' and chr(ord(coors[0]) - 1) != 'A':
                if has_ship(field, (chr(ord(coors[0]) - 2), coors[1])):
                    size += 1
                    if chr(ord(coors[0]) - 2) != 'a' and chr(ord(coors[0]) - 2) != 'A':
                        if has_ship(field, (chr(ord(coors[0]) - 3), coors[1])):
                            size += 1
        return size


def is_valid(field):
    """
    (data) -> (bool)
    Checks if a given gamefield is a correct one according to the rules of the game. The specific amounts of times we
    find each ship I developed based on my own observations.
    """
    lst = []
    for i in range(1, 11):
        for let in 'ABCDEFGHIJ':
            if ship_size(field, (let, i)) is not None:
                lst.append(ship_size(field, (let, i)))
    if lst.count(4) == 4 and lst.count(3) == 6 and lst.count(2) == 6 and lst.count(1) == 4:
        return True
    return False


def field_to_str(field):
    """
    (data) -> (str)
    Prints the gamefield and creates a file called 'gamefield.txt' in which saves the gamefield.
    """
    with open('random_gamefield.txt', 'w') as f:
        for k in field:
            f.write("".join(k))
            f.write("\n")
    for k in range(len(field)):
        print("".join(field[k]), "\n", sep='', end="")


all_free_coor = [(i, k) for k in range(1, 11) for i in "ABCDEFGHIJ"]  # generates a free gamefield


def generate_ships(field, size, q=None):
    """
    () -> (data)
    Generates random coordinates of a ship with a given size. Returns all free coordinates left and the coordinates of
    the ship.
    """
    all_free_coor = [(i, k) for k in range(1, 11) for i in "ABCDEFGHIJ"]  # generates a free gamefield
    if q is None:
        all_free_coor_minus_used = []
    else:
        all_free_coor_minus_used = field

    try:
        coor = [(random.choice(field))]  # generates the starting coordinate of the ship
    except IndexError:
        coor = [(random.choice(all_free_coor))]
    direction = random.choice([0, 3, 6, 9])  # randomly picks the direction, in which the ship will be built; 0 means
    # upwards, 3 means rightwards, and so on.
    # four next functions (that start with 'if') generate the remaining coordinates of the ship
    if direction == 0:
        for i in range(1, size):
            if coor[0][1] - i >= 1:
                coor.append((chr(ord(coor[0][0])), coor[0][1] - i))
            else:
                coor.sort(reverse=True)
                coor.append((chr(ord(coor[0][0])), coor[0][-1] + 1))
    elif direction == 3:
        for i in range(1, size):
            if chr(ord(coor[0][0]) + i) in 'ABCDEFGHIJ':
                coor.append((chr(ord(coor[0][0]) + i), coor[0][1]))
            else:
                coor.sort()
                coor.append((chr(ord(coor[0][0]) - 1), coor[0][1]))
    elif direction == 6:
        for i in range(1, size):
            if coor[0][1] + i <= 10:
                coor.append((chr(ord(coor[0][0])), coor[0][1] + i))
            else:
                coor.sort()
                coor.append((chr(ord(coor[0][0])), coor[0][-1] - 1))
    elif direction == 9:
        for i in range(1, size):
            if chr(ord(coor[0][0]) - i) in 'ABCDEFGHIJ':
                coor.append((chr(ord(coor[0][0]) - i), coor[0][1]))
            else:
                coor.sort(reverse=True)
                coor.append((chr(ord(coor[0][0]) + 1), coor[0][1]))
    [all_free_coor_minus_used.remove(k) for i in coor for k in all_free_coor_minus_used if i == k]  # removes used
    # coordinates of the ship
    coor.sort()
    # the next two functions (that start with 'if') remove the rest of coordinates - those at the sides of the ship
    if direction == 0 or direction == 6:
        for i in range(-1, size + 1):
            try:
                all_free_coor_minus_used.remove((chr(ord(coor[0][0]) + 1), coor[0][1] + i))
            except ValueError:
                pass
        for i in range(-1, size + 1):
            try:
                all_free_coor_minus_used.remove((chr(ord(coor[0][0]) - 1), coor[0][1] + i))
            except ValueError:
                pass
        try:
            all_free_coor_minus_used.remove((coor[0][0], coor[0][1] - 1))
        except ValueError:
            pass
        try:
            all_free_coor_minus_used.remove((coor[0][0], coor[-1][1] + 1))
        except ValueError:
            pass
    if direction == 3 or direction == 9:
        for i in range(-1, size + 1):
            try:
                all_free_coor_minus_used.remove((chr(ord(coor[0][0]) + i), coor[0][1] + 1))
            except ValueError:
                pass
        for i in range(-1, size + 1):
            try:
                all_free_coor_minus_used.remove((chr(ord(coor[0][0]) + i), coor[0][1] - 1))
            except ValueError:
                pass
        try:
            all_free_coor_minus_used.remove((chr(ord(coor[-1][0]) + 1), coor[0][1]))
        except ValueError:
            pass
        try:
            all_free_coor_minus_used.remove((chr(ord(coor[0][0]) - 1), coor[0][1]))
        except ValueError:
            pass
    return all_free_coor_minus_used, coor


def generate_all_ships():
    """
    Generates coordinates of all ships and returns a list of them.
    """
    ship_of_4 = generate_ships(all_free_coor, 4, q=4)
    ship_of_3 = generate_ships(ship_of_4[0], 3, q=4)
    ship_of_3_2 = generate_ships(ship_of_3[0], 3, q=4)
    ship_of_2 = generate_ships(ship_of_3_2[0], 2, q=4)
    ship_of_2_2 = generate_ships(ship_of_2[0], 2, q=4)
    ship_of_2_3 = generate_ships(ship_of_2_2[0], 2, q=4)
    ship_of_1 = generate_ships(ship_of_2_3[0], 1, q=4)
    ship_of_1_2 = generate_ships(ship_of_1[0], 1, q=4)
    ship_of_1_3 = generate_ships(ship_of_1_2[0], 1, q=4)
    ship_of_1_4 = generate_ships(ship_of_1_3[0], 1, q=4)
    lst_of_coors = [ship_of_4[1] + ship_of_3[1] + ship_of_3_2[1] + ship_of_2[1] + ship_of_2_2[1] + ship_of_2_3[1] +
                    ship_of_1[1] + ship_of_1_2[1] + ship_of_1_3[1] + ship_of_1_4[1]]  # makes list of all coordinates,
    # taken up by ships
    return lst_of_coors[0]


def insert_stars(coordinates):
    """
    Transforms coordinates from generate_all_ships() to the 'star' format.
    """
    all_free_coor_new = [(i, k) for k in range(1, 11) for i in "ABCDEFGHIJ"]  # generates a free gamefield
    new = [all_free_coor_new.index(k) for k in coordinates]
    for i in new:
        all_free_coor_new[i] = '*'
    for i in range(len(all_free_coor_new)):
        if all_free_coor_new[i] != '*':
            all_free_coor_new[i] = ' '
    correct_form_coors = [all_free_coor_new[x:x + 10] for x in range(0, len(all_free_coor_new), 10)]
    return correct_form_coors


def iterate_until_valid():
    """
    Generates random fields until a valid one is created.
    """
    for i in range(3333):
        sigma = insert_stars(generate_all_ships())
        if is_valid(sigma):
            break
    return sigma
# ready_to_print = iterate_until_valid()
# field_to_str(ready_to_print)
