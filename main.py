# Soccer game
# Have 2 players and score by kicking the ball into certain areas


import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1280
HEIGHT = 720
TITLE = "Soccer Madness"


class Ground(pygame.sprite.Sprite):
    """Represents the ground for the game"""
    def __init__(self):
        # Call in constructor for ground
        super().__init__()

        self.width, self.height = (WIDTH, 10)
        self.rect.x, self.rect.y = (WIDTH/2, 0)



class Player(pygame.sprite.Sprite):
    """This Class represents the class"""

    def __init__(self):
        # Call the player constructor
        super().__init__()

        self.jump_count = 0

        # Load player picture
        self.image = pygame.image.load("mario.png")
        self.image = pygame.transform.scale(self.image, (64, 64))

        # Get hit box
        self.rect = self.image.get_rect()

        #set speed for the player
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """For player movement"""

        # caculating gravity
        self.calc_grav()

        # Player jumps
        ground_hit_list = pygame.sprite.spritecollide(self, ground_sprites)

        self.rect.y += 2





class Player2:
    pass


class goal:
    pass


class ball:
    pass


def main():
    pygame.init()

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



    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
