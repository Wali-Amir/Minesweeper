from functions import Minesweeper
from time import time

game_continue = True
game = Minesweeper(int(input("What difficulty do you wanna play?\n1. Beginner (9x9)\n2. Intermediate (16x16)\n3. Advanced (30x16)\nEnter the number of your chocie: ")))
won = False
start = time()

while game_continue and not won:
    print(f"\nTime Elapsed: {round(time()-start,1)}")
    game.render()
    move, row, col = input("Enter your move in the form: 'move row column', where move can be R for reveal or F for flag, and row and column are the numbers\n").split(' ')
    row = int(row) - 1
    col = int(col) - 1

    while (row<0 or row>=game.height or col<0 or col>=game.width):
        print("Cell chosen is out of bounds.")
        move, row, col = input("Enter your move in the form: 'move row column', where move can be R for reveal or F for flag, and row and column are the numbers\n").split(' ')

    if move.upper()=='F':
        game.flag(row,col)
    elif move.upper()=='R':
        game_continue = game.reveal(row,col)
    
    won = game.check_win()

game.render()
print("Game over!" if not won else "Congratulations!")
print(f"That game took a total of {round(time()-start,1)} seconds.")

