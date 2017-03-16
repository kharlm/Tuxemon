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


MONSTERS_EVENT = pygame.USEREVENT + 30
BAG_EVENT = pygame.USEREVENT + 31
LOAD_EVENT = pygame.USEREVENT + 32
SAVE_EVENT = pygame.USEREVENT + 33
EXIT_EVENT = pygame.USEREVENT + 34


FIGHT_EVENT = pygame.USEREVENT + 20
ITEM_EVENT = pygame.USEREVENT + 21
RUN_EVENT = pygame.USEREVENT + 22


INPUT_EVENT = 0


#To call an event use:
#   pygame.event.post(pygame.event.Event(MENU_EVENT))

VOICE_EVENT_SET = [NORTH_EVENT, EAST_EVENT, SOUTH_EVENT, WEST_EVENT, STOP_EVENT, MENU_EVENT, MOVE_EVENT, MONSTERS_EVENT, BAG_EVENT, LOAD_EVENT, SAVE_EVENT, EXIT_EVENT, FIGHT_EVENT, ITEM_EVENT, RUN_EVENT]
