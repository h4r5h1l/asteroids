import pygame
from circleshape import CircleShape 
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # overriding parent class method
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
            
            
    def move(self, dt):
        facing = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += facing * PLAYER_SPEED * dt
        
    def shoot(self, dt):
        if self.timer > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        facing = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = facing * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN