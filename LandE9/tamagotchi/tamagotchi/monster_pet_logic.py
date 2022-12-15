from enum import Enum


HUNGER_INCREASE = 5
BOREDOM_INCREASE = 5
DIRT_INCREASE = 5

HUNGER_MAX = 100
BOREDOM_MAX = 100
DIRT_MAX = 100


class TamagotchiState(Enum):
    ALRIGHT = 0
    PLAYING = 1
    DIZZY = 2
    DEAD = 3


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0
        self.dirtiness = 0

        self.state = TamagotchiState.ALRIGHT

        assert self.hunger == self.boredom == self.dirtiness == 0
        assert self.state == TamagotchiState.ALRIGHT

    def feed(self, nutrition):
        self._update_state(nutrition)

    def play(self, play_action):
        self.state = TamagotchiState.PLAYING
        self._update_state(play_action)

    def clean(self, clean_action):
        self._update_state(clean_action)

    def clock_tick(self):
        self.hunger += HUNGER_INCREASE
        self.boredom += BOREDOM_INCREASE
        self.dirtiness += DIRT_INCREASE

        if self.hunger > 80 or self.boredom > 80 or self.boredom > 80:
            self.state = TamagotchiState.DIZZY
        else:
            self.state = TamagotchiState.ALRIGHT

        if (
            self.hunger >= HUNGER_MAX
            or self.boredom >= BOREDOM_MAX
            or self.dirtiness >= DIRT_MAX
        ):
            self.state = TamagotchiState.DEAD

        if self.state == TamagotchiState.DIZZY:
            assert self.hunger >= 80 or self.boredom >= 80 or self.dirtiness >= 80
        elif self.state == TamagotchiState.DEAD:
            assert self.hunger >= 100 or self.boredom >= 100 or self.dirtiness >= 100
        elif self.state == TamagotchiState.ALRIGHT:
            assert self.hunger < 80 and self.boredom < 80 and self.dirtiness  < 80
        
        self.print_state()

    def _update_state(self, action):
        self.hunger += action.hunger_change
        self.boredom += action.boredom_change
        self.dirtiness += action.dirtiness_change
        if self.hunger < 0:
            self.hunger = 0
        if self.boredom < 0:
            self.boredom = 0
        if self.dirtiness < 0:
            self.dirtiness = 0

    def print_state(self):
        msg = (
            f"{self.state.name} - H: {self.hunger}, B: {self.boredom}"
            + f", D: {self.dirtiness}"
        )
        # TODO log here
        print(msg)


class Nutrion:
    pass


class Food(Nutrion):
    pass


class Drink(Nutrion):
    pass


class Pizza(Food):
    def __init__(self):
        self.hunger_change = -3
        self.boredom_change = -5
        self.dirtiness_change = 3


class Sandwich(Food):
    def __init__(self):
        self.hunger_change = -6
        self.boredom_change = -2
        self.dirtiness_change = 3


class Pudding(Food):
    def __init__(self):
        self.hunger_change = -2
        self.boredom_change = -4
        self.dirtiness_change = 2


class Icecream(Food):
    def __init__(self):
        self.hunger_change = -2
        self.boredom_change = -5
        self.dirtiness_change = 1


class Soda(Drink):
    def __init__(self):
        self.hunger_change = -1
        self.boredom_change = -3
        self.dirtiness_change = 1


class Rootbeer(Drink):
    def __init__(self):
        self.hunger_change = -1
        self.boredom_change = -3
        self.dirtiness_change = 2


class Action:
    pass


class Play(Action):
    def __init__(self):
        self.hunger_change = 5
        self.boredom_change = -10
        self.dirtiness_change = 3


class Clean(Action):
    def __init__(self):
        self.hunger_change = +5
        self.boredom_change = +5
        self.dirtiness_change = -10
