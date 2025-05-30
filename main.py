import pygame
from constants import *
from players import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot
import sys
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  

    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()
        

        screen.fill((0, 0, 0))
        
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    

    


if __name__ == "__main__":
    main()