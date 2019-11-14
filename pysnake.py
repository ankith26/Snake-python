import pygame
import random
pygame.init()
clock = pygame.time.Clock()
def newfood():
    if borders:
        cord = [random.randint(2,34), random.randint(2,34)]
    else:
        cord = [random.randint(1,35), random.randint(1,35)]
    if cord in array:
        return newfood()
    else:
        return cord
win = pygame.display.set_mode((360, 360))
pygame.display.set_caption('Snake')
running = True
array = [[2,10]]
food = [random.randint(1,36), random.randint(1,36)]
key = "right"
borders = True
while running:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if key != "right":
                    key = "left"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if key != "left":
                    key = "right"
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if key != "down":
                    key = "up"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if key != "up":
                    key = "down"
        else: pass
    if key == "up":
        pos = [array[0][0], array[0][1]-1]
    elif key == "down":
        pos = [array[0][0], array[0][1]+1]
    elif key == "right":
        pos = [array[0][0]+1, array[0][1]]
    elif key == "left":
        pos = [array[0][0]-1, array[0][1]]
    else:
        break
    if borders:
        if pos[0] not in range(2,36) or pos[1] not in range(2,36):
            running = False
            print("Gameover")
        pygame.draw.rect(win, (255,0,255),(0,0,10,360))
        pygame.draw.rect(win, (255,0,255),(0,0,360,10))
        pygame.draw.rect(win, (255,0,255),(350,0,10,360))
        pygame.draw.rect(win, (255,0,255),(0,350,360,10))
    else:
        if pos[0] < 2:
            pos[0] = 36
        elif pos[0] > 36:
            pos[0] = 1
        if pos[1] < 1:
            pos[1] = 36
        elif pos[1] > 36:
            pos[1] = 1
    if pos == food:
        array.append(array[-1])
        food = newfood()
    
    if array.count(pos) >= 1:
        running = False
        print("Gameover")
    else:
        array.insert(0, pos)
        cords = array.pop()
        pygame.draw.rect(win, (255,255,0),(food[0]*10-10,food[1]*10-10,10,10))
        pygame.draw.rect(win, (0,0,0),(cords[0]*10-10,cords[1]*10-10,10,10))
        pygame.draw.rect(win, (255,255,255),(pos[0]*10-10,pos[1]*10-10,10,10))
    pygame.display.update()
pygame.quit()
