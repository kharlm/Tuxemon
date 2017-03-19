import pygame

GAME_EVENT = pygame.USEREVENT + 0
FOO_EVENT = pygame.USEREVENT + 1
NORTH_EVENT = pygame.USEREVENT + 2
EAST_EVENT = pygame.USEREVENT + 3
SOUTH_EVENT = pygame.USEREVENT + 4
WEST_EVENT = pygame.USEREVENT + 5
STOP_EVENT = pygame.USEREVENT + 6
MENU_EVENT = pygame.USEREVENT + 7
MOVE_EVENT =    pygame.USEREVENT + 8
BATTLE_EVENT = pygame.USEREVENT + 9

MONSTERS_EVENT = pygame.USEREVENT + 30
BAG_EVENT = pygame.USEREVENT + 31
LOAD_EVENT = pygame.USEREVENT + 32
SAVE_EVENT = pygame.USEREVENT + 33
EXIT_EVENT = pygame.USEREVENT + 34


FIGHT_EVENT = pygame.USEREVENT + 20
ITEM_EVENT = pygame.USEREVENT + 21
# RUN_EVENT = pygame.USEREVENT + 9
SWAP_EVENT = pygame.USEREVENT + 23



INPUT_EVENT = 0


#To call an event use:
#   pygame.event.post(pygame.event.Event(MENU_EVENT))

VOICE_EVENT_SET = [NORTH_EVENT, EAST_EVENT, SOUTH_EVENT, WEST_EVENT,
    STOP_EVENT, MENU_EVENT, MOVE_EVENT, BATTLE_EVENT]
