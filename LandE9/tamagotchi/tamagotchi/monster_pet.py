import pygame
from random import choice
from monster_pet_ui import SimulationUI, ActionButton
from monster_pet_logic import (Tamagotchi, TamagotchiState, Play, Clean, Pizza, 
                               Sandwich, Icecream, Pudding, Soda, Rootbeer)


CLICKEVENT = pygame.USEREVENT + 1


def create_name():
    """Return a random troll name from a list of 85 troll names.

    Names were generated with:
    https://www.fantasynamegenerators.com/troll_names.php
    """
    troll_names = ["Alunja", "Alwan", "Alzim", "Anje", "Anji", "Ayagi", 
                   "Ayargajin", "Baliaja", "Dorkuraz", "Eleja", "Erasto", 
                   "Erodjan", "Esha", "Girisha", "Halasuwa", "Hamedi", 
                   "Hokajin", "Jabir", "Jalai", "Jaryaya", "Javinda", "Javyn", 
                   "Jayunya", "Jijel", "Jiranty", "Jojin", "Jubukraa", "Jumoke",
                   "Kanjin", "Katanja", "Kelraz", "Khelynn", "Kululu", "Lakjin",
                   "Malak", "Mandula", "Matuna", "Melkree", "Moza", "Nelina", 
                   "Nyabingi", "Reji", "Renji", "Ronjaty", "Seji", "Senwe", 
                   "Seshi", "Shadrala", "Shamra", "Sligo", "Sollix", "Suja", 
                   "Sulynn", "Tanjin", "Tezzi", "Trezzahn", "Ugoki", "Vanjin", 
                   "Vekuzz", "Vulzala", "Vuzashi", "Vuzembi", "Watu", "Xia", 
                   "Xukundi", "Yaci", "Yashi", "Yavo", "Yera", "Yetu", "Zara", 
                   "Zashi", "Zelaji", "Zenma", "Zeti", "Zhonya", "Ziataaman", 
                   "Ziataja", "Zufem", "Zulgeteb", "Zulja", "Zulkaz", "Zulraja",
                   "Zulwatha", "Zulyafi"]
    return choice(troll_names)


def main():
    name = create_name()
    tamagotchi = Tamagotchi(name=name)

    ui = SimulationUI(tamagotchi, CLICKEVENT)

    running = True
    while running:
        ui.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == CLICKEVENT:
                tamagotchi.clock_tick()

                if tamagotchi.state == TamagotchiState.ALRIGHT:
                    ui.show_run_animation()
                elif tamagotchi.state == TamagotchiState.PLAYING:
                    ui.show_play_animation()
                elif tamagotchi.state == TamagotchiState.DIZZY:
                    ui.show_dizzy_animation()
                elif tamagotchi.state == TamagotchiState.DEAD:
                    # Potentially show another animation or a goodbye screen
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = event.pos
                clicked_action = ui.which_action_was_clicked(click_x, click_y)

                if clicked_action == ActionButton.PIZZA:
                    pizza = Pizza()
                    tamagotchi.feed(pizza)
                    ui.toggle_background("orange")
                elif clicked_action == ActionButton.SANDWICH:
                    sandwich = Sandwich()
                    tamagotchi.feed(sandwich)
                    ui.toggle_background("orange")
                elif clicked_action == ActionButton.ICECREAM:
                    icecream = Icecream()
                    tamagotchi.feed(icecream)
                    ui.toggle_background("orange")
                elif clicked_action == ActionButton.PUDDING:
                    pudding = Pudding()
                    tamagotchi.feed(pudding)
                    ui.toggle_background("orange")
                elif clicked_action == ActionButton.SODA:
                    soda = Soda()
                    tamagotchi.feed(soda)
                    ui.toggle_background("orange")
                elif clicked_action == ActionButton.ROOTBEER:
                    rootbeer = Rootbeer()
                    tamagotchi.feed(rootbeer)
                    ui.toggle_background("orange")
                elif clicked_action == ActionButton.PLAY:
                    play_action = Play()
                    tamagotchi.play(play_action)
                    if tamagotchi.state != TamagotchiState.DIZZY:
                        ui.show_play_animation()
                elif clicked_action == ActionButton.CLEAN:
                    clean_action = Clean()
                    tamagotchi.clean(clean_action)

                    ui.toggle_background()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    ui.toggle_random_mode()

        if tamagotchi.state == TamagotchiState.DEAD:
            running = False
        ui.clock_tick()
    pygame.quit()


if __name__ == "__main__":
    main()
