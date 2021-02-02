# Soccer game
# Have 2 players and score by kicking the ball into certain areas


import pygame
import ball as Ball

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1280
HEIGHT = 720
TITLE = "Soccer Madness"
background_image = pygame.image.load("1337873.jpg")
background_image = pygame.transform.scale(background_image, (1280, 720))

'''class Ground(pygame.sprite.Sprite):
    """Represents the ground for the game"""

    def __init__(self):
        # Call in constructor for ground
        super().__init__()

        self.width, self.height = (WIDTH, 10)
        self.rect.x, self.rect.y = (WIDTH / 2, 0)'''


class Net(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Net, self).__init__()

        self.image = pygame.image.load("soccer.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (130, 212))


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


class Player2(pygame.sprite.Sprite):

    def __init__(self):
        # Call the player constructor
        super().__init__()

        self.jump_count = 0

        # Load player picture
        rluigi = pygame.image.load("luigi.png")
        rluigi = pygame.transform.scale(rluigi, (64, 64))
        self.image = rluigi

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

        rluigi = pygame.image.load("luigi.png")
        rluigi = pygame.transform.scale(rluigi, (64, 64))
        self.image = rluigi
        lluigi = pygame.transform.flip(rluigi, True, False)
        rljump = pygame.image.load("luijump.png")
        rljump = pygame.transform.scale(rljump, (80, 80))
        lljump = pygame.transform.flip(rljump, True, False)

        if self.rect.bottom <= HEIGHT and self.vel_x > 0:
            self.image = rljump
        elif self.rect.bottom <= HEIGHT and self.vel_x < 0:
            self.image = lljump

        if self.vel_x < 0 and self.rect.bottom == HEIGHT:
            self.image = rluigi
        elif self.vel_x > 0 and self.rect.bottom == HEIGHT:
            self.image = rluigi
        elif self.vel_x == 0 and self.rect.bottom == HEIGHT:
            self.image = lluigi

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
            self.vel_y = -12

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0


class Ball(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        # Import the ball picture
        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        # set initial speed for ball
        self.y_vel = 10
        self.x_vel = 0

    def update(self):

        # ball physics
        # set initial frictions and dampening for speed
        self.calc_gravity()
        friction = 0.3
        dampening = 0.88

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # set it so every time the ball bounces it does it less everytime

        if self.rect.bottomright[1] >= HEIGHT:
            self.y_vel *= -dampening

        if self.rect.topleft[1] <= 1:
            self.y_vel *= -1

        # set friction for when the balls bounce side ways

        if self.rect.bottomright[0] >= WIDTH:
            self.x_vel = -(self.x_vel * friction)
        if self.rect.topleft[0] <= 1:
            self.x_vel = -(self.x_vel * friction)

    def calc_gravity(self):
        if self.y_vel == 0:
            self.y_vel = 1
        else:
            self.y_vel += 0.35

    # detect collsions with player

    def collsion(self, player):
        return self.rect.colliderect(player.rect)

    # detect collsions with net

    def collsion2(self, net):
        return self.rect.colliderect(net.rect)


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

    # Making the ball into it's own group
    ball_sprites = pygame.sprite.Group()

    # Player group
    player_sprites = pygame.sprite.Group()

    # Net Group
    net_sprites = pygame.sprite.Group()

    # adding player to all sprite group

    ball = Ball()
    ball.rect.x = WIDTH / 2
    all_sprites.add(ball)
    ball_sprites.add(ball)
    net = Net()

    # adding the nets to the groups
    net1 = Net()
    net2 = Net()

    # net positions
    net1.rect.x = 0
    net1.rect.y = 525

    net2.image = pygame.transform.flip(net2.image, True, False)
    net2.rect.x = 1150
    net2.rect.y = 525

    # add the net to the groups

    net_sprites.add(net1)
    all_sprites.add(net1)

    net_sprites.add(net2)
    all_sprites.add(net2)

    # Player 1
    player = Player()
    all_sprites.add(player)

    player.rect.x = 125
    player.rect.y = 600

    # Player 2

    player2 = Player2()
    all_sprites.add(player2)

    player2.rect.x = 1100
    player2.rect.y = 600

    #

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player2.go_left()
                if event.key == pygame.K_d:
                    player2.go_right()
                if event.key == pygame.K_w:
                    player2.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player2.vel_x < 0:
                    player2.stop()
                if event.key == pygame.K_d and player2.vel_x > 0:
                    player2.stop()

        # ----- LOGIC
        all_sprites.update()

        c_tol = 90
        if ball.collsion(player):
            print('collision!')

            if abs(player.rect.top - ball.rect.bottom) < c_tol:
                ball.rect.bottom = player.rect.top
                ball.y_vel *= -1.0
            if abs(player.rect.bottom - ball.rect.top) < c_tol:
                ball.rect.top = player.rect.bottom
                ball.y_vel *= -1.0
                ball.y_vel -= 0.5
            if abs(player.rect.right - ball.rect.left) < c_tol:
                ball.rect.left = player.rect.right
                ball.x_vel *= -1.0
                ball.x_vel += 10
            if abs(player.rect.left - ball.rect.right) < c_tol:
                ball.rect.right = player.rect.left
                ball.x_vel *= -1.0
                ball.x_vel -= 10

        if ball.collsion(player2):
            print('collision!')

            if abs(player2.rect.top - ball.rect.bottom) < c_tol:
                ball.rect.bottom = player2.rect.top
                ball.y_vel *= -1.0
            if abs(player2.rect.bottom - ball.rect.top) < c_tol:
                ball.rect.top = player2.rect.bottom
                ball.y_vel *= -1.0
                ball.y_vel -= 0.5
            if abs(player2.rect.right - ball.rect.left) < c_tol:
                ball.rect.left = player2.rect.right
                ball.x_vel *= -1.0
                ball.x_vel += 10
            if abs(player2.rect.left - ball.rect.right) < c_tol:
                ball.rect.right = player2.rect.left
                ball.x_vel *= -1.0
                ball.x_vel -= 10

        if ball.collsion(net1):
            print('collision!')

            if abs(net1.rect.top - ball.rect.bottom) < c_tol:
                ball.rect.bottom = net1.rect.top
                ball.y_vel *= -1.0

        if ball.collsion(net2):
            print('collision!')

            if abs(net2.rect.top - ball.rect.bottom) < c_tol:
                ball.rect.bottom = net2.rect.top
                ball.y_vel *= -1.0

        if ball.collsion(net1):
            print('Player 2 Wins!')

        if ball.collsion(net2):
            print('Player 1 Wins!')

        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
