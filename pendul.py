#am ascuns o chestie pe care pygame o tot printa ma enerva
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#declaram librarii
import pygame
import math
#declaram variabile
width, height = 1000, 1000
pornit = False
lungime = 0
unghi = 0
velocitate = 0
white = (255,255,255)
black = (0,0,0)
pygame.init()
background = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#declaram functii
def draw(bg):
    global x,y,radius
    pygame.draw.lines(bg, black,False, [(int(width/2),0), (x, y)], 2)
    pygame.draw.circle(bg, black, (x, y), 8)
def lungime_unghi():
    global x,y,radius,lungime
    lungime = math.sqrt(math.pow(x - width/2, 2) + math.pow(y , 2))
    #print(lungime)
    unghi = math.asin((x - width/2)/ lungime)
    return (unghi, lungime)
def traiectorie(lungime):
    global x,y,radius
    x = round(width/2 + lungime * math.sin(unghi))
    y = round( lungime * math.cos(unghi))
def update():
    background.fill(white)
    if pornit == True:
     draw(background)
    pygame.display.update()
def nulifica():
    global lungime,unghi,Aacc,ac,velocitate
    lungime=0
    unghi=0
    ac=0
    velocitate=0
#rulam functia
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            nulifica()
            x,y= pygame.mouse.get_pos()
            unghi, lungime = lungime_unghi()
            const=float(lungime/100)
            amortizare=0.99
            ac=-1/pow(10,const/3)
            pornit = True
    if pornit:
        velocitate=(velocitate+ac*math.sin(unghi))*amortizare
        unghi += velocitate
        traiectorie(lungime)
    update()

pygame.quit()

