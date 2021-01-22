# Soccer game
# Have 2 players and score by kicking the ball into certain areas


import pygame
from random import randint
from ball import Ball

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1280
HEIGHT = 720
TITLE = "Soccer Madness"

'''class Ground(pygame.sprite.Sprite):
    """Represents the ground for the game"""

    def __init__(self):
        # Call in constructor for ground
        super().__init__()

        self.width, self.height = (WIDTH, 10)
        self.rect.x, self.rect.y = (WIDTH / 2, 0)'''


class Player(pygame.sprite.Sprite):
    """This Class represents the player controlled image"""

    def __init__(self):
        # Call the player constructor
        super().__init__()

        self.jump_count = 0

        # Load player picture
        rmario = pygame.image.load("mario.png")
        rmario = pygame.transform.scale(rmario, (64, 64))
        self.image = rmario

        # Get hit box
        self.rect = self.image.get_rect()

        # set speed for the player
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        """For player movement"""

        # caculating gravity
        self.calc_grav()

        # Moving the player to left or right
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        rmario = pygame.image.load("mario.png")
        rmario = pygame.transform.scale(rmario, (64, 64))
        self.image = rmario
        lmario = pygame.transform.flip(rmario, True, False)
        rjump = pygame.image.load("unnamed.png")
        rjump = pygame.transform.scale(rjump, (64, 64))
        ljump = pygame.transform.flip(rjump, True, False)

        if self.rect.bottom <= HEIGHT and self.vel_x > 0:
            self.image = rjump
        elif self.rect.bottom <= HEIGHT and self.vel_x < 0:
            self.image = ljump

        if self.vel_x < 0 and self.rect.bottom == HEIGHT:
            self.image = lmario
        elif self.vel_x > 0 and self.rect.bottom == HEIGHT:
            self.image = rmario
        elif self.vel_x == 0 and self.rect.bottom == HEIGHT:
            self.image = lmario

    def calc_grav(self):
        """For calculating the effects of gravity"""

        if self.vel_y == 0:
            self.vel_y = 1
        else:

            self.vel_y += .35

        # See if we are on the ground.
        if self.rect.y >= HEIGHT - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self):
        """Defining jump"""

        # If it's ok to jump, set up speed to go upwards
        if self.rect.bottom >= HEIGHT:
            self.vel_y = -10

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0


class Player2:
    pass


class goal:
    pass


def main():
    pygame.init()

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 195

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    ground_sprites = pygame.sprite.Group()

    # adding player to all sprite group
    player = Player()
    all_sprites.add(player)
    ball = Ball()
    all_sprites.add(ball)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.vel_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.vel_x > 0:
                    player.stop()

        # ----- LOGIC
        all_sprites.update()

        if ball.rect.x >= 690:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
