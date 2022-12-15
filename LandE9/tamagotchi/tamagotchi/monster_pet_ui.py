import os
import pygame
from enum import Enum
from pygame import Rect
from random import choice
from pygame.sprite import Sprite
from monster_pet_logic import HUNGER_MAX, BOREDOM_MAX, DIRT_MAX


# Configuration and constants for positioning the icons
ARTWORK_PATH = "sprites"
SOUNDS_PATH = "sounds"
SCREENSIZE = WIDTH, HEIGHT = 250, 500
BACKGROUND_COLOR = pygame.Color("black")
NAME_LABEL_POS = (10, 10)
HUNGER_LABEL_POS = (10, 80)
BOREDOM_LABEL_POS = (10, 100)
DIRTINESS_LABEL_POS = (10, 120)
PIZZA_BUTTON_POS = (10, 400)
SANDWICH_BUTTON_POS = (40, 400)
ICECREAM_BUTTON_POS = (10, 430)
PUDDING_BUTTON_POS = (40, 430)
SODA_BUTTON_POS = (10, 460)
ROOTBEER_BUTTON_POS = (40, 460)
PLAY_BUTTON_POS = (100, 400)
CLEAN_BUTTON_POS = (170, 410)


class StatusSprite(Sprite):
    def __init__(self, tamagotchi, kind, pos):
        super().__init__()
        self.images = []
        for idx in range(0, 11):
            fname = f"statusbar_{idx}.bmp"
            img_path = os.path.join(ARTWORK_PATH, fname)
            image = pygame.image.load(img_path)
            x, y = image.get_rect().size
            image = pygame.transform.scale(image, (x // 4, y // 4))
            self.images.append(image)

        self.image = self.images[10]
        self.rect = pygame.Rect(pos[0], pos[1], x // 4, y // 4)
        self.tamagotchi = tamagotchi
        self.kind = kind

    def update(self):
        if self.kind == "hunger":
            data = self.tamagotchi.hunger
        elif self.kind == "boredom":
            data = self.tamagotchi.boredom
        elif self.kind == "dirtiness":
            data = self.tamagotchi.dirtiness
        self.image = self.images[HUNGER_MAX // 10 - (data // 10)]


class MonsterSprite(Sprite):
    action = None
    frames = None

    def __init__(self):
        super().__init__()
        # Since a sprite is an animation based on a collection of frame images,
        # we add all the images to sprite list
        self.images = []
        for idx in range(1, self.frames):
            fname = f"{self.action}_{idx}.bmp"
            img_path = os.path.join(ARTWORK_PATH, fname)
            image = pygame.image.load(img_path)
            x, y = image.get_rect().size
            image = pygame.transform.scale(image, (x * 2, y * 2))
            self.images.append(image)

        # index value to get the image from the list initially it is 1
        self.index = 1
        self.image = self.images[self.index]

        # creating a rect at position x, y with the size size of the sprite
        self.rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 50, 50)

    def update(self):
        # whenever the update method is called, we increment the index to point 
        # to the next image in the sprite animation
        self.index += 1
        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we start from the beginning again
            self.index = 1
        # finally, we update the image that will be displayed
        self.image = self.images[self.index]


class MonsterPlayingSprite(MonsterSprite):
    def __init__(self):
        self.action = "playing"
        self.frames = 6
        super().__init__()


class MonsterRunningSprite(MonsterSprite):
    def __init__(self):
        self.action = "running"
        self.frames = 8
        super().__init__()


class MonsterDizzySprite(MonsterSprite):
    def __init__(self):
        self.action = "dizzy"
        self.frames = 4
        super().__init__()


class SimulationUI:
    """docstring for SimulationUI"""

    def __init__(self, tamagotchi, clickevent):
        self.running_sprite = MonsterRunningSprite()
        self.playing_sprite = MonsterPlayingSprite()
        self.dizzy_sprite = MonsterDizzySprite()
        # creating a group for the monster movement sprite
        self.sprite_group = pygame.sprite.Group(self.running_sprite)

        # getting the pygame clock for handling fps
        self.clock = pygame.time.Clock()

        self.hunger_status_sprite = StatusSprite(tamagotchi, kind="hunger",
                                                 pos=(100, 80))
        self.boredom_status_sprite = StatusSprite(tamagotchi, kind="boredom",
                                                  pos=(100, 100))
        self.dirtyness_status_sprite = StatusSprite(tamagotchi,
                                                    kind="dirtiness",
                                                    pos=(100, 120))
        # creating another group for the statusbar sprites
        self.sprite_group2 = pygame.sprite.Group(self.hunger_status_sprite,
                                                 self.boredom_status_sprite,
                                                 self.dirtyness_status_sprite)
        img_path = os.path.join(ARTWORK_PATH, "pizza.bmp")
        self.pizza_img = pygame.image.load(img_path)
        img_path = os.path.join(ARTWORK_PATH, "icecream.bmp")
        self.icecream_img = pygame.image.load(img_path)
        img_path = os.path.join(ARTWORK_PATH, "pudding.bmp")
        self.pudding_img = pygame.image.load(img_path)
        img_path = os.path.join(ARTWORK_PATH, "sandwich.bmp")
        self.sandwich_img = pygame.image.load(img_path)
        img_path = os.path.join(ARTWORK_PATH, "soda.bmp")
        self.soda_img = pygame.image.load(img_path)
        img_path = os.path.join(ARTWORK_PATH, "rootbeer.bmp")
        self.rootbeer_img = pygame.image.load(img_path)
        img_path = os.path.join(ARTWORK_PATH, "play.bmp")
        self.play_img = pygame.image.load(img_path)
        img_path = os.path.join(ARTWORK_PATH, "clean.bmp")
        self.clean_img = pygame.image.load(img_path)

        pygame.init()
        pygame.display.set_caption("Monster Pet")
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.time.set_timer(clickevent, 5000)

        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        font_small = pygame.font.Font(pygame.font.get_default_font(), 16)
        self.name_txt_img = font.render(tamagotchi.name, True, (250, 250, 250))
        self.hunger_txt_img = font_small.render("Hunger: ", True, 
                                                (250, 250, 250))
        self.boredom_txt_img = font_small.render("Boredom: ", True, 
                                                 (250, 250, 250))
        self.dirtiness_txt_img = font_small.render("Dirtiness: ", True, 
                                                   (250, 250, 250))
        self.random_mode = False

    def update(self):
        self.sprite_group.update()
        self.sprite_group2.update()

        # filling the screen with background color
        self.screen.fill(BACKGROUND_COLOR)

        self.screen.blit(self.name_txt_img, dest=NAME_LABEL_POS)
        self.screen.blit(self.hunger_txt_img, dest=HUNGER_LABEL_POS)
        self.screen.blit(self.boredom_txt_img, dest=BOREDOM_LABEL_POS)
        self.screen.blit(self.dirtiness_txt_img, dest=DIRTINESS_LABEL_POS)

        self.screen.blit(self.pizza_img, dest=PIZZA_BUTTON_POS)
        self.screen.blit(self.sandwich_img, dest=SANDWICH_BUTTON_POS)
        self.screen.blit(self.icecream_img, dest=ICECREAM_BUTTON_POS)
        self.screen.blit(self.pudding_img, dest=PUDDING_BUTTON_POS)
        self.screen.blit(self.soda_img, dest=SODA_BUTTON_POS)
        self.screen.blit(self.rootbeer_img, dest=ROOTBEER_BUTTON_POS)

        self.screen.blit(self.play_img, dest=PLAY_BUTTON_POS)
        self.screen.blit(self.clean_img, dest=CLEAN_BUTTON_POS)

        # drawing the sprite
        self.sprite_group.draw(self.screen)
        self.sprite_group2.draw(self.screen)

        # updating the display
        pygame.display.update()

    def clock_tick(self):
        self.clock.tick(10)
    
    def show_run_animation(self):
        self.sprite_group = pygame.sprite.Group(self.running_sprite)
    
    def show_play_animation(self):
        self.sprite_group = pygame.sprite.Group(self.playing_sprite)
                
    def show_dizzy_animation(self):
        self.sprite_group = pygame.sprite.Group(self.dizzy_sprite)

    def which_action_was_clicked(self, x_coord, y_coord):
        button_rects = [self.pizza_img.get_rect(topleft=PIZZA_BUTTON_POS),
                        self.sandwich_img.get_rect(topleft=SANDWICH_BUTTON_POS),
                        self.icecream_img.get_rect(topleft=ICECREAM_BUTTON_POS),
                        self.pudding_img.get_rect(topleft=PUDDING_BUTTON_POS),
                        self.soda_img.get_rect(topleft=SODA_BUTTON_POS),
                        self.rootbeer_img.get_rect(topleft=ROOTBEER_BUTTON_POS),
                        self.play_img.get_rect(topleft=PLAY_BUTTON_POS),
                        self.clean_img.get_rect(topleft=CLEAN_BUTTON_POS)]

        if self.random_mode:
            action_values = [a.value for a in ActionButton]
            return ActionButton(choice(action_values))
        else:
            for idx, rect in enumerate(button_rects):
                if rect.collidepoint(x_coord, y_coord):
                    return ActionButton(idx)

    def toggle_background(self, color="gray"):
        self.screen.fill(pygame.Color(color))
        pygame.display.update()

    def toggle_random_mode(self):
        self.random_mode = not self.random_mode



class ActionButton(Enum):
    PIZZA = 0
    SANDWICH = 1
    ICECREAM = 2
    PUDDING = 3
    SODA = 4
    ROOTBEER = 5
    PLAY = 6
    CLEAN = 7
