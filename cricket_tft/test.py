import json
import sys
import pygame
import os
import time

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

main_screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

CYAN = theme['COLOR']['CYAN']
MAROON = theme['COLOR']['MAROON']
RED = theme['COLOR']['RED']
GREEN = theme['COLOR']['GREEN']
VIOLET = theme['COLOR']['VIOLET']

pygame.font.init()

FONT_SMALL_BOLD = pygame.font.Font(FONT_PATH + 'Roboto-Medium.ttf', 14)
CURR_SCORE_FONT = pygame.font.Font(FONT_PATH + 'Roboto-Bold.ttf', 40)

string = '9'
print(FONT_SMALL_BOLD, FONT_SMALL_BOLD.size(string))
# while True:
#     main_screen.fill(CYAN)
#     pygame.draw.line(screen, RED, [0, 240], [320, 240], 5)
#     pygame.draw.line(screen, GREEN, [160, 0], [160, 240], 5)
#     screen.blit((FONT_SMALL_BOLD.render(string, True, MAROON)), (43, 96))
#     pygame.display.update()

curr_score = {"Runs": "72", "Wickets": "6", "Overs": '20'}
bat1 = {"Name": "Virat Kohli", "Runs": '20',
        "Balls": '11', "4s": '2', "6s": '1', "SR": '181.81'}
bat2 = {"Name": "Rohit Sharma", "Runs": '130',
        "Balls": '125', "4s": '22', "6s": '28', "SR": '120.00'}
bowler1 = {"Name": "Bhuvneshwar Kumar", "Overs": '20', "Maidens": '4',
           "Runs": '75', "Wickets": '2', "No_Balls": '0', "Wide": '2', "Eco": '3.80'}
bowler2 = {"Name": "Reece Topley", "Overs": '55', "Maidens": '52',
           "Runs": '39', "Wickets": '52', "No_Balls": '0', "Wide": '2', "Eco": '12.60'}

score= curr_score['Runs']+'/'+curr_score['Wickets']
SCORE_XY = (80,100)


SR_X = 266
SIX_X = 252
FOUR_X = 222
BALLS_X = 195
RUNS_X = 162

class DrawBatsman:
    def __init__(self, surf, string, font, color, y):
        self.string = string
        self.font = font
        self.color = color
        self.y = y
        self.size = self.font.size('2')[0]
        self.surf = surf

    def drawbatsman(self, offset=0):
        name_x = 10
        sr_x = 310 - self.font.size('.')[0]-self.font.size(self.string['SR'])[0]
        six_x = 252 - self.font.size(self.string['6s'])[0]
        four_x = 222 - self.font.size(self.string['4s'])[0]
        b_x = 195 - self.font.size(self.string['Balls'])[0]
        bat_run_x = 162 - self.font.size(self.string['Runs'])[0]

        # print(name_x,bat_run_x,b_x,four_x,six_x,sr_x)

        self.surf.blit(self.font.render(
            self.string['Name'], True, self.color), (name_x, self.y))
        self.surf.blit(self.font.render(
            self.string['Runs'], True, self.color), (bat_run_x, self.y))
        self.surf.blit(self.font.render(
            self.string['Balls'], True, self.color), (b_x, self.y))
        self.surf.blit(self.font.render(
            self.string['4s'], True, self.color), (four_x, self.y))
        self.surf.blit(self.font.render(
            self.string['6s'], True, self.color), (six_x, self.y))
        self.surf.blit(self.font.render(
            self.string['SR'], True, self.color), (sr_x, self.y))

    def drawbowler(self, offset=0):

        name_x = 10
        eco_x = 310 - self.font.size('.')[0]-self.font.size(self.string['Eco'])[0]
        wkt_x = 252 - self.font.size(self.string['Wickets'])[0]
        run_x = 222 - self.font.size(self.string['Runs'])[0]
        m_x = 195 - self.font.size(self.string['Maidens'])[0]
        ovr_x = 162 - self.font.size(self.string['Overs'])[0]

        self.surf.blit(self.font.render(
            self.string['Name'], True, self.color), (name_x, self.y))
        self.surf.blit(self.font.render(
            self.string['Overs'], True, self.color), (ovr_x, self.y))
        self.surf.blit(self.font.render(
            self.string['Maidens'], True, self.color), (m_x, self.y))
        self.surf.blit(self.font.render(
            self.string['Runs'], True, self.color), (run_x, self.y))
        self.surf.blit(self.font.render(
            self.string['Wickets'], True, self.color), (wkt_x, self.y))
        self.surf.blit(self.font.render(
            self.string['Eco'], True, self.color), (eco_x, self.y))

def curr_score(surf, string, font, color,location):

    surf.blit(font.render(string,True,color),location)

while True:
    main_screen.fill(CYAN)
    curr_score(main_screen,score,CURR_SCORE_FONT,VIOLET,SCORE_XY)
    DrawBatsman(main_screen, bat1, FONT_SMALL_BOLD, MAROON, 300).drawbatsman()
    DrawBatsman(main_screen, bat2, FONT_SMALL_BOLD, MAROON, 320).drawbatsman()
    DrawBatsman(main_screen, bowler1, FONT_SMALL_BOLD, MAROON, 360).drawbowler()
    DrawBatsman(main_screen, bowler2, FONT_SMALL_BOLD, MAROON, 380).drawbowler()
    pygame.display.update()