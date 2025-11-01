import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroidfield = AsteroidField()
    Shot.containers = (shots_group, updatable_group, drawable_group)
    
    # Game Loop
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable_group:
            obj.draw(screen)
        updatable_group.update(dt)
        pygame.display.flip()
        
        for asteroid in asteroids_group:
            if asteroid.collision_check(player):
                print("Game Over!")
                sys.exit()
        
        for asteroid in asteroids_group:
            for shot in shots_group:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
        
        


if __name__ == "__main__":
    main()
