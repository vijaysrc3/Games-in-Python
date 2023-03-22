import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping Pong")

# Set up the game objects
BALL_RADIUS = 10
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = 5
ball_dy = 5

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
player1_x = 50
player1_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_x = WINDOW_WIDTH - 50 - PADDLE_WIDTH
player2_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Draw the game objects
def draw_objects():
    window.fill(BLACK)
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.rect(window, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Update the game objects
def update_objects():
    global ball_x, ball_y, ball_dx, ball_dy, player1_y, player2_y

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Collision detection with paddles and boundaries
    if ball_x < BALL_RADIUS + PADDLE_WIDTH and player1_y < ball_y < player1_y + PADDLE_HEIGHT:
        ball_dx = abs(ball_dx)
    elif ball_x < BALL_RADIUS + PADDLE_WIDTH:
        print("Player 2 wins!")
        pygame.quit()
        quit()
    if ball_x > WINDOW_WIDTH - BALL_RADIUS - PADDLE_WIDTH and player2_y < ball_y < player2_y + PADDLE_HEIGHT:
        ball_dx = -abs(ball_dx)
    elif ball_x > WINDOW_WIDTH - BALL_RADIUS - PADDLE_WIDTH:
        print("Player 1 wins!")
        pygame.quit()
        quit()
    if ball_y < BALL_RADIUS or ball_y > WINDOW_HEIGHT - BALL_RADIUS:
        ball_dy = -ball_dy

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 5
    if keys[pygame.K_s] and player1_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        player1_y += 5
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        player2_y += 5

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw and update the game objects
    draw_objects()
    update_objects()

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)
