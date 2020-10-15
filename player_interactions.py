from map_logic import current_player_position


def move_player(where, given_map, player, enemies):
    y, x = current_player_position(given_map, player)
    print(f"Y: {y}, X: {x}")
    if where.lower() == "s":
        if y + 1 >= 0 and y + 1 < len(given_map) and given_map[y + 1][x] not in enemies:
            given_map[y][x] = ""
            given_map[y + 1][x] = player
    elif where.lower() == "n":
        if y - 1 >= 0 and y - 1 < len(given_map) and given_map[y - 1][x] not in enemies:
            given_map[y][x] = ""
            given_map[y - 1][x] = player
    elif where.lower() == "w":
        if (
            x + 1 >= 0
            and x + 1 < len(given_map[0])
            and given_map[y][x + 1] not in enemies
        ):
            given_map[y][x] = ""
            given_map[y][x + 1] = player
    elif where.lower() == "e":
        if (
            x - 1 >= 0
            and x - 1 < len(given_map[0])
            and given_map[y][x - 1] not in enemies
        ):
            given_map[y][x] = ""
            given_map[y][x - 1] = player
    return given_map