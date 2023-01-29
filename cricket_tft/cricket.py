import json
import sys, pygame, os, time

os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()

PATH = sys.path[0] + '/'
ICON_PATH = PATH + '/icons/'
FONT_PATH = PATH + '/fonts/'
LOG_PATH = PATH + '/logs/'

config_data = open(PATH + 'config.json').read()
config = json.loads(config_data)

theme_config = config["THEME"]

theme_settings = open(PATH + theme_config).read()
theme = json.loads(theme_settings)

DISPLAY_WIDTH = int(config["DISPLAY"]["WIDTH"])
DISPLAY_HEIGHT = int(config["DISPLAY"]["HEIGHT"])


screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

CYAN = theme['COLOR']['CYAN']
MAROON = theme['COLOR']['MAROON']
RED = theme['COLOR']['RED']
GREEN = theme['COLOR']['GREEN']

pygame.font.init()
FONT_SMALL_BOLD = pygame.font.Font(FONT_PATH + 'Roboto-Medium.ttf', 14)
string='100.41'
print(FONT_SMALL_BOLD,FONT_SMALL_BOLD.size(string))
while True:
    screen.fill(CYAN)
    pygame.draw.line(screen,RED,[0,240],[320,240],5)
    pygame.draw.line(screen,GREEN,[160,0],[160,240],5)
    screen.blit((FONT_SMALL_BOLD.render(string, True, MAROON)),(43,96))
    pygame.display.update()
    
