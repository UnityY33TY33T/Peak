import pygame
import random
pygame.init()

# Sound/music
pygame.mixer.init()

# size of the playing screen
screen_width = 1250
screen_height = 840
screen = pygame.display.set_mode((screen_width, screen_height))

# Window name
pygame.display.set_caption("Peak: Rise Up")

# speed
vel = 3.2

# Player Sprites
walkRight = [pygame.image.load('ER0.png'), pygame.image.load('ER1.png'), pygame.image.load('ER2.png'),
             pygame.image.load('ER3.png'), pygame.image.load('ER4.png'), pygame.image.load('ER5.png'),
             pygame.image.load('ER6.png'), pygame.image.load('ER7.png'), pygame.image.load('ER8.png')]
walkLeft = [pygame.image.load('EL0.png'), pygame.image.load('EL1.png'), pygame.image.load('EL2.png'),
            pygame.image.load('EL3.png'), pygame.image.load('EL4.png'), pygame.image.load('EL5.png'),
            pygame.image.load('EL6.png'), pygame.image.load('EL7.png'), pygame.image.load('EL8.png')]
walkStill = [pygame.image.load('S0.png'), pygame.image.load('S1.png')]

# Background
bg = pygame.image.load('Background.jpg')

# Clock
clock = pygame.time.Clock()

# Player
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 39, self.y + 39, self.width - 12, self.height - 13)


    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 39, self.y + 39, self.width - 12, self.height - 13)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 3)

# Enemy
class Enemy(object):
    walkRight = [pygame.image.load('R0.png'), pygame.image.load('R1.png'), pygame.image.load('R2.png'),
                 pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'),
                 pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
    walkLeft = [pygame.image.load('L0.png'), pygame.image.load('L1.png'), pygame.image.load('L2.png'),
                pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'),
                pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 10
        self.path = [self.x, self.end]
        self.hitbox = (self.x, self.y, self.width - 20, self.height - 20)
        self.isJump = False
        self.jumpCount = 10

    def draw(self, screen):
        self.move()
        if self.walkCount + 1 >= 18:
            self.walkCount = 0

        if self.vel > 0:
            screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x, self.y, self.width - 20, self.height - 20)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 3)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0



    def hit(self):
        if not self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.25 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
                self.y = 600
        print(self.y)


# Bullets
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 50 * facing

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    screen.blit(bg, (0, 0))
    man.draw(screen)
    green.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.update()


# mainloop
man = Player(625, 550, 64, 64)
green = Enemy(100, 600, 64, 64, 1180)
bullets = []
shootLoop = 0

run = True
while run:
    clock.tick(35)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    for bullet in bullets:
        if bullet.y - bullet.radius < green.hitbox[1] + green.hitbox[3] and bullet.y + bullet.radius > green.hitbox[1]:
            if bullet.x + bullet.radius > green.hitbox[0] and bullet.x - bullet.radius < green.hitbox[0] + green.hitbox[2]:
                green.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 1:
            bullets.append(projectile(round(man.x + 32 + man.width // 2), round(man.y + 22 + man.height // 2), 6, (0, 255, 0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.25 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()

# if keys[pygame.K_UP] and y > vel:
#     y -= vel
#
# if keys[pygame.K_DOWN] and y < screen_height - height - vel:
#     y += vel
