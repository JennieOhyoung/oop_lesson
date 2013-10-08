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

GAME_WIDTH = 8
GAME_HEIGHT = 8

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True
    INTERACTIVE = False

class Green_gem(GameElement):
    IMAGE = "GreenGem"
    SOLID = False
    INTERACTIVE = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("Woo! A gem! You have %d items!"%(len(player.inventory)))

class Horn_girl(GameElement):
    IMAGE = "Horns"
    SOLID = True
    INTERACTIVE = True


class Character(GameElement):
    IMAGE = "Cat"

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
                return (self.x + (GAME_WIDTH-1), self.y)
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
            (6, 2), 
            (7, 2)
        ]  
    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    #rocks[-1].SOLID = False

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("This game is going to teach us about class!")

    gem = Green_gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(6, 1, gem)

    horn = Horn_girl()
    GAME_BOARD.register(horn)
    GAME_BOARD.set_el(2, 6, horn)

def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"
        # GAME_BOARD.draw_msg("You pressed up!")
        # next_y = PLAYER.y - 1
        # GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        # GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

    if KEYBOARD[key.DOWN]:
        direction = "down"  
        # GAME_BOARD.draw_msg("You pressed down!")
        # next_y = PLAYER.y + 1
        # GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        # GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

    if KEYBOARD[key.RIGHT]:
        direction = "right"
        # GAME_BOARD.draw_msg("You pressed right!")
        # next_x = PLAYER.x + 1
        # GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        # GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)

    if KEYBOARD[key.LEFT]:
        direction = "left"
        # GAME_BOARD.draw_msg("You pressed left!")
        # next_x = PLAYER.x - 1
        # GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        # GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)

    if KEYBOARD[key.SPACE]:
        GAME_BOARD.erase_msg()

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)
        
        if existing_el and existing_el.INTERACTIVE:
                GAME_BOARD.draw_msg("Hi, I'm Horn Girl.")

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)

        # GAME_BOARD.draw_msg("This game is going to teach us about class!")
        # if existing_el.INTERACTIVE:
        #     print "Hello there, my name is Horn Girl."

# def portal_pos(self):
#     PLAYER.del_el(PLAYER.x, PLAYER.y)
#     return PLAYER.set_el(7, 0, PLAYER)


    # green_gem1 = Green_gem()
    # GAME_BOARD.register(green_gem1)
    # GAME_BOARD.set_el(2, 2, green_gem1)

    # cat1 = Cat()
    # GAME_BOARD.register(cat1)
    # GAME_BOARD.set_el(2, 1, cat1)





    # print "The first rock is at", (rock1.x, rock1.y)
    # print "The second rock is at", (rock2.x, rock2.y)
    # print "The first gem is at", (green_gem1.x, green_gem1.y)
    # print "The first cat girl is at", (cat1.x, cat1.y)
    # print "Rock 1 image", rock1.IMAGE
    # print "Rock 2 image", rock2.IMAGE
    # # print "Green Gem 1 image", green_gem1.IMAGE
    # print "Cat Girl 1 image", cat1.IMAGE