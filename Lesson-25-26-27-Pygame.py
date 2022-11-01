#!/bin/python3
#coding: UTF8
import pygame

#while True:
#    pygame.display.flip() - запуск пустого экрана в цикле

MAX_X = 800     # указания ширины окна
MAX_Y = 600     # указания высоты окна
IMG_SIZE_X=92
IMG_SIZE_Y=61

game_over = False   # указание значения переменной окончания игры
bg_color = (0, 20, 0) # создание переменной слегка зеленого цвета, в формате RGB

pygame.init()       # инициализация ресурсов модуля pygame
screen = pygame.display.set_mode((MAX_X,MAX_Y)) #, pygame.FULLSCREEN) # инициализация дисплея (и перевод в полноэкранный режим)
pygame.display.set_caption("PyGame-Game")  # указание названия окна

# print(pygame.image.get_extended())    - 
# проверка поддержание дополнительных
#  расширений изображений кроме BMP

myimage = pygame.image.load("./files/robot.jpeg").convert() # запись в область памяти файла-картинки
# myimage = pygame.transform.scale2x(myimage) # (IMG_SIZE_X, IMG_SIZE_X))  # преобразование размеров карттинки в случае необходимости

x = 300
y = 300

move_left = False
move_right = False
move_up = False
move_down = False

# --------------- MAIN GAME LOOP
while game_over == False:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:    # перехват клика мышки и 
            x, y = event.pos                        # и передача положения курсора - объекту

        if event.type == pygame.KEYDOWN:            # перехват нажатия клавиши 
            if event.key == pygame.K_ESCAPE:        # проверка какая клавиша нажата
                game_over = True                    # действия изза нажатия конкретной кнопки
            if event.key == pygame.K_LEFT:
                # x -= 25   # движение без удержания, рывками
                move_left = True
            if event.key == pygame.K_RIGHT:         # проверка какая клавиша нажата
                # x += 25                             # действия изза нажатия конкретной кнопки
                move_right = True
            if event.key == pygame.K_UP:
                # y -= 25
                move_up = True
            if event.key == pygame.K_DOWN:
                # y += 25
                move_down = True
            
        if event.type == pygame.KEYUP:            # перехват отжатия клавиши 
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:         
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            
    if move_left == True:
        x -= 1
        if x < 0:
            x = 0
    if move_right == True:
        x += 1
        if x > MAX_X - IMG_SIZE_X:
            x = MAX_X - IMG_SIZE_X
    if move_up == True:
        y -= 1
        if y < 0:
            y = 0
    if move_down == True:
        y += 1
        if y > MAX_Y - IMG_SIZE_Y:
            y = MAX_Y - IMG_SIZE_Y       

    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()