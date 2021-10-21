# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

CELLS_WITH_COINS = [(1, 2), (2, 2), (2, 3), (3, 2)]


def main():
    # Main starts here
    play_again = True
    while play_again:
        play()
        again = input("Play again (y/n): ")
        play_again = again.lower() == "y"


def play():
    """Plays the game"""
    victory = False
    row = 1
    col = 1
    total_coins = 0

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, total_coins = play_one_move(
            col, row, valid_directions, total_coins
        )
    print("Victory! Total coins {}.".format(total_coins))


def find_directions(col, row):
    """Returns valid directions as a string given the supplied location"""
    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST
    return valid_directions


def print_directions(directions_str):
    print("You can travel: ", end="")
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end="")
        if ch == NORTH:
            print("(N)orth", end="")
        elif ch == EAST:
            print("(E)ast", end="")
        elif ch == SOUTH:
            print("(S)outh", end="")
        elif ch == WEST:
            print("(W)est", end="")
        first = False
    print(".")


def play_one_move(col, row, valid_directions, total_coins):
    """Plays one move of the game
    Return if victory has been obtained and updated col,row and coins"""
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()

    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        coins = get_coins(col, row)
        total_coins += coins
        if coins > 0:
            print_coins(coins, total_coins)
    return victory, col, row, total_coins


def move(direction, col, row):
    """Returns updated col, row given the direction"""
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return (col, row)


def is_victory(col, row):
    """Return true is player is in the victory cell"""
    return col == 3 and row == 1  # (3,1)


def get_coins(col, row):
    if (col, row) in CELLS_WITH_COINS:
        answer = input("Pull a lever (y/n): ")
        if answer.lower() == "y":
            return 1
    return 0


def print_coins(coins, total_coins):
    print("You received {:d} coin, your total is now {:d}.".format(coins, total_coins))


if __name__ == "__main__":
    main()
