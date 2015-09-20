from random import randint
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
	
ships_onboard = []#defining a new list to store the positions of the ships
for x in range(5):	
	ships_onboard.append(["O"] * 5)
#Building ship1 at a random position
ship1_direction = randint(0,1)
#print "The direction of ship1 is ",ship1_direction
if ship1_direction == 0:
	ship1_row = random_row(ships_onboard)
	ship1_col = randint(0, 2)
	ships_onboard[ship1_row][ship1_col]="S"
	ships_onboard[ship1_row][ship1_col+1]="S"
	ships_onboard[ship1_row][ship1_col+2]="S"
else:
	ship1_row = randint(0, 2)
	ship1_col = random_col(ships_onboard)
	ships_onboard[ship1_row][ship1_col]="S"
	ships_onboard[ship1_row+1][ship1_col]="S"
	ships_onboard[ship1_row+2][ship1_col]="S"
#Building ship 2 at a random position and checking for collisions with ship 1
ship2_direction = randint(0,1)
#print "The direction of ship2 is ",ship2_direction
if ship2_direction == 0:
	while True:
		ship2_row = random_row(ships_onboard)
		ship2_col = randint(0, 3)
		if ships_onboard[ship2_row][ship2_col]=="S" or ships_onboard[ship2_row][ship2_col+1]=="S":
			continue
		else:
			ships_onboard[ship2_row][ship2_col]="S"
			ships_onboard[ship2_row][ship2_col+1]="S"
			break
else:
	while True:
		ship2_row = randint(0, 3)
		ship2_col = random_col(ships_onboard)
		if ships_onboard[ship2_row][ship2_col]=="S" or ships_onboard[ship2_row+1][ship2_col]=="S":
			continue
		else:
			ships_onboard[ship2_row][ship2_col]="S"
			ships_onboard[ship2_row+1][ship2_col]="S"
			break
	
    
# Game turns begins here  
turn=0  
while turn<4:
	print "Turn ", turn + 1
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))
	if guess_row==17 and guess_col==17:
		print ("This is the debug mode and the location of the ships is as shown: ")
		print_board(ships_onboard)
		print ("---------------------------------------")
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			print "Oops, that's not even in the ocean."
		elif ships_onboard[guess_row][guess_col] == "S":
			print "Congratulations! You sunk my battleship and you have WON :) "
			break
		elif(board[guess_row][guess_col] == "X"):
			print "You guessed that one already."
		else:
			print "You missed my battleship!"
			board[guess_row][guess_col] = "X"
		if turn == 3:
			print("Game Over")
		turn=turn+1
		print_board(board)
		print ("---------------------------------------")
#python C:\Users\Rohit\Desktop\script.py