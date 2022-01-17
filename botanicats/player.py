import pygame
from level import Player
from  botanicats import level 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos , colour, goleft, goright):
        super().__init__()
        
        self.image = pygame.Surface ((32, 64))
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft = pos )
        print("in player 1 position is " , pos)
        self.direction = pygame.math.Vector2 (0,0)
        self.goleft = goleft
        self.goright = goright
        self.speed = 8
        
        
   
    def get_input(self, pos , t , g):
        keys = pygame.key.get_pressed()

        if keys[self.goright]:
           
           self.direction.x =  1
        elif keys [self.goleft]:
           self.direction.x =  -1
        else: 
           self.direction.x =  0

         

    def update(self):
         self.get_input()

         self.rect.x = self.rect.x + self.direction.x * self.speed
        #check wether the position of the player intersects with any of the tiles in the y direction. checking bottom of player, top of tile
        #need a functio to check wether a square has a tile in it
         #if self.rect.colliderect(player_one, player_two):

           #  print("there is collision")

        


