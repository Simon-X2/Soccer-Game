import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "<You're title here>"




class Ball(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()


        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        self.y_vel = 2
        self.x_vel = 0

    def update(self):


        gravity = 0.7
        friction = 0.3

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.bottomright[1] >= HEIGHT:
                self.y_vel *= -1

        if self.rect.topleft[1] <= 1:
                self.y_vel *= -1

        if self.rect.bottomright[0] >= WIDTH:
                self.x_vel = -(self.x_vel * friction)

        if self.rect.topleft[0] <= 1:
                self.x_vel = -(self.x_vel * friction)

        self.y_vel += gravity








def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    ball = Ball()
    all_sprites.add(ball)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)


        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
