import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys
import random

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 16
GAME_HEIGHT = 9

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True
    INTERACTIVE = False

# class Green_gem(GameElement):
#     IMAGE = "GreenGem"
#     SOLID = False
#     INTERACTIVE = False

#     def interact(self, player):
#         player.inventory.append(self)
#         GAME_BOARD.draw_msg("Woo! A gem! You have %d items!"%(len(player.inventory)))

class Slow_lan(GameElement):
    IMAGE = "BC"
    SOLID = True
    INTERACTIVE = True

    def move_lan(self):
        #print "C_lan move"
        if self.y < GAME_HEIGHT - 1:
            GAME_BOARD.del_el(self.x, self.y)
            GAME_BOARD.set_el(self.x, self.y + 1, self)
        else:
            GAME_BOARD.del_el(self.x, self.y)
            GAME_BOARD.set_el(self.x, 0, self)

    # def interactive(self, player):
    #     player.inventory.append(self)

class Fast_lan(GameElement):
    IMAGE = "Cucumber"
    SOLID = True
    INTERACTIVE = True

    def move_lan(self):
        if self.y < GAME_HEIGHT - 2:
            GAME_BOARD.del_el(self.x, self.y)
            GAME_BOARD.set_el(self.x, self.y + 2, self)
        else:
            GAME_BOARD.del_el(self.x, self.y)
            GAME_BOARD.set_el(self.x, 0, self)

# class Superfast_lan(GameElement):
#     IMAGE = "Cucumber"
#     SOLID = True
#     INTERACTIVE = True

#     def move_lan(self):
#         if self.y < GAME_HEIGHT - 4:
#             GAME_BOARD.del_el(self.x, self.y)
#             GAME_BOARD.set_el(self.x, self.y + 3, self)
#         else:
#             GAME_BOARD.del_el(self.x, self.y)
#             GAME_BOARD.set_el(self.x, 0, self)

class Balloonicorn(GameElement):
    IMAGE = "BC"
    SOLID = True
    INTERACTIVE = True

    def interact(self, player):
        # player.inventory.append(self)
        GAME_BOARD.draw_msg("Woo! A Balloonicorn! %r wins!"%(player.NAME))
        # GAME_BOARD.draw_msg("Woo! A Balloonicorn! %r has %d points!"%(player.NAME, len(player.inventory)))


        # bc1 = Balloonicorn()
        # GAME_BOARD.register(bc1)
        # GAME_BOARD.set_el(15, 4, bc1)

        # next_location = PLAYER.next_pos(direction)
        # next_x = next_location[0]
        # next_y = next_location[1]

        # existing_el = GAME_BOARD.get_el(next_x, next_y)

class Character(GameElement):
    IMAGE = "Chris"
    SOLID = True
    INTERACTIVE = False
    NAME = "Chris"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

    def next_pos(self, direction):
        if direction == "up":
            if self.y == 0:
                return (self.x, self.y + (GAME_HEIGHT-1))
            else:
                return (self.x, self.y - 1)
            
        elif direction == "down":
            if self.y == 7:
                return (self.x, self.y - (GAME_HEIGHT-1))
            else: 
                return (self.x, self.y + 1)

        elif direction == "left":
            if self.x == 0:
                return (self.x, self.y)
            else:
                return (self.x - 1, self.y)
        
        elif direction == "right":
            if self.x == 7:
                return (self.x - (GAME_WIDTH-1), self.y)
            else:
                return (self.x + 1, self.y)

        return None


####   End class definitions    ####

