import random

# создаем поле 10х10 
board = []
for i in range(10):
    board.append(["O"] * 10)

# создаем поле бота 
bot_board = []
for i in range(10):
    bot_board.append(["O"] * 10)


# функция для отображения поля
def print_board(board):
    for row in board:
        print(" ".join(row))

    # случайное размещение кораблей на поле бота


def place_ships(bot_board):
    ship_sizes = [5, 4, 3, 3, 2]  # размеры кораблей 
    for size in ship_sizes:
        placed = False
        while not placed:
            # случайно выбираем координаты и ориентацию корабля 
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            orientation = random.choice(["horizontal", "vertical"])
            # проверяем, можно ли разместить корабль в выбранной позиции 
            if orientation == "horizontal" and x + size <= 10:
                valid = True
                for i in range(size):
                    if bot_board[y][x + i] != "O":
                        valid = False
                        break
                if valid:
                    for i in range(size):
                        bot_board[y][x + i] = "S"
                    placed = True
            elif orientation == "vertical" and y + size <= 10:
                valid = True
                for i in range(size):
                    if bot_board[y + i][x] != "O":
                        valid = False
                        break
                if valid:
                    for i in range(size):
                        bot_board[y + i][x] = "S"
                    placed = True

                # размещаем корабли на поле бота


place_ships(bot_board)

# выводим поле бота 
print("Bot's board:")
print_board(bot_board)

# начинаем игру 
while True:
    # вводим координаты выстрела 
    print("Your turn!")
    guess_x = int(input("Guess X (0-9): "))
    guess_y = int(input("Guess Y (0-9): "))
    # проверяем попал ли игрок в корабль 
    if bot_board[guess_y][guess_x] == "S":
        print("Hit!")
        bot_board[guess_y][guess_x] = "X"
    else:
        print("Miss!")
        bot_board[guess_y][guess_x] = "-"
        # проверяем, остались ли на поле бота корабли
    if "S" not in [item for sublist in bot_board for item in sublist]:
        print("You win!")
        break
        # бот делает выстрел
    print("Bot's turn!")
    guess_x = random.randint