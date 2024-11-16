import pygame
import os
import random

WIDTH=500
HEIGHT=600

s1=90
s2=90

enemy_speed_factor=1.5
vel=5

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space_invador")

icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
##add charecter 
SPACESHIP_BLUE=pygame.image.load(os.path.join("blue.png"))
BLUE=pygame.transform.scale(SPACESHIP_BLUE,(s1,s2))

#enemy setup
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


#enemyImg = []
#enemyX = []
#enemyY = []
#enemyX_change = []
#enemyY_change = []
#num_of_enemies = 10

def respawn_enemy(i):
    if i < num_of_enemies:
        enemyX[i] = random.randint(0, WIDTH - 64)
        enemyY[i] = random.randint(50, 150)
        enemyX_change[i] = 4 * enemy_speed_factor
        enemyY_change[i] = 40 * enemy_speed_factor

for i in range(num_of_enemies+1):
    YELLOW = pygame.image.load("enemy.png")
    enemyImg.append(YELLOW)
    enemyX.append(0)
    enemyY.append(0)
    enemyX_change.append(0)
    enemyY_change.append(0)
    respawn_enemy(i)


def enemy_movement():
    for i in range(num_of_enemies+1):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4 * enemy_speed_factor
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= WIDTH - 64:
            enemyX_change[i] = -4 * enemy_speed_factor
            enemyY[i] += enemyY_change[i]
#charecter movement
def character_movement(blue,keys):
     if keys[pygame.K_LEFT] and blue.x > vel:
        blue.x -= vel
     if keys[pygame.K_RIGHT] and blue.x < WIDTH - s1 - vel:
         blue.x += vel
     if keys[pygame.K_UP] and blue.y > vel:
         blue.y -= vel
     if keys[pygame.K_DOWN] and blue.y < HEIGHT - s2 - vel:
        blue.y += vel

bg=pygame.image.load("bg.png")
def game_window(blue):
    WIN.blit(bg,(0,0))
    WIN.blit(BLUE,(blue.x,blue.y))

    for i in range(num_of_enemies):
       WIN.blit(enemyImg[i], (enemyX[i], enemyY[i]))

    pygame.display.update()


def main():
    clock.tick(60)
    blue=pygame.Rect(210,480,s1,s2)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        keys=pygame.key.get_pressed()

        character_movement(blue,keys)
        enemy_movement()
        
        game_window(blue)
    pygame.quit()

if __name__=="__main__":
     main()