def initialize():
    """Put game initialization code here"""

    rock_positions = [
            (5, 0),
            (5, 1),
            (5, 2),
            (5, 3), 
            (5, 5),
            (5, 6),
            (5, 7),
            (5, 8),
            (10, 1),
            (10, 2),
            (10, 3), 
            (10, 4),
            (10, 5),
            (10, 7),
            (10, 6)
        ]  
    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(0, 0, PLAYER)
    print PLAYER

    global PLAYER2
    PLAYER2 = Character()
    PLAYER2.NAME = "Liz"
    PLAYER2.IMAGE = "Liz"
    GAME_BOARD.register(PLAYER2)
    GAME_BOARD.set_el(0, 8, PLAYER2)

    GAME_BOARD.draw_msg("Race to the Balloonicorn!")

    # gem = Green_gem()
    # GAME_BOARD.register(gem)
    # GAME_BOARD.set_el(6, 1, gem)

    bc1 = Balloonicorn()
    GAME_BOARD.register(bc1)
    GAME_BOARD.set_el(15, 4, bc1)

    # initialize bad guys!
    c1= Slow_lan()
    c1.IMAGE = "C"
    GAME_BOARD.register(c1)
    GAME_BOARD.set_el(1, 1, c1)
    GAME_BOARD.BAD_GUYS.append(c1)

    cucumber1 = Fast_lan()
    cucumber1.IMAGE = "Cucumber"
    GAME_BOARD.register(cucumber1)
    GAME_BOARD.set_el(2, 2, cucumber1)
    GAME_BOARD.BAD_GUYS.append(cucumber1)

    dart1 = Slow_lan()
    dart1.IMAGE = "Dart"
    GAME_BOARD.register(dart1)
    GAME_BOARD.set_el(3, 6, dart1)
    GAME_BOARD.BAD_GUYS.append(dart1)

    haskell1 = Fast_lan()
    haskell1.IMAGE = "Haskell"
    GAME_BOARD.register(haskell1)
    GAME_BOARD.set_el(4, 5, haskell1)
    GAME_BOARD.BAD_GUYS.append(haskell1)

    jennie = Fast_lan()
    jennie.IMAGE = "Jennie"
    GAME_BOARD.register(jennie)
    GAME_BOARD.set_el(13, 4, jennie)
    GAME_BOARD.BAD_GUYS.append(jennie)

    jordyn = Slow_lan()
    jordyn.IMAGE = "Jordyn"
    GAME_BOARD.register(jordyn)
    GAME_BOARD.set_el(12, 6, jordyn)
    GAME_BOARD.BAD_GUYS.append(jordyn) 

    java1 = Slow_lan()
    java1.IMAGE = "Java"
    GAME_BOARD.register(java1)
    GAME_BOARD.set_el(6, 0, java1)
    GAME_BOARD.BAD_GUYS.append(java1)

    python1 = Fast_lan()
    python1.IMAGE = "Python"
    GAME_BOARD.register(python1)
    GAME_BOARD.set_el(7, 7, python1)
    GAME_BOARD.BAD_GUYS.append(python1)

    ruby1 = Slow_lan()
    ruby1.IMAGE = "Ruby"
    GAME_BOARD.register(ruby1)
    GAME_BOARD.set_el(8, 2, ruby1)
    GAME_BOARD.BAD_GUYS.append(ruby1)

    scala1 = Fast_lan()
    scala1.IMAGE = "Scala"
    GAME_BOARD.register(scala1)
    GAME_BOARD.set_el(9, 5, scala1)
    GAME_BOARD.BAD_GUYS.append(scala1)

def badguy_handler():
    for i in GAME_BOARD.BAD_GUYS:
        i.move_lan()



def keyboard_handler():
    direction = None #controls PLAYER
    direction2 = None #controls PLAYER2

    ## use this for specific messages?
    # if KEYBOARD[key.SPACE]:
    #     GAME_BOARD.erase_msg()

    # controls PLAYER
    if KEYBOARD[key.UP]:
        direction = "up"

    if KEYBOARD[key.DOWN]:
        direction = "down"  

    if KEYBOARD[key.RIGHT]:
        direction = "right"

    if KEYBOARD[key.LEFT]:
        direction = "left"

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)
        
        # if existing_el and existing_el.INTERACTIVE:

        #         GAME_BOARD.draw_msg("You saved the Balloonicorn!")

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)

    # controls PLAYER2
    if KEYBOARD[key.W]:
        direction2 = "up"

    if KEYBOARD[key.S]:
        direction2 = "down"  

    if KEYBOARD[key.D]:
        direction2 = "right"

    if KEYBOARD[key.A]:
        direction2 = "left"

    if direction2:
        next_location = PLAYER2.next_pos(direction2)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER2)
        
        # if existing_el and existing_el.INTERACTIVE:
        #         GAME_BOARD.draw_msg("You saved the Balloonicorn!")

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER2.x, PLAYER2.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER2)

        # GAME_BOARD.draw_msg("Save the Balloonicorn!")