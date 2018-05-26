from random import randint
#randint will generate a random position on the board.

board = [] #empty list, will fill it up later

for x in range(0, 5):
  board.append(["O"] * 5) #we create a board represented by upper-case O's. Instead of creating just 1 row, we create 5, and put this in the board list above

def print_board(board):
  for row in board:
    print " ".join(row) #makes sure each "O" on the board is seperated by a white space.

print_board(board) #here we print the board

def random_row(board):
  return randint(0, len(board) - 1)
#here we are creating a random position in the rows, starting from 0 to the end of the board which is 5. Since this ends up with 6 positions, we take 1 away.

def random_col(board):
  return randint(0, len(board[0]) - 1)
#same as above but for columns, the square brackes is needed here because columns are represented by an index

ship_row = random_row(board)
ship_col = random_col(board)
#here we give the ship a position on the board

print ship_row
print ship_col
#the above is for debugging, it prints where the ship is
for turn in range(4): #this gives us 4 turns
  print "Turn", turn + 1 #tells the user what turn they're on
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  #asks the user to input where they think the ship is

  if guess_row == ship_row and guess_col == ship_col: #if input is same as ship pos, correct
    print "Congratulations! You sank my battleship!" 
    break #ends for loop so game over
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
      #if it's not on the board, we tell the user to play the damn game right
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
      #this is for forgetful folk who input the same stuff
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X" #turns empty spot into an "X" rather than an "O"
    print_board(board) #reprints with "X"
    if turn == 3:
      print "Game Over" #closes game after max turns, which is 4. It says 3 here because we start at 0.
