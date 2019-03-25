#project5.py
import pygame
import columns
import random
ORANGE = (255, 153, 0)
BLUE = (0, 0, 225)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (153, 0, 255)

class DisplayGame:
    
    def __init__(self):
        self.surface = ''
        self.game = columns.GameState(13, 6).new_game()
        self.width = 0
        self.height = 0
        self.game = 0
        self.faller = 0
        self.matches = False
        self._colors = []
        self._running = True
        
    def run_pygame(self) -> None:
        pygame.init()
        
        #surface = pygame.display.set_mode((700, 600))
        self._resize_surface((400, 600))
        
        self.draw_game_board()
        self.game = columns.GameState(13, 6)
        clock = pygame.time.Clock()
        
        
        
        while self._running:
            clock.tick(30)
            self.handle_events()
            self.put_on_board()
            
            
                    
        pygame.quit()
    def handle_events(self):
        self.assign_colors_to_faller()
        print(self.game)
        print(self.game.board, "board")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.faller.change_direction('right')
                    elif event.key == pygame.K_LEFT:
                        self.faller.change_direction('left')
                    elif event.key == pygame.K_r:
                        self.faller.rotates()
                self.faller.move()

            


        
    def _resize_surface(self, size: (int, int)):
        self.width = size[0]
        self.height = size[1]
        self.surface = pygame.display.set_mode(size, pygame.RESIZABLE)
        COLUMN1 = (0/6 * self.width)
        COLUMN2 = (1/6 * self.width)
        COLUMN3 = (2/6 * self.width)
        COLUMN4 = (3/6 * self.width)
        COLUMN5 = (4/6 * self.width)
        COLUMN6 = (5/6 * self.width)
        ROW1 = 0/13 * self.height
        ROW2 = 1/13 * self.height
        ROW3 = 2/13 * self.height
        ROW4 = 3/13 * self.height
        ROW5 = 4/13 * self.height
        ROW6 = 5/13 * self.height
        ROW7 = 6/13 * self.height
        ROW8 = 7/13 * self.height
        ROW9 = 8/13 * self.height
        ROW10 = 9/13 * self.height
        ROW11 = 10/13 * self.height
        ROW12 = 11/13 * self.height
        ROW13 = 12/13 * self.height
     

    
    
    def draw_game_board(self):
        start_x = 0
        start_y = 0
        width = self.width
        height = self.height
        #draw columns
        #pygame.draw.rect(self.surface, blue, (start_x, start_y, width, height), 1)
        pygame.draw.line(self.surface, BLUE, ((1/6 * width), start_y), ((1/6 * width), height), 1)
        pygame.draw.line(self.surface, BLUE, ((2/6 * width), start_y), ((2/6 * width), height), 1)
        pygame.draw.line(self.surface, BLUE, ((3/6 * width), start_y), ((3/6 * width), height), 1)
        pygame.draw.line(self.surface, BLUE, ((4/6 * width), start_y), ((4/6 * width), height), 1)
        pygame.draw.line(self.surface, BLUE, ((5/6 * width), start_y), ((5/6 * width), height), 1)

        #draw rows
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (1/13 * height))), ((start_x + width), start_y + (1/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (2/13 * height))), ((start_x + width), start_y + (2/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (3/13 * height))), ((start_x + width), start_y + (3/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (4/13 * height))), ((start_x + width), start_y + (4/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (5/13 * height))), ((start_x + width), start_y + (5/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (6/13 * height))), ((start_x + width), start_y + (6/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (7/13 * height))), ((start_x + width), start_y + (7/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (8/13 * height))), ((start_x + width), start_y + (8/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (9/13 * height))), ((start_x + width), start_y + (9/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (10/13 * height))), ((start_x + width), start_y + (10/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (11/13 * height))), ((start_x + width), start_y + (11/13 * height)), 1)
        pygame.draw.line(self.surface, BLUE, (start_x, (start_y + (12/13 * height))), ((start_x + width), start_y + (12/13 * height)), 1)
        

    def create_faller(self):
        
        letters = ["R", 'O', 'G', 'B', 'Y', 'P', 'W']
        gem1 = random.choice(letters)
        gem2 = random.choice(letters)
        gem3 = random.choice(letters)
        three_types = [gem1, gem2, gem3]
        column_num = random.randint(1, 6)
        self.faller = columns.fallers(three_types, column_num, self.game)

    def assign_colors_to_faller(self):
        #if frozen, draw with border
        column_1 = (0/6 * self.width)
        self.create_faller()
        self._colors = []
        for letter in self.faller.types:
            if letter == "R":
                self._colors.append(RED)
            elif letter == "O":
                self._colors.append(ORANGE)
            elif letter == "G":
                self._colors.append(GREEN)
            elif letter == "B":
                self._colors.append(BLUE)
            elif letter == "Y":
                self._colors.append(YELLOW)
            elif letter == "P":
                self._colors.append(PURPLE)
            elif letter == "W":
                self._colors.append(WHITE)
        #pygame.draw.rect(self.surface, self._colors[0], (column_1, 0, (1/6 * self.width), 1/13 * self.height))
        #pygame.draw.rect(self.surface, self._colors[1], (column_1, 1/13 * self.height, (1/6 * self.width), 1/13 * self.height))
        #pygame.draw.rect(self.surface, self._colors[2], (column_1, 2/13 * self.height, (1/6 * self.width), 1/13 * self.height))


    def move_faller(self):
        #put faller
        #if position[1] > 0:
##        while self.faller._state == 'moving':
##                
##            for item in range(len(self.faller.position)):
##                if self.faller.position[item][1] > 0:
##                    col = 'COLUMN' + str(self.faller.position[item][0])
##                    row = 'ROW' + str(self.faller.position[item][1])
##                    print(col)
##                    print(row)
##                    pygame.draw.rect(self.surface, self._colors[item], col, row, (1/6 * self.width), 1/13 * self.height)
##            
##                    
           self.faller.move()


    
    
            

    def put_on_board(self):
        self.draw_game_board()
        width_of_block = 1/6 * self.width
        height_of_block = 1/13 *self.height
        for col in range(len(self.game.board)):
            for row in range(len(self.game.board[col])):
                if self.game.board[col][row] == "   ":
                    pass
                elif self.game.board[col][row].startswith("|"):
                    #put frozen boarder
                    pass
                else:
                    letter = self.game.board[col][row].strip("[] ")
                    if letter == "R":
                        color = RED
                    elif letter == "O":
                        color = (ORANGE)
                    elif letter == "G":
                        color = (GREEN)
                    elif letter == "B":
                        color = (BLUE)
                    elif letter == "Y":
                        color = (YELLOW)
                    elif letter == "P":
                        color = (PURPLE)
                    elif letter == "W":
                        color = (WHITE)
                    pygame.draw.rect(self.surface, color, (((col-1/6) * self.width), (row)/13 * self.height, width_of_block, height_of_block))


        pygame.display.flip()
                    #don't know what should do yet whoops
        
                
                            
        #each list is a column
        #first figure how to print board

        #so printing the board...
        #

    


if __name__ == '__main__':
    x = DisplayGame().run_pygame()
