field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinations_wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
game_over = False
player = 1


def field_print():
    print(f'{field[0]}  {field[1]}  {field[2]}')
    print(f'{field[3]}  {field[4]}  {field[5]}')
    print(f'{field[6]}  {field[7]}  {field[8]}')


def steps(step, X_O):
    field[field.index(step)] = X_O


def win_detection():
    win = None

    for i in combinations_wins:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "Победили крестики"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "Победили нолики"

    return win


while not game_over:

    field_print()

    if player % 2:
        X_O = "X"
        step = int(input("Ходят крестики: "))
    else:
        X_O = "O"
        step = int(input("Ходят нолики: "))
    if field[step - 1] == "X" or field[step - 1] == "0":
        print("Клетка занята, выберите другую")
        continue
    steps(step, X_O)
    win = win_detection()
    if win:
        game_over = True
    else:
        game_over = False

    player += 1

field_print()

print(win)
