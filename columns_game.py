#columns_game.py
import columns
import pygame
import random


ORANGE = (255, 153, 0)
BLUE = (0, 0, 225)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (118, 0, 244)

class ColumnsGame:
    def __init__(self):
        self._running = True
        self._state = columns.GameState(13, 6)
        self._state.new_game()
        self.surface = ''
        
        

        
    def run(self):
        pygame.init()
        self._resize_surface((400, 600))
        self.draw_gameboard_background()
        pygame.display.flip()
        timer = pygame.time.Clock()
        pygame.display.set_caption("Columns", "Columns")
        while self._running:
            timer.tick(1)
            
            self._create_faller()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == (pygame.K_RIGHT):
                        self._state.temp_faller.change_direction("right")
                        
                    elif event.key == pygame.K_LEFT:
                        self._state.temp_faller.change_direction("left")
                        
                    elif event.key == pygame.K_SPACE:
                        self._state.temp_faller.rotates()
                        
            self._state.temp_faller.move()
            
            if self._state.temp_faller.see_if_game_is_over():
                columns.game_over()
                break
            else:
                self.print_board()
            
        pygame.quit()


    def _resize_surface(self, size: (int, int)) -> 'surface':
        self.surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def draw_gameboard_background(self):
        surface = pygame.display.get_surface()
        width = surface.get_width()
        height = surface.get_height()
        #draw columns
        for i in range(1, 6):
            pygame.draw.line(surface, WHITE, ((i/6 * width), 0), ((i/6 * width), height), 1)
        #draw rows
        for j in range(1, 13):
            pygame.draw.line(surface, WHITE, (0, (j/13 * height)), (width, (j/13 * height)), 1)
        
        
    def print_board(self):
        frozen_color = (244, 0, 208)
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(0, 0, 0))
        self.draw_gameboard_background()
        width_of_block = (1.01/6 * surface.get_width())
        height_of_block = 1/13 * surface.get_height()
        
        color = ' '
        for col in range(len(self._state.board)):
            for row in range(len(self._state.board[col])):
                #draw rectangle representing color
                if self._state.board[col][row].strip(" []") == "R":
                    color = RED
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                elif self._state.board[col][row].strip(" []") == "O":
                    color = ORANGE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                elif self._state.board[col][row].strip(" []") == "G":
                    color = GREEN
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))                    
                elif self._state.board[col][row].strip(" []") == "B":
                    color = BLUE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                elif self._state.board[col][row].strip(" []") == "Y":
                    color = YELLOW
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                elif self._state.board[col][row].strip(" []") == "W":
                    color = WHITE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                elif self._state.board[col][row].strip(" []") == "P":
                    color = PURPLE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                    
                    
                elif self._state.board[col][row].startswith("|") and self._state.board[col][row][1] == "R":
                    color = RED
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                    pygame.draw.rect(surface, frozen_color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block), 5)
                    
                elif self._state.board[col][row].startswith("|") and self._state.board[col][row][1] == "O":
                    color = ORANGE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))     
                    pygame.draw.rect(surface, frozen_color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block), 5)
                    
                elif self._state.board[col][row].startswith("|") and self._state.board[col][row][1] == "G":
                    color = GREEN
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                    pygame.draw.rect(surface, frozen_color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block), 5)
                                       
                elif self._state.board[col][row].startswith("|") and self._state.board[col][row][1] == "B":
                    color = BLUE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                    pygame.draw.rect(surface, frozen_color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block), 5)

                elif self._state.board[col][row].startswith("|") and self._state.board[col][row][1] == "Y":
                    color = YELLOW
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                    pygame.draw.rect(surface, frozen_color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block), 5)
                    
                elif self._state.board[col][row].startswith("|") and self._state.board[col][row][1] == "W":
                    color = WHITE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                    pygame.draw.rect(surface, frozen_color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block), 5)
                    
                elif self._state.board[col][row].startswith("|") and self._state.board[col][row][1] == "P":
                    color = PURPLE
                    pygame.draw.rect(surface, color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block))
                    pygame.draw.rect(surface, frozen_color, (((col/6 * surface.get_width())), ((row)/13) * surface.get_height(), width_of_block, height_of_block), 5)
                    

        pygame.display.update()
        pygame.display.flip()
              
                
    def _create_faller(self):
        if self._state.temp_faller == "":
            colors = ['R', 'O', 'G', 'B', 'Y', 'P', 'W']
            gem1 = random.choice(colors)
            gem2 = random.choice(colors)
            gem3 = random.choice(colors)
            three_types = [gem1, gem2, gem3]
            column_num = random.randint(1, 6)
            self._state.create_faller(column_num, three_types)
        elif self._state.temp_faller._state == 'permanent':
            colors = ['R', 'O', 'G', 'B', 'Y', 'P', 'W']
            gem1 = random.choice(colors)
            gem2 = random.choice(colors)
            gem3 = random.choice(colors)
            three_types = [gem1, gem2, gem3]
            column_num = random.randint(1, 6)
            self._state.create_faller(column_num, three_types)
        else:
            self._state.temp_faller.change_direction("down")
        

            
            
    def game_over(self):
        
        color = (66, 134, 244)
        font = pygame.font.SysFont('comicsansms', 24)
        text = font.render("GAME OVER", True, color)
        screen = self.surface
        screen.blit(text, ((1/2 * screen.get_width()), ((1/2 * screen.get_height()))))
        

if __name__ == '__main__':
    ColumnsGame().run()
        
        
