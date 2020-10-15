from prettytable import PrettyTable
from prettytable import ALL
from map_logic import current_player_position


def show_map(game_map):
    pretty_map = PrettyTable()
    pretty_map.header = False
    pretty_map.hrules = ALL
    pretty_map.field_names = [(f"x_{i+1}") for i in range(len(game_map[0]))]
    for i in game_map:
        pretty_map.add_row(i)

    print(pretty_map)


def show_player_vision(board, player_coords, player, enemies):
    can_see = []
    y = player_coords[0]
    x = player_coords[1]

    for i in range(2):
        for checker in range(2):
            i = i if checker == 0 else i * (-1)
            if y + i >= 0 and y + i < len(board):
                if x + i >= 0 and x + i < len(board[y + i]):
                    can_see.append([y + i, x + i])

                if x - i >= 0 and x - i < len(board[y + i]):
                    can_see.append([y + i, x - i])

            if x + i >= 0 and x + i < len(board[y]) and [y, x + i] not in can_see:
                can_see.append([y, x + i])

            if y + i >= 0 and y + i < len(board) and [y + i, x] not in can_see:
                can_see.append([y + i, x])

    fill_table = [["-"] * len(board[0]) for _ in range(len(board))]

    for i in range(len(fill_table)):
        for j in range(len(fill_table[i])):
            if [i, j] in can_see:
                fill_table[i][j] = " "

            if i == y and j == x:
                fill_table[i][j] = player

            if board[i][j] in enemies and [i, j] in can_see:
                fill_table[i][j] = board[i][j]

    pretty_vision = PrettyTable()
    pretty_vision.header = False
    pretty_vision.field_names = [(f"x_{i+1}") for i in range(3)]

    temp_vision_holder = []
    count = 0
    for i in fill_table:
        temp_row = [j for j in i if j != "-"]

        if len(temp_row) != 0:
            temp_vision_holder.append(temp_row)
            count += 1

    store_o = current_player_position(temp_vision_holder, player)

    if len(temp_vision_holder[0]) < 3:
        if store_o[0] == 0:
            if store_o[1] == 0:
                temp_vision_holder[0].insert(0, "-")
                temp_vision_holder[1].insert(0, "-")
                temp_vision_holder.insert(0, ["-", "-", "-"])

            elif store_o[1] == 1:
                temp_vision_holder[0].append("-")
                temp_vision_holder[1].append("-")
                temp_vision_holder.insert(0, ["-", "-", "-"])

        elif store_o[0] == 1:
            if store_o[1] == 0:
                temp_vision_holder[0].insert(0, "-")
                temp_vision_holder[1].insert(0, "-")

                if len(temp_vision_holder) < 3:
                    temp_vision_holder.append(["-", "-", "-"])
                else:
                    temp_vision_holder[2].insert(0, "-")

            elif store_o[1] == 1:
                temp_vision_holder[0].append("-")
                temp_vision_holder[1].append("-")

                if len(temp_vision_holder) < 3:
                    temp_vision_holder.append(["-", "-", "-"])
                else:
                    temp_vision_holder[2].append("-")

        elif store_o[0] == 2:
            if store_o[1] == 0:
                temp_vision_holder[0].insert(0, "-")
                temp_vision_holder[1].insert(0, "-")
                temp_vision_holder.append(["-", "-", "-"])

            elif store_o[1] == 1:
                temp_vision_holder[0].append("-")
                temp_vision_holder[1].append("-")
                temp_vision_holder.append(["-", "-", "-"])

    elif len(temp_vision_holder) < 3:
        if store_o[0] == 0:
            temp_vision_holder.insert(0, ["-", "-", "-"])
        else:
            temp_vision_holder.append(["-", "-", "-"])

    for i in temp_vision_holder:
        pretty_vision.add_row(i)

    print(pretty_vision)