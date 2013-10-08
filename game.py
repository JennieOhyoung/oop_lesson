import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

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

class Balloonicorn(GameElement):
    IMAGE = "BC"
    SOLID = True
    INTERACTIVE = True

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("Woo! A Balloonicorn! %r has %d points!"%(player.char_name, len(player.inventory)))

class Character(GameElement):
    IMAGE = "Cat"
    SOLID = True
    INTERACTIVE = False

    def char_name(self, player):
        if PLAYER: 
            print "Chris"
        elif PLAYER2:
            print "Liz"

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
            (15, 0),
            (15, 1),
            (15, 2),
            (15, 3), 
            (15, 4)
        ]  
    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    global PLAYER
    PLAYER = Character()
    NAME = "Chris"
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(0, 0, PLAYER)
    print PLAYER

    global PLAYER2
    PLAYER2 = Character()
    PLAYER2.IMAGE = "Horns"
    NAME = "Liz"
    GAME_BOARD.register(PLAYER2)
    GAME_BOARD.set_el(0, 8, PLAYER2)

    GAME_BOARD.draw_msg("This game is going to teach us about class!")

    # gem = Green_gem()
    # GAME_BOARD.register(gem)
    # GAME_BOARD.set_el(6, 1, gem)

    bc1 = Balloonicorn()
    GAME_BOARD.register(bc1)
    GAME_BOARD.set_el(15, 4, bc1)

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