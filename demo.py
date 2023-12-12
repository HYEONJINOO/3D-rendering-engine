import pygame
import random
import math
import engine as e

pygame.init()

RES = [1280,720]
engine = e.Engine(RES)
clock = pygame.time.Clock()
display = pygame.display.set_mode(RES)

time = 0
scroll = [0, 0]
colors = [[242,129,24], [85,68,52]]

# box generation
for y in range(20):
    for x in range(20):
        color = random.choice(colors)
        side_color = [x-12 for x in color]
        engine.add_box(e.Box(
                pygame.Rect(x*20, y*15, 15, 10), 
                random.choice(range(10, 50, 4)), 
                color,
                side_color
        ))

def render(surface):
    surface.fill((255,255,255))
    engine.run_cycle(surface, scroll)
    pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    keys = pygame.key.get_pressed()
    velocity = 3  
    if keys[pygame.K_LSHIFT]:
        velocity /= 1.8
    if keys[pygame.K_UP]:
        scroll[1] += velocity
    if keys[pygame.K_DOWN]:
        scroll[1] -= velocity
    if keys[pygame.K_RIGHT]:
        scroll[0] -= velocity
    if keys[pygame.K_LEFT]:
        scroll[0] += velocity


    for i, box in enumerate(engine.box_list):
        value = math.sin(pygame.time.get_ticks()/1000 + i)
        if 10 >= box.width + value or 70 <= box.width + value:
            value = 0
        box.width += value
    time += 1

    render(display)

pygame.quit()
