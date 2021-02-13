#poson nuter 69 now on thonny or whatever ide you use for python, never coming to java, or c/c++/c#, or javascript :)
import pygame, pyautogui,sys,random
pygame.init()


w=800
h=600
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('poson nuter 69 now on thonny or whatever ide you use for python, never coming to java, or c/c++/c#, or javascript :)')

time=0
points=0

nutterer_rad=10
nutterer_x=w//2
nutterer_y=h//2
nutterer_x_change=0
nutterer_y_change=0
nutterer_color=(69,42,255)

poissonBonbon_rad=15
poissonBonbon_x=random.randint(poissonBonbon_rad,w-poissonBonbon_rad)
poissonBonbon_y=random.randint(poissonBonbon_rad,h-poissonBonbon_rad)
poissonBonbon_def_Tim_gauche=275
poissonBonbon_Tim_gauche=poissonBonbon_def_Tim_gauche
poissonBonbon_col=(100, 88, 20)
points=0

font=pygame.font.SysFont('comicsansms',32)
text=font.render(str(points),True,(255,0,204))

while True:
    text=font.render(str(points),True,(255,0,204))
    text_pro=text.get_rect(topright=(w//2,10))
    time+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_i:
                nutterer_y_change=-2
            if event.key==pygame.K_k:
                nutterer_y_change=2
            if event.key==pygame.K_j:
                nutterer_x_change=-2
            if event.key==pygame.K_l:
                nutterer_x_change=2
        elif event.type==pygame.KEYUP:
            nutterer_x_change=nutterer_y_change=0
    poissonBonbon_Tim_gauche-=1
    if poissonBonbon_Tim_gauche<=0:
        poissonBonbon_Tim_gauche=poissonBonbon_def_Tim_gauche
        poissonBonbon_x=random.randint(poissonBonbon_rad,w-poissonBonbon_rad)
        poissonBonbon_y=random.randint(poissonBonbon_rad,h-poissonBonbon_rad)
        points=0
    elif pygame.draw.circle(screen,poissonBonbon_col,(poissonBonbon_x,poissonBonbon_y),poissonBonbon_rad).colliderect(pygame.draw.circle(screen,nutterer_color,(nutterer_x,nutterer_y),nutterer_rad)):
        poissonBonbon_Tim_gauche=poissonBonbon_def_Tim_gauche
        poissonBonbon_x=random.randint(poissonBonbon_rad,w-poissonBonbon_rad)
        poissonBonbon_y=random.randint(poissonBonbon_rad,h-poissonBonbon_rad)
        points+=1
    screen.fill((89, 115, 54))
    nutterer_x+=nutterer_x_change
    nutterer_y+=nutterer_y_change
    
    if nutterer_x-nutterer_rad<=0:
        nutterer_x=w-nutterer_rad-3
    elif nutterer_x+nutterer_rad>=w:
        nutterer_x=nutterer_rad+3
    elif nutterer_y-nutterer_rad<=0:
        nutterer_y=h-nutterer_rad-3
    elif nutterer_y+nutterer_rad>=h:
        nutterer_y=nutterer_rad+3
    
    pygame.draw.circle(screen,poissonBonbon_col,(poissonBonbon_x,poissonBonbon_y),poissonBonbon_rad)
    pygame.draw.circle(screen,nutterer_color,(nutterer_x,nutterer_y),nutterer_rad)
    screen.blit(text,text_pro)
    pygame.display.update()
    