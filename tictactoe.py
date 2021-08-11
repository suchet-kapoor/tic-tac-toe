

def display_board(theBoard):
    print("\n")
    print("\t   |     |")
    print("\t {} | {}   | {} ".format(theBoard[1],theBoard[2],theBoard[3]))
    print("\t   |     |")
    print("           --------")
    print("\t   |     |")
    print("\t {} |  {}  | {} ".format(theBoard[4],theBoard[5],theBoard[6]))
    print("\t   |     |")
    print("           --------")
    print("\t   |     |")
    print("\t  {}|  {}  | {} ".format(theBoard[7],theBoard[8],theBoard[9]))
    print("\t   |     |")

def player_input():

   marker=''
   while not(marker=='X'or marker=='O'):
        marker=input('player1: do u want to be X or O ?').upper()
        if marker=='X':
            return ('X','O')
        else:
            return('O','X')
def place_marker(theBoard,marker,position):
    theBoard[position]=marker

def win_check(theBoard,mark):

    return ((theBoard[7] == mark and theBoard[8] == mark and theBoard[9] == mark) or # across the top
    (theBoard[4] == mark and theBoard[5] == mark and theBoard[6] == mark) or # across the middle
    (theBoard[1] == mark and theBoard[2] == mark and theBoard[3] == mark) or # across the bottom
    (theBoard[7] == mark and theBoard[4] == mark and theBoard[1] == mark) or # down the middle
    (theBoard[8] == mark and theBoard[5] == mark and theBoard[2] == mark) or # down the middle
    (theBoard[9] == mark and theBoard[6] == mark and theBoard[3] == mark) or # down the right side
    (theBoard[7] == mark and theBoard[5] == mark and theBoard[3] == mark) or # diagonal
    (theBoard[9] == mark and theBoard[5] == mark and theBoard[1] == mark)) # diagonal
import random
def choose_first():
     flip= random.randint(0,1)
     if flip==0:
         return 'Player1'
     else:
         return 'Player2'
def space_check(theBoard,position):
     if theBoard[position]==' ':
         return True
     else:
         return False
def full_board_check(theBoard):
    for i in range(1,10):
        if space_check(theBoard,i):
            return False
        else:
            pass
    return True
def player_choice(theBoard):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or  not space_check(theBoard,position):
        position=int(input('choose your next position:(1-9)'))

    return position
    display_board(the_Board)
def replay():
    choice=input("yes or no ")
    return choice =='yes'
    #return input('do u want to play again y for yes n for no').lower().startwith('y')

print('welocme to real difficult game to code frist time')
while True:

      the_Board=[' ']*10
      player1_marker,player2_marker=player_input()
      turn=choose_first()

      print(turn + ' will go first.')

      play_game = input('Are you ready to play? Enter y or n')

      if play_game.lower() == 'y':
        game_on = True
      else:
        game_on = False

      while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(the_Board)
            position = player_choice(the_Board)

            place_marker(the_Board, player1_marker, position)


            if win_check(the_Board, player1_marker):
                display_board(the_Board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(the_Board):
                    display_board(the_Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(the_Board)
            position = player_choice(the_Board)
            place_marker(the_Board, player2_marker, position)

            if win_check(the_Board, player2_marker):
                display_board(the_Board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_Board):
                    display_board(the_Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

      if not replay():
        break
