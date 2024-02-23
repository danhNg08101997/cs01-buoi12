import pygame

# Hàm tạo ra 1 surface text
def create_surface_text(f_game:pygame.font.Font, value, color, bg_color, alpha):
    surface_text = f_game.render(value, True, color, bg_color)
    surface_rect = surface_text.get_rect()
    surface_text.set_alpha(alpha)
    
    # Output là surface
    return (surface_text, surface_rect)