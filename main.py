import random
from map_logic import generate_map, current_player_position
from player_interactions import move_player
from display import show_map, show_player_vision
from game_classes import Player


_DEBUG = False

### NOTES ###

# => Bug fix enemy display
# => Main menu
# => Interactions
# => Battle system
# => Items? or Equipment?
# => Chests
# => Entering / Exiting a Level
# => Level and Experiance system
# => More varied environment
# => Different shaped maps


def main():
    print("Hello Player!\nWhat's your name?")
    name = input("=> ")
    player = Player(name)
    current_map, enemies = generate_map(player)
    print("Lets begin!")

    while player.alive:
        x, y = current_player_position(current_map, player)
        show_player_vision(current_map, [x, y], player, enemies)
        print("Where would you like to go?\nSouth/North/East/West")
        move = input("=> ")
        current_map = move_player(move, current_map, player, enemies)

        if _DEBUG:
            show_map(current_map)

    print("GG, Game Over!")


if __name__ == "__main__":
    main()