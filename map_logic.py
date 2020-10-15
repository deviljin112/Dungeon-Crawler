import random
from game_classes import Zombie, Vampire, Warewolf


def current_player_position(map, player):
    store_o = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == player:
                store_o.append(i)
                store_o.append(j)
                break
    return store_o


def generate_map(player):
    x = random.randint(3, 10)
    y = random.randint(3, 10)

    enemy_count = int((x + y) / 4)
    game_map = [[""] * x for _ in range(y)]

    start_point = random.choice(["north", "south", "east", "west"])

    player_coords = []

    if start_point == "north" or start_point == "south":
        player_pos = random.randint(0, len(game_map[0]) - 1)
        exact_point = 0 if start_point == "north" else len(game_map) - 1
        game_map[exact_point][player_pos] = player
        player_coords.append(exact_point)
        player_coords.append(player_pos)

    else:
        player_pos = random.randint(0, len(game_map) - 1)
        exact_point = 0 if start_point == "east" else len(game_map[0]) - 1
        game_map[player_pos][exact_point] = player
        player_coords.append(player_pos)
        player_coords.append(exact_point)

    enemies_added = 0
    enemy_list = []
    while enemies_added < enemy_count:
        ene_x = random.randint(0, len(game_map[0]) - 1)
        ene_y = random.randint(0, len(game_map) - 1)

        if game_map[ene_y][ene_x] == "":
            chosen_enemy = random.choice([Zombie, Vampire, Warewolf])
            game_map[ene_y][ene_x] = chosen_enemy
            enemy_list.append(chosen_enemy)
            enemies_added += 1

    return game_map, enemy_list
