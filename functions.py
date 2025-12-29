from random import randint
from termcolor import colored

class Minesweeper:

    def __init__(self, difficulty):
        self.width, self.height = {1 : (9,9), 2: (16,16), 3: (30,16)}[difficulty]
        self.bombs = {1: 10, 2: 40, 3: 99}[difficulty]
        self.blocked = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.insert_bombs()
        self.calculate_nums()

    def insert_bombs(self):
        for _ in range(self.bombs):
            random_x = randint(0,self.height-1)
            random_y = randint(0,self.width-1)
            while self.grid[random_x][random_y] == 'B':
                random_x = randint(0,self.height-1)
                random_y = randint(0,self.width-1)
            self.grid[random_x][random_y] = 'B'
    
    def calculate_nums(self):
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == 'B':
                    continue
                nearby_bombs = 0
                for i in range(-1,2,1):
                    for j in range(-1,2,1):
                        if (x+i<0 or x+i>=self.height or y+j<0 or y+j>=self.width):
                            continue
                        elif self.grid[x+i][y+j]=='B':
                            nearby_bombs+=1
                self.grid[x][y] = nearby_bombs
    
    def render(self):
        print("    ",end="")
        for x in range(self.width):
            print(x+1,' ' if x+1==9 else '', sep="",end=" ")
        print('')
        
        for row in range(self.height):
            print(f"{row+1:>2}|",end=" ")
            for col in range(self.width):
                if self.blocked[row][col] == 'F':
                    print(colored('F','grey','on_yellow'),' ' if col>7 else '',sep = "",end=" ")
                elif self.blocked[row][col] == 1:
                    print('\u25A0',' ' if col>7 else '',sep = "",end=" ")
                else:
                    if self.grid[row][col]== 'B':
                        print(colored(' ','red','on_red'),' ' if col>7 else '',sep = "",end=" ")
                    if self.grid[row][col]==0:
                        print(" ",' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]==1:
                        print(colored(1,'blue'),' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]==2:
                        print(colored(2,'green'),' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]== 3:
                        print(colored(3,'red'),' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]== 4:
                        print(colored(4,'yellow'),' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]== 5:
                        print(colored(5,'red',None,['bold']),' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]== 6:
                        print(colored(6,'cyan'),' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]== 7:
                        print(colored(7,'magenta'),' ' if col>7 else '',sep = "",end=" ")
                    elif self.grid[row][col]== 8:
                        print(colored(8,'grey'),' ' if col>7 else '',sep = "",end=" ")
            print('')
    
    def reveal(self,row,col):
        if self.grid[row][col] == 'B':
            self.blocked = [[0 for _ in range(self.width)] for _ in range(self.height)]
            return False
        if self.blocked[row][col] == 0:
            return
        self.blocked[row][col] = 0
        if self.grid[row][col] == 0:
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if (row+i<0 or row+i>=self.height or col+j<0 or col+j>=self.width) or (i==0 and j==0):
                        continue
                    elif self.grid[row+i][col+j]==0:
                        self.reveal(row+i,col+j)
                    elif self.grid[row+i][col+j]!='B':
                        self.blocked[row+i][col+j] = 0
        return True
    
    def flag(self,row,col):
        if self.blocked[row][col] == 'F':
            self.blocked[row][col] = 1
        elif self.blocked[row][col]!=0:
            self.blocked[row][col]='F'

    def check_win(self):
        won = True
        for row in range(self.height):
            for col in range(self.width):
                if not ((self.blocked[row][col]==0 and self.grid[row][col]!='B') or (self.blocked[row][col]!=0 and self.grid[row][col]=='B')):
                    won = False
        return won