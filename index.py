import random
import pygame
pygame.init()
pygame.display.set_caption('Basic Snake')

win = pygame.display.set_mode((800, 800))

move = True
game_over = False

left = False
right = False
up = False
down = False

for y in range(0, 16):
    for x in range(0, 16):
        pygame.draw.rect(win, (0, 0, 0), (x * 50, y * 50, 50, 50))


snake_pos = [(1, 1)]
snake_length = 1
apple_pos = [5, 5]

for i in range(snake_length):
    pygame.draw.rect(win, (0, 255, 0), (snake_pos[i][0] * 50, snake_pos[i][1] * 50, 50, 50))


pygame.draw.rect(win, (255, 0, 0), (apple_pos[0] * 50, apple_pos[1] * 50, 50, 50))


def new_apple():
    global apple_pos
    global snake_length
    global snake_pos

    r1 = random.randint(0, 15)
    r2 = random.randint(0, 15)

    temp_apple_pos = (r1, r2)

    go_again = False

    for i in snake_pos:
        if temp_apple_pos == i:
            go_again = True

    if go_again == True:
        new_apple()
    else:
        apple_pos[0] = temp_apple_pos[0]
        apple_pos[1] = temp_apple_pos[1]


while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if move:
                if event.key == 100:  # RIGHT
                    if not left:
                        left = False
                        right = True
                        up = False
                        down = False
                elif event.key == 119:  # UP
                    if not down:
                        left = False
                        right = False
                        up = True
                        down = False
                elif event.key == 97:  # LEFT
                    if not right:
                        left = True
                        right = False
                        up = False
                        down = False
                elif event.key == 115:  # DOWN
                    if not up:
                        left = False
                        right = False
                        up = False
                        down = True


    if right:
        snake_pos.insert(snake_length-1, (snake_pos[snake_length - 1][0], snake_pos[snake_length - 1][1]))

        temp = list(snake_pos[0])
        temp[0] += 1
        snake_pos.insert(0, tuple(temp))

        for y in range(0, 16):
            for x in range(0, 16):
                pygame.draw.rect(win, (0, 0, 0), (x * 50, y * 50, 50, 50))

        if not snake_length == 1:
            for i in range(snake_length):
                pygame.draw.rect(win, (0, 255, 0), (snake_pos[i][0] * 50, snake_pos[i][1] * 50, 50, 50))
        else:
            pygame.draw.rect(win, (0, 255, 0), (snake_pos[0][0] * 50, snake_pos[0][1] * 50, 50, 50))


    if left:
        snake_pos.insert(snake_length-1, (snake_pos[snake_length - 1][0], snake_pos[snake_length - 1][1]))

        temp = list(snake_pos[0])
        temp[0] -= 1
        snake_pos.insert(0, tuple(temp))

        for y in range(0, 16):
            for x in range(0, 16):
                pygame.draw.rect(win, (0, 0, 0), (x * 50, y * 50, 50, 50))


        if not snake_length == 1:
            for i in range(snake_length):
                pygame.draw.rect(win, (0, 255, 0), (snake_pos[i][0] * 50, snake_pos[i][1] * 50, 50, 50))
        else:
            pygame.draw.rect(win, (0, 255, 0), (snake_pos[0][0] * 50, snake_pos[0][1] * 50, 50, 50))


    if up:
        snake_pos.insert(snake_length-1, (snake_pos[snake_length - 1][0], snake_pos[snake_length - 1][1]))

        temp = list(snake_pos[0])
        temp[1] -= 1
        snake_pos.insert(0, tuple(temp))

        for y in range(0, 16):
            for x in range(0, 16):
                pygame.draw.rect(win, (0, 0, 0), (x * 50, y * 50, 50, 50))


        if not snake_length == 1:
            for i in range(snake_length):
                pygame.draw.rect(win, (0, 255, 0), (snake_pos[i][0] * 50, snake_pos[i][1] * 50, 50, 50))
        else:
            pygame.draw.rect(win, (0, 255, 0), (snake_pos[0][0] * 50, snake_pos[0][1] * 50, 50, 50))


    if down:
        snake_pos.insert(snake_length-1, (snake_pos[snake_length - 1][0], snake_pos[snake_length - 1][1]))

        temp = list(snake_pos[0])
        temp[1] += 1
        snake_pos.insert(0, tuple(temp))

        for y in range(0, 16):
            for x in range(0, 16):
                pygame.draw.rect(win, (0, 0, 0), (x * 50, y * 50, 50, 50))


        if not snake_length == 1:
            for i in range(snake_length):
                pygame.draw.rect(win, (0, 255, 0), (snake_pos[i][0] * 50, snake_pos[i][1] * 50, 50, 50))
        else:
            pygame.draw.rect(win, (0, 255, 0), (snake_pos[0][0] * 50, snake_pos[0][1] * 50, 50, 50))


    if snake_pos[0][0] == apple_pos[0] and snake_pos[0][1] == apple_pos[1]:
        snake_length += 1
        new_apple()

    
    while len(snake_pos) > snake_length:
        snake_pos.pop()

    if not game_over:
        for x in range(len(snake_pos)):
            if not x == 0:
                if snake_pos[0] == snake_pos[x]:
                    print("Game Over! - Hit Self (Score = " + str(snake_length) + ")")
                    right = False
                    left = False
                    down = False
                    up = False
                    move = False
                    game_over = True

                    break


        if snake_pos[0][0] * 50 < 0 or snake_pos[0][0] * 50 > 750 or snake_pos[0][1] * 50 < 0 or snake_pos[0][1] * 50 > 750:
            print("Game Over! - Hit Wall (Score = " + str(snake_length) + ")")
            right = False
            left = False
            down = False
            up = False
            move = False
            game_over = True


        if not game_over:
            if snake_length == 100:
                print("Victory! You beat the food chain!")
                right = False
                left = False
                down = False
                up = False
                move = False
                game_over = True


    pygame.draw.rect(win, (255, 0, 0), (apple_pos[0] * 50, apple_pos[1] * 50, 50, 50))
    pygame.display.update()
