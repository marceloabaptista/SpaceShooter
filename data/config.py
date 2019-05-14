import pygame


W = 800
H = 600
HW = W / 2
HH = H / 2
screen = pygame.display.set_mode((W, H))
image_dir = 'assets/PNG/'
ship_blue = pygame.image.load(image_dir + 'playerShip1_blue.png').convert_alpha()
bg_black = pygame.image.load('assets/Backgrounds/black.png').convert_alpha()
bg_blue = pygame.image.load('assets/Backgrounds/blue.png').convert_alpha()
bg_purple = pygame.image.load('assets/Backgrounds/purple.png').convert_alpha()
meteor_brown_big = pygame.image.load(image_dir + 'Meteors/meteorBrown_big1.png').convert_alpha()
meteor_grey_big = pygame.image.load(image_dir + 'Meteors/meteorGrey_big1.png').convert_alpha()
laser_blue = pygame.image.load(image_dir + 'Lasers/laserBlue07.png').convert_alpha()
laser_blue_impact = pygame.image.load(image_dir + 'Lasers/laserBlue08.png').convert_alpha()
clock = pygame.time.Clock()
black = (0, 0, 0)
vel = 5
FPS = 120
game_exit = False
meteors = []
lasers = []
laser_cooldown_max = 30
laser_cooldown_count = 0
laser_cooldown = False
laser_hit = False
meteor_spawn_chance = 80