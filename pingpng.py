import pygame

# Initialize the game
pygame.init()

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

# Function to draw the game objects
def draw_objects():
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 255, 255), (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.rect(window, (255, 255, 255), (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, (255, 255, 255), (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Function to update the game objects
def update_objects():
    global ball_x, ball_y, ball_dx, ball_dy, player1_y, player2_y
    ball_x += ball_dx
    ball_y += ball_dy
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 5
    if keys[pygame.K_s] and player1_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        player1_y += 5
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        player2_y += 5

# Main game loop
clock = pygame.time.Clock()
while True:
    draw_objects()
    update_objects()
    pygame.display.update()
    clock.tick(60)
