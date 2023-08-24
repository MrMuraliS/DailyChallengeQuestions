import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 400
height = 700

# Colors
red = (255, 0, 0)
white = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Love Symbol")

# Load heart image
heart_img = pygame.image.load("heart.png")  # Replace with the path to your heart image
heart_img = pygame.transform.scale(heart_img, (50, 50))

# Create a list to store heart objects
hearts = []


class Heart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])


# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Create new hearts at random positions
    if len(hearts) < 20:
        new_heart = Heart(random.randint(0, width - 50), random.randint(0, height - 50))
        hearts.append(new_heart)

    # Update and draw hearts
    for heart in hearts:
        heart.x += heart.speed_x
        heart.y += heart.speed_y

        # Boundary checking
        if heart.x <= 0 or heart.x >= width - 50:
            heart.speed_x *= -1
        if heart.y <= 0 or heart.y >= height - 50:
            heart.speed_y *= -1

        # Draw the heart
        screen.blit(heart_img, (heart.x, heart.y))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
