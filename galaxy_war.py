import pygame

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

# Vòng lặp game
running = True
while running:
    # Background
    screen.fill((255,255,255))
    
    # Xây dựng event thoát game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Xử lý blit các surface
    screen.blit(player_img, player_rect) #1. truyền tuple tọa độ, 2. truyền vào react
    
    # Cập nhật game
    pygame.display.flip()

# Thoát khỏi vòng lặp thì tắt game
pygame.quit()