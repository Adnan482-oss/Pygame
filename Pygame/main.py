import pygame

WIDTH=500
HEIGHT=600

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space_invade")

icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
    pygame.quit()
if __name__=="__main__":
    main()
            