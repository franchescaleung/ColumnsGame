#project5.py
import pygame
import columns

class display_fallers:
    def __init__(self):
        self.blocks = []


def run_pygame() -> None:
    pygame.init()
    
    surface = pygame.display.set_mode((700, 600))
    
    pygame.quit()

if __name__ == '__main__':
    run_pygame()
