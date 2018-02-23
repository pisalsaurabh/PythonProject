from __future__ import print_function
import random
import os

def fullboard(board):
    x=0
    for pointer in xrange(1,10):
        if board[pointer]!=' ':
            x+=1

    if(x==9):
        return True
    else:
        return False


# from IPython.display import clear_output
def sp_choose_symbol():

    '''
    DocTxt: This function is used to select symbol for player 1 and player 2 and asign it to player1 symbol
    and player 2 symbol simultaneously
    '''
    symbol = ''
    while (symbol !='X' or symbol!='O'):

         symbol=raw_input("Please select your symbol for PLAYER 1 between X and O ").upper()
         if symbol == 'X':
              return 'X', 'O'
         elif symbol =='O':
             return 'O', 'X'
         else:
             print(" Please Select 'X' or 'O', other characters cannot be used")

def chooseplayer():
    '''
    This will randomly select a player for its turn.
    '''
    if random.randint(1,2)==1:
        return 'player1'
    else:
        return 'player2'






def printboard(board):
    # code for printing the board
    os.system('cls')
    print("\n")
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

    pass

def boardwrite(player_symbol,position,board):
    #code
    board[position]=player_symbol
    pass



def checkforwin(board,player1_symbol):
    #logic for wining
    return ((board[7] == player1_symbol and board[8] == player1_symbol and board[9] == player1_symbol) or  # across the top
            (board[4] == player1_symbol and board[5] == player1_symbol and board[6] == player1_symbol) or  # across the middle
            (board[1] == player1_symbol and board[2] == player1_symbol and board[3] == player1_symbol) or  # across the bottom
            (board[7] == player1_symbol and board[4] == player1_symbol and board[1] == player1_symbol) or  # down the middle
            (board[8] == player1_symbol and board[5] == player1_symbol and board[2] == player1_symbol) or  # down the middle
            (board[9] == player1_symbol and board[6] == player1_symbol and board[3] == player1_symbol) or  # down the right side
            (board[7] == player1_symbol and board[5] == player1_symbol and board[3] == player1_symbol) or  # diagonal
            (board[9] == player1_symbol and board[5] == player1_symbol and board[1] == player1_symbol))  # diagonal

def replay():
    x= raw_input("Do you want to play again Y or N?").upper()

    if x == 'Y':
        return False
    elif x == 'N':
        return True
    else:
        print("Inputs invalid")
        replay()



'''
Start of the program
'''

print("Welcome to the tic tac toe game in python "+str(2.7))

player1_symbol,player2_symbol=sp_choose_symbol()

print("Player 1 symbol "+player1_symbol+"\nPlayer 2 symbol "+player2_symbol+"\n")

while True:
    Game_on = True
    board = [' '] * 10
    empty = False
    turn = chooseplayer()
    print(turn)

    while Game_on:
        '''Choose the player randomly'''

        global turn
        if turn == 'player1':

            printboard(board)
            print("Player 1 turn\n")
            position = input("ENTER POSITION ACCORDING TO YOUR NUMPAD 1 TO 9 ")
            boardwrite(player1_symbol, position, board)

            printboard(board)



            if checkforwin(board, player1_symbol):
                printboard(board)
                print("Congratulations Player 1 you have won ")
                Game_on = False  # as the game has been won
            elif fullboard(board):
                print("The game is draw")
                Game_on=False
                break
            else:
                turn = 'player2'



        if turn == 'player2':
            print("Player 2 turn\n")

            printboard(board)
            print("Player 2 turn\n")
            position = input("ENTER POSITION ACCORDING TO YOUR NUMPAD 1 TO 9 ")

            boardwrite(player2_symbol, position, board)


            printboard(board)



            if checkforwin(board, player2_symbol):
                printboard(board)
                print("Congratulations Player 2 you have won ")
                Game_on = False  # as the game has been won
            elif fullboard(board):
                print("The game is draw")
                Game_on=False
                break

            else:
                turn = "player1"

    if replay():
        print("Thank you for playing the X and Zero Game")
        break



