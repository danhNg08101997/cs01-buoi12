import pygame, method, sys
from method import create_surface_text

pygame.init()

# Khai báo cửa sổ
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Galaxy War')

# Xây dựng player (surface: hình, rect, sound...)
player_img = pygame.image.load('./galaxy war/graphics/air_craft.png')
player_rect = player_img.get_rect()
player_rect.x = SCREEN_WIDTH  / 2 - player_rect.width / 2
player_rect.y = SCREEN_HEIGHT - 200

# Set up các surface text
f_game = pygame.font.Font('./galaxy war/graphics/subatomic.ttf', 32)

# Set up background
bg_game = pygame.image.load('./galaxy war/graphics/background_space.jpg')
bg_game = pygame.transform.scale(bg_game, (SCREEN_WIDTH,SCREEN_HEIGHT))

# Vòng lặp game
running = True
while running:
    # Background
    screen.blit(bg_game,(0,0))
    
    # Xây dựng event thoát game
    for event in pygame.event.get(): #vòng lặp từng phím
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION: #MOUSEMOTION là rê chuột
            #Lấy ra tọa độ chuột
            x,y = pygame.mouse.get_pos()
            player_rect.x = x - player_rect.width / 2
            player_rect.y = y - player_rect.height / 2
            
    # Xử lý blit các surface
    screen.blit(player_img, player_rect) #1. truyền tuple tọa độ, 2. truyền vào rect
    
    #Xử lý surface text
    # Mạng
    live_text, live_rect = create_surface_text(f_game,f'Live: {5}','Red', 'White',90)
    live_rect = (0, SCREEN_HEIGHT - 100)
    
    # Điểm
    score_text, score_rect = create_surface_text(f_game, f'Score: {0}','Red', 'White', 90)
    score_rect = (SCREEN_WIDTH / 2 - score_text.get_width() / 2,SCREEN_HEIGHT - 100)
    
    # Level
    level_text, level_rect = create_surface_text(f_game, f'Level: {1}', 'Red', 'White', 90)
    level_rect = (SCREEN_WIDTH - level_rect.width, SCREEN_HEIGHT - 100)
    
    screen.blit(live_text, live_rect)
    screen.blit(score_text, score_rect)
    screen.blit(level_text,level_rect)
    # Cập nhật game
    pygame.display.flip()

# Thoát khỏi vòng lặp thì tắt game
pygame.quit()
sys.exit()