





# game_on = True

def play():

    def check_range(input):
        if input >= 1 and input <= 3:
            return True
        else:
            return False

    def is_block_free(input_x, input_y):
        if board[input_y][input_x] == '_':
            return True
        else:
            return False

    # function to take an input and convert it to a board position
    def get_choice():
        print("Which square would you like to choose? Enter your choice as an (x,y) coordinate-")

        def get_inputs_xy():
            x_choice = int(input("Which x value: "))
            while check_range(x_choice) == False:
                print("That value is out of range. Please input an x value again-")
                x_choice = int(input("Which x value: "))

            y_choice = int(input("Which y value: "))
            while check_range(y_choice) == False:
                print("That value is out of range. Please input an y value again-")
                y_choice = int(input("Which x value: "))
            return [y_choice, x_choice]

        values = get_inputs_xy()

        while is_block_free((values[0] - 1), (values[1] - 1)) == False:
            print("\nThat block has already been played on. Please choose another block:\n")
            values = get_inputs_xy()

        x_choice = values[1] - 1
        y_choice = values[0] - 1
        return [y_choice, x_choice]

    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    def print_board():
        for line in board:
            print(line)

    def player_1_move():
        [y_choice, x_choice] = get_choice()
        board[y_choice][x_choice] = 'O'
        print_board()

    def player_2_move():
        [y_choice, x_choice] = get_choice()
        board[y_choice][x_choice] = 'x'
        print_board()

    def p1_is_winner():
        game_on = True
        for line in board:
            if line[0] == 'O' and line[1] == 'O' and line[2] == 'O':
                print("player 1 is the winner!\n")
                game_on = False
        for number in range(0, len(board)):
            if board[0][number] == 'O' and board[1][number] == 'O' and board[2][number] == 'O':
                print("player 1 is the winner!\n")
                game_on = False
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            print("player 1 is the winner!\n")
            game_on = False
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            print("player 1 is the winner!\n")
            game_on = False
        return game_on

    def p2_is_winner():
        game_on = True
        for line in board:
            if line[0] == 'x' and line[1] == 'x' and line[2] == 'x':
                print("Player 2 is the winner!\n")
                game_on = False
        for number in range(0, len(board)):
            if board[0][number] == 'x' and board[1][number] == 'x' and board[2][number] == 'x':
                print("Player 2 is the winner!\n")
                game_on = False
        if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            print("Player 2 is the winner!\n")
            game_on = False
        elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            print("Player 2 is the winner!\n")
            game_on = False
        return game_on

    print_board()
    game_on = True
    while game_on == True:
        player_1_move()
        p1_is_winner()
        player_2_move()
        game_on = p2_is_winner()
    play_again = input("Would you like to play a new game? Type 'y' or 'n' :")
    if play_again == 'y' or play_again == 'yes':
        play()
    else:
        print("Thank you for playing")
        exit()

play()
