import pygame
import numpy as np

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill("Pink")
pygame.display.set_caption("TIc tAc toE!")

Running = True

x_img = pygame.image.load("assets/x.png")
o_img = pygame.image.load("assets/o.png")
x_img = pygame.transform.scale(x_img, (100, 100))
o_img = pygame.transform.scale(o_img, (100, 100))

turn = 'x' #MIN, manusia #'O' Max AI

map = [['','',''],
       ['','',''],
       ['','','']]

def resetBoard():
    global map
    screen.fill("Pink")
    draw_stick()
    virtual_box()

    map = [['','',''],
       ['','',''],
       ['','','']]

def displayText(winOrDraw, player):
    textToDisplay = ''

    if winOrDraw == 'win':
        textToDisplay = f"{player} win"
    elif winOrDraw == 'draw':
        textToDisplay = f"DRAW!"

    font = pygame.font.Font('assets/White Shadows.otf', 50)
    text = font.render(textToDisplay, True, "Red")
    screen.blit(text, (198, 410))
    pygame.display.update()
    pygame.time.delay(1000)
    resetBoard()

def checkWin():
    map_array = np.array(map)
    winner = ''
    winner_info = {
        "row_col_number" : -1,
        "row_col_win" : ""
    }

    main_diagonal = map_array.diagonal()
    off_diagonal = np.fliplr(map_array).diagonal()

    if len(set(main_diagonal)) == 1 and set(main_diagonal) != {''}:
        winner = main_diagonal[0]
        winner_info['row_col_win'] = "main"
    elif len(set(off_diagonal)) == 1 and set(off_diagonal) != {''}:
        winner = off_diagonal[0]
        winner_info["row_col_win"] = "off"

    for row in range(3):
        if winner: break

        if len(set(map_array[row, :])) == 1 and set(map_array[row, :]) != {''}:
            winner = map_array[row, 0]
            winner_info['row_col_number'] = row
            winner_info['row_col_win'] = "row"
    
    for col in range(3):
        if winner: break

        if len(set(map_array[:, col])) == 1 and set(map_array[:, col]) != {''}:
            winner = map_array[0, col]
            winner_info['row_col_number'] = col
            winner_info['row_col_win'] = "col"

    isFull = True if '' not in map_array.flatten() else False

    if isFull and not winner:
        displayText("draw", "")
    if winner:
        displayText("win", winner)



def switch_turn():
    global turn
    turn = 'o' if turn == 'x' else 'x'

def draw_stick():
    pygame.draw.line(screen, "White", pygame.Vector2((100, 200)), pygame.Vector2((400, 200)), 5)
    pygame.draw.line(screen, "White", pygame.Vector2((100, 300)), pygame.Vector2((400, 300)), 5)
    pygame.draw.line(screen, "White", pygame.Vector2((200, 100)), pygame.Vector2((200, 400)), 5)
    pygame.draw.line(screen, "White", pygame.Vector2((300, 100)), pygame.Vector2((300, 400)), 5)

def virtual_box():
    global top_left
    global top_mid
    global top_right
    global mid_left
    global mid_mid
    global mid_right
    global bottom_left
    global bottom_mid
    global bottom_right
    top_left = pygame.Rect(100, 100, 100, 100)
    top_mid = pygame.Rect(200, 100, 100, 100)
    top_right = pygame.Rect(300, 100, 100, 100)
    mid_left = pygame.Rect(100, 200, 100, 100)
    mid_mid = pygame.Rect(200, 200, 100, 100)
    mid_right = pygame.Rect(300, 200, 100, 100)
    bottom_left = pygame.Rect(100, 300, 100, 100)
    bottom_mid = pygame.Rect(200, 300, 100, 100)
    bottom_right = pygame.Rect(300, 300, 100, 100)

def placeXO(mouse_x, mouse_y):
    position = (mouse_x, mouse_y)

    if turn == 'x':
        screen.blit(x_img, position)
    else:
        screen.blit(o_img, position)
    
def collision(section, mouse_x, mouse_y):
    return section.collidepoint(mouse_x, mouse_y)

virtual_box()
draw_stick()

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            placed = False
            if collision(top_left, mouse_x, mouse_y) and not map[0][0]:
                placeXO(top_left.x, top_left.y)
                map[0][0] = turn
            elif collision(top_mid, mouse_x, mouse_y) and not map[0][1]:
                placeXO(top_mid.x, top_mid.y)
                map[0][1] = turn
            elif collision(top_right, mouse_x, mouse_y) and not map[0][2]:
                placeXO(top_right.x, top_right.y)
                map[0][2] = turn
            elif collision(mid_left, mouse_x, mouse_y) and not map[1][0]:
                placeXO(mid_left.x, mid_left.y)
                map[1][0] = turn
            elif collision(mid_mid, mouse_x, mouse_y) and not map[1][1]:
                placeXO(mid_mid.x, mid_mid.y)
                map[1][1] = turn
            elif collision(mid_right, mouse_x, mouse_y) and not map[1][2]:
                placeXO(mid_right.x, mid_right.y)
                map[1][2] = turn
            elif collision(bottom_left, mouse_x, mouse_y) and not map[2][0]:
                placeXO(bottom_left.x, bottom_left.y)
                map[2][0] = turn
            elif collision(bottom_mid, mouse_x, mouse_y) and not map[2][1]:
                placeXO(bottom_mid.x, bottom_mid.y)
                map[2][1] = turn
            elif collision(bottom_right, mouse_x, mouse_y) and not map[2][2]:
                placeXO(bottom_right.x, bottom_right.y)
                map[2][2] = turn

            checkWin()
            switch_turn()
    pygame.display.update()

pygame.quit()