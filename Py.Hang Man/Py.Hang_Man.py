import pygame
import sys
import random
import time

pygame.init()
clock = pygame.time.Clock()
width = 800
height = 500 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")
icon = pygame.image.load("image")
pygame.display.set_icon(icon)
game_over = False
row = 2
col = 13
gap = 20
size = 40
boxes = []
for row in range(row):
    for col in range(col):
        x = ((col * gap) + gap) + (size * col)
        y = ((row * gap) + gap) + (size * row) + 350
        box = pygame.Rect(x, y, size, size)
        boxes.append(box)

buttons = []
A = 65

for ind, box in enumerate(boxes):
    letter = chr(A + ind)
    button = [box, letter]
    buttons.append(button)
    # To draw buttons
    def draw_buttons(buttons):
        for box, letter in buttons:
            btn_text = font.render(letter, True, (0, 0, 0))
            btn_rect = btn_text.get_rect(center=
                                  (box.x + 20, box.y + 20))
            screen.blit(btn_text, btn_rect)
            pygame.draw.rect(screen, (0, 0, 0), box, 2)

    def display_guess():
        display_text = ''
        for letter in word:
            if letter in guessed:
                display_text += f"{letter} "
            else:
                display_text += '_ '
        text = letter_font.render(display_text, True, (0, 0, 0,))
        screen.blit(text, (400, 200))


images = []    
hangman_status = 0

words = ['PYGAME', 'PYTHON', 'JAVA', 'HELLO', 'WORLD',
         'HANGMAN', 'TIME', 'TURTLE', 'RANDOM']
word = random.choice(words)
guessed = []

image = pygame.image.load("image")
images.append(image)

font = pygame.font.SysFont("arial", 30)
game_font = pygame.font.SysFont("arial", 80)
letter_font = pygame.font.SysFont("arial", 60)

title = "Hangman"
title_text = game_font.render(title, True, (0, 0, 0))
title_rect = title_text.get_rect(center=(width // 2,
                 title_text.get_height() // 2 + 10))

running = True
while running:
    screen.fill((255, 255, 255))
    # checking for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit event
            running = False
        # checking for mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = event.pos 


    for button, letter in buttons:
        if button.collidepoint(click_pos):
            if letter not in word:
                hangman_status += 1
            if hangman_status == 6:
                game_over = True
            guessed.append(letter)
            buttons.remove([button, letter])
    # displaying the images accordingly
    for i in range(5):
        if hangman_status == 1:
            image = pygame.image.load("image")
            images.append(image) 
        elif hangman_status == 2:
            image = pygame.image.load("image")
            images.append(image)
        elif hangman_status == 3:
            image = pygame.image.load("image")
            images.append(image)
        elif hangman_status == 4:
            image = pygame.image.load("image")
            images.append(image)
        elif hangman_status == 5:
            image = pygame.image.load("image")
            images.append(image)
        elif hangman_status == 6:
            running = False
    screen.blit(image, (150, 150))
    for box in boxes:
        pygame.draw.rect(screen, (0, 0, 0), box, 2)


    won = True
    for letter in word:
        if letter not in guessed:
            won = False

    if won:
        game_over = True
        game_text = "you won!!!"
    else:
        game_text = "you lost!!"

    draw_buttons(buttons)
    display_guess()
    screen.blit(title_text, title_rect)
    clock.tick(50)
    pygame.display.update()

    # Displaying the result text
    if game_over:
        screen.fill((255, 255, 255))
        text = game_font.render(game_text, True, (0, 0, 0))
        text_rect = text.get_rect(center = (width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()
pygame.quit()                                                                                
