
import pygame
from pygame.constants import K_LEFT
from settings import tile_size
from tiles import Tile
from player import  Player



class Level:
    #level setup
    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.setup_level (level_data)

        self.world_shift = 0
       # self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        
    
    def setup_level(self, layout):
       
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()

        for row_index, row in enumerate(layout):

            for col_index, cell in enumerate(row):
                
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y) , tile_size)
                    self.tiles.add(tile)
                
                if cell == 'P' :
                    player_one= Player ((x,y), 'blue', pygame.K_LEFT, pygame.K_RIGHT)
                    player_one.get_input ( 2, 3, 4)

                    self.player.add(player_one)
                
                if cell == 'D' :

                    player_two = Player((x,y), 'white',  pygame.K_a, pygame.K_d)
                    self.player.add(player_two)
                    

                
                 
                
   
    def run(self):

        #tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
         
        #players
        self.player.update()
        self.player.draw(self.display_surface)

        