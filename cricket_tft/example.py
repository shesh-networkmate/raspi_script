import sys, pygame, os, time

os.environ["SDL_FBDEV"] = "/dev/fb1"
pygame.init()

size = width, height = 320,480
speed = [5, 5]
red = 255,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
print(ballrect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    # print(ballrect,ballrect.left,ballrect.right,ballrect.top,ballrect.bottom,speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(red)
    screen.blit(ball, ballrect)
    time.sleep(0.1)
    pygame.display.flip()