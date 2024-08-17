import pygame

# Initialize pygame
pygame.init()

# Set the screen size and caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mi juego")

# Load assets
player_image = pygame.image.load("player.png")

# Set player starting position
player_x = 350
player_y = 250

# Initialize player speed
player_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    screen.blit(player_image, (player_x, player_y))

    # Update the display
    pygame.display.flip()

# Exit pygame
pygame.quit()