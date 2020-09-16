

def representation_of_game(matrix, num, value):
    row1, row2, row3 = matrix[0], matrix[1], matrix[2]

    if num   == 1:row1[0] = value
    elif num == 2: row1[1] = value
    elif num == 3:row1[2] = value
    elif num == 4: row2[0] = value
    elif num == 5:row2[1] = value
    elif num == 6:row2[2] = value
    elif num == 7:row3[0] = value
    elif num == 8:row3[1] = value
    elif num == 9:row3[2] = value

    print('{0:^5}|{1:^5}|{2:^5}'.format(row1[0], row1[1], row1[2]))
    print('{0:-^5}|{0:-^5}|{0:-^5}'.format("", "", ""))
    print('{0:^5}|{1:^5}|{2:^5}'.format(row2[0], row2[1], row2[2]))
    print('{0:-^5}|{0:-^5}|{0:-^5}'.format("", "", ""))
    print('{0:^5}|{1:^5}|{2:^5}'.format(row3[0], row3[1], row3[2]))


def logic_of_game(player1, player2):
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']

    matrix = [row1, row2, row3]

    player1_flag = True
    input_check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("SELECT POSITION BETWEEN 1 to 9 :")
    representation_of_game(matrix, 1, ' ')

    while True:
        if len(input_check_list) != 0:

            if row1[0] == row1[1] == row1[2] != ' ':
                print(row1[0], " IS WINNER....")
                break
            elif row2[0] == row2[1] == row2[2] != ' ':
                print(row2[0], " IS WINNER....")
                break
            elif row3[0] == row3[1] == row3[2] != ' ':
                print(row3[0], " IS WINNER....")
                break
            elif row1[0] == row2[0] == row3[0] != ' ':
                print(row1[0], " IS WINNER....")
                break
            elif row1[1] == row2[1] == row3[1] != ' ':
                print(row1[1], " IS WINNER....")
                break
            elif row1[2] == row2[2] == row3[2] != ' ':
                print(row1[2], " IS WINNER....")
                break
            elif row1[0] == row2[1] == row3[2] != ' ':
                print(row1[0], " IS WINNER....")
                break
            elif row1[2] == row2[1] == row3[0] != ' ':
                print(row1[2], " IS WINNER....")
                break

            elif player1_flag:
                input_of_player = int(input("Enter Player1 choice at At 1-9 destination : "))
                if input_of_player not in input_check_list:
                    print("place was already taken..")
                    continue
                representation_of_game(matrix, input_of_player, player1)
                input_check_list.remove(input_of_player)
                player1_flag = not player1_flag
                continue
            else:
                input_of_player = int(input("Enter Player2 choice at At 1-9 destination : "))
                if input_of_player not in input_check_list:
                    print("place was already taken..")
                    continue
                representation_of_game(matrix, input_of_player, player2)
                input_check_list.remove(input_of_player)
                player1_flag = not player1_flag
                continue

        elif len(input_check_list) == 0:
            print("MATCH WAS TIE....")
            break

    check = input("\n WANT TO PLAY ONE MORE TIME..?? : ")
    if check == 'Y' or check == "y":
        start_game()
    else:
        print("Thank YOU.")


def start_game():
    player_choice = ''
    player1 = ''
    player2 = ''
    flag = True
    while True:
        switch_of_game = input("To play game press 'Y' or for exit  'N' :  ")
        if switch_of_game in ['y', 'Y', 'N', 'n']:
            if switch_of_game == 'y' or switch_of_game == 'Y':
                player_choice = input("SELECT BETWEEN 'X' AND 'O' FOR PLAYER 1 : ")
                if player_choice not in ['X', 'O']:
                    print("Entered input was wrong make sure select 'X' OR 'O' ")
                    continue
                if player_choice == "X":
                    player1 = "X"
                    player2 = "O"
                else:
                    player1 = "O"
                    player2 = "X"

                logic_of_game(player1, player2)
                break
            else:
                break

        else:
            print("Entered input was wrong make sure select 'Y' OR 'N' ")
            continue


if __name__ == '__main__':
    start_game()
