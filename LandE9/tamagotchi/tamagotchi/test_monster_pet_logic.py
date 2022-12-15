from monster_pet_logic import (Tamagotchi, TamagotchiState, Pudding, 
                               HUNGER_INCREASE, BOREDOM_INCREASE, DIRT_INCREASE)


def test_name():
    tamagotchi = Tamagotchi(name="Ooomph!")
    assert tamagotchi.name == "Ooomph!"


def test_clock_tick():
    tamagotchi = Tamagotchi(name="Ooomph!")
    for _ in range(3):
        tamagotchi.clock_tick()
    assert tamagotchi.hunger == HUNGER_INCREASE * 3
    assert tamagotchi.boredom == BOREDOM_INCREASE * 3
    assert tamagotchi.dirtiness == DIRT_INCREASE * 3


def test_feed():
    tamagotchi = Tamagotchi(name="Ooomph!")
    tamagotchi.clock_tick()
    hunger_start = tamagotchi.hunger
    boredom_start = tamagotchi.boredom
    dirtiness_start = tamagotchi.dirtiness

    pudding = Pudding()
    tamagotchi.feed(pudding)
    
    assert tamagotchi.hunger == hunger_start + pudding.hunger_change
    assert tamagotchi.boredom == boredom_start + pudding.boredom_change
    assert tamagotchi.dirtiness == dirtiness_start + pudding.dirtiness_change


def test_sleep():
    tamagotchi = Tamagotchi(name="Ooomph!")
    tamagotchi.clock_tick()
    hunger_start = tamagotchi.hunger
    boredom_start = tamagotchi.boredom
    dirtiness_start = tamagotchi.dirtiness

    tamagotchi.sleep()
    
    assert tamagotchi.hunger == hunger_start + 1
    assert tamagotchi.boredom == boredom_start - 3
    assert tamagotchi.dirtiness == dirtiness_start + 1

