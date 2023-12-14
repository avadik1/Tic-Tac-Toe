print('Добро пожаловать в крестикики нолики!')
print('-' * 37)

gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_GameBoard():
    for x in range(3):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(3):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+")


print_GameBoard()
chose1 = int(input('Выберете цифру от 1 до 9:'))


def chose_player_1(chose_1=chose1):
    if chose_1 < 1 or chose_1 > 9:
        print('Неправильный ввод. Попробуйте снова!')
        exit()
    elif chose_1 == 1:
        gameBoard[0][0] = 'X'
    elif chose_1 == 2:
        gameBoard[0][1] = 'X'
    elif chose_1 == 3:
        gameBoard[0][2] = 'X'
    elif chose_1 == 4:
        gameBoard[1][0] = 'X'
    elif chose_1 == 5:
        gameBoard[1][1] = 'X'
    elif chose_1 == 6:
        gameBoard[1][2] = 'X'
    elif chose_1 == 7:
        gameBoard[2][0] = 'X'
    elif chose_1 == 8:
        gameBoard[2][1] = 'X'
    else:
        gameBoard[2][2] = 'X'
    return


chose_player_1()
print_GameBoard()
chose2 = int(input('Выберете цифру от 1 до 9, исключая прошлый выбор игрока:'))


def chose_player_2(chose_2=chose2):
    if chose_2 < 1 or chose_2 > 9:
        print('Неправильной ввод. Попробуйте снова!')
        exit()
    elif chose_2 == 1:
        gameBoard[0][0] = '0'
    elif chose_2 == 2:
        gameBoard[0][1] = '0'
    elif chose_2 == 3:
        gameBoard[0][2] = '0'
    elif chose_2 == 4:
        gameBoard[1][0] = '0'
    elif chose_2 == 5:
        gameBoard[1][1] = '0'
    elif chose_2 == 6:
        gameBoard[1][2] = '0'
    elif chose_2 == 7:
        gameBoard[2][0] = '0'
    elif chose_2 == 8:
        gameBoard[2][1] = '0'
    else:
        gameBoard[2][2] = '0'
    return


chose_player_2()
print_GameBoard()


def check_winner():
    possible_combinations = [
        [gameBoard[0][0], gameBoard[0][1], gameBoard[0][2]],
        [gameBoard[1][0], gameBoard[1][1], gameBoard[1][2]],
        [gameBoard[2][0], gameBoard[2][1], gameBoard[2][2]],
        [gameBoard[0][0], gameBoard[1][0], gameBoard[2][0]],
        [gameBoard[0][1], gameBoard[1][1], gameBoard[2][1]],
        [gameBoard[0][2], gameBoard[1][2], gameBoard[2][2]],
        [gameBoard[0][0], gameBoard[1][1], gameBoard[2][2]],
        [gameBoard[0][2], gameBoard[1][1], gameBoard[2][0]]
    ]

    for combination in possible_combinations:
        if combination == ['X', 'X', 'X']:
            print('Игрок "X" победил!')
            exit()
        elif combination == ['0', '0', '0']:
            print('Игрок "0" победил!')
            exit()


def check_draw():
    for lst in gameBoard:
        for i in gameBoard:
            if i != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                return 'Ничья!'


def game():
    chose_player_1(int(input('Выберете цифру от 1 до 9:')))
    print_GameBoard()

    chose_player_2(int(input('Выберете цифру от 1 до 9:')))
    print_GameBoard()

    chose_player_1(int(input('Выберете цифру от 1 до 9:')))
    print_GameBoard()
    check_winner()

    chose_player_2(int(input('Выберете цифру от 1 до 9:')))
    print_GameBoard()
    check_winner()

    chose_player_1(int(input('Выберете цифру от 1 до 9:')))
    print_GameBoard()
    check_winner()

    chose_player_2(int(input('Выберете цифру от 1 до 9:')))
    print_GameBoard()
    check_winner()

    chose_player_1(int(input('Выберете цифру от 1 до 9:')))
    print_GameBoard()
    check_winner()
    print(check_draw())


game()


