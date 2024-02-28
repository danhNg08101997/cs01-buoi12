import pygame, sys, random
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

# Tạo 1 collection chứa đạn
lst_bullet:list[pygame.Rect] = []
    # tốc độ của đạn
speed_bullet = 2

# Tạo ra 1 list chứa nhiều thiên thạch
meteor_image = pygame.image.load('./galaxy war/graphics/meteor.png')
    # collection chứa thiên thạch
lst_meteor:list[pygame.Rect] = []
    # tốc độ rơi của thiên thạch
speed_meteor = 1
    # thời gian tạo thiên thạch
time_meteor_start = 0
    # thời gian rơi
time_span_meteor = 1000

# Tạo biến lưu trữ
score = 0
level = 1
live = 5

# Xử lý âm thanh
sound_bg = pygame.mixer.Sound('./galaxy war/sounds/music.wav')
attack = pygame.mixer.Sound('./galaxy war/sounds/laser.ogg')
explosion = pygame.mixer.Sound('./galaxy war/sounds/explosion.wav')
sound_bg.play(-1)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Tạo ra 1 viện đạn đưa vào list đạn
            bullet_image = pygame.image.load('./galaxy war/graphics/laser.png')
            bullet_rect = bullet_image.get_rect()
            # lấy tọa độ đạn tại vị trí đầu của mũi máy bay
            # bullet_rect = player_rect.midtop #(player.rect.x + player_rect.width/2, player_rect.y)
            bullet_rect.x = player_rect.x + player_rect.width/2
            bullet_rect.y = player_rect.y
            # lưu đạn vào lst_bullet
            lst_bullet.append(bullet_rect)
            print('lst_bullet: ',lst_bullet)
            # Mỗi lần bắn thì phát ra âm thanh
            attack.play()
            
    # Xử lý thiên thạch
    current_time_meteor = pygame.time.get_ticks() #lấy thời gian game hiện tại
    if current_time_meteor - time_meteor_start >= time_span_meteor: # 1s rơi 1 lần
        # Tạo ra 1 thiên thạch rect đưa vào list
        meteor_rect = meteor_image.get_rect()
        meteor_rect.x = random.randint(0, SCREEN_WIDTH - meteor_rect.width)
        meteor_rect.y = 0
        lst_meteor.append(meteor_rect)
        print('lst_meteor: ', lst_meteor)
        # Gán lại thời gian start
        time_meteor_start = current_time_meteor
        
    # xử lý đạn
    for bullet_rect in lst_bullet:
        screen.blit(bullet_image,bullet_rect)
        # sau khi blit từng viên đạn thì giảm y của từng viên đạn
        bullet_rect.y -= speed_bullet
        # tối ưu
        if bullet_rect.y < 0:
            lst_bullet.remove(bullet_rect)
        # xét xem từng viên đạn có chạm vào thiên thạch hay không
        for meteor_rect in lst_meteor:
            if bullet_rect.colliderect(meteor_rect):
                explosion.play()
                score += 100
                lst_meteor.remove(meteor_rect)
                lst_bullet.remove(bullet_rect)
                # Xử lý lên level
                if score % 1000 == 0 and score != 0:
                    level += 1
                    # Tăng độ khó game
                    time_span_meteor -= 100
    
    # Xử lý thiên thạch rơi
    for meteor_rect in lst_meteor:
        screen.blit(meteor_image, meteor_rect)
        # thay đổi vị trí thiên thạch
        meteor_rect.y += speed_meteor / 2
        meteor_rect.x += random.randint(0, 10) * 0.1
        # tối ưu thiên thạch
        if meteor_rect.x < 0 or meteor_rect.x > SCREEN_WIDTH or meteor_rect.y > SCREEN_HEIGHT:
            lst_meteor.remove(meteor_rect)
        # Xử lý khi thiên thạch rơi trúng máy bay
        if meteor_rect.colliderect(player_rect):
            live -= 1
            # Xóa thiên thạch
            lst_meteor.remove(meteor_rect)
            if live < 0:
                score = 'Game over'
                
    # Xử lý blit các surface
    screen.blit(player_img, player_rect) #1. truyền tuple tọa độ, 2. truyền vào rect
    
    #Xử lý surface text
    # Mạng
    live_text, live_rect = create_surface_text(f_game,f'Live: {live}','Red', 'White',90)
    live_rect = (0, SCREEN_HEIGHT - 100)
    
    # Điểm
    score_text, score_rect = create_surface_text(f_game, f'Score: {score}','Red', 'White', 90)
    score_rect = (SCREEN_WIDTH / 2 - score_text.get_width() / 2,SCREEN_HEIGHT - 100)
    
    # Level
    level_text, level_rect = create_surface_text(f_game, f'Level: {level}', 'Red', 'White', 90)
    level_rect = (SCREEN_WIDTH - level_rect.width, SCREEN_HEIGHT - 100)
    
    screen.blit(live_text, live_rect)
    screen.blit(score_text, score_rect)
    screen.blit(level_text,level_rect)
    
    # Cập nhật game
    pygame.display.flip()

# Thoát khỏi vòng lặp thì tắt game
pygame.quit()
sys.exit()