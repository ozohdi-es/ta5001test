# Example file showing a circle moving on screen
import pygame
import random

WIDTH = 1280
HEIGHT= 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0 #delta Time

class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x,y)

    def draw (self, screen):
        top = pygame.Vector2(self.position.x,self.position.y)
        right = pygame.Vector2(self.position.x+30, self.position.y+30)
        left = pygame.Vector2(self.position.x-30, self.position.y+30)
        pygame.draw.polygon(screen, "black", [top, left, right],  2)
    

def create_boids(total_num_boids):
    
    #boids_list = []
    #for newBoid in range(total_num_boids):
    #    newBoid = Boid(random.uniform(0,WIDTH), random.uniform(0, HEIGHT))
    #    boids_list.append(newBoid)

    boids_list = [Boid(random.uniform(0,WIDTH), random.uniform(0, HEIGHT)) for _ in range(total_num_boids)]
    return boids_list

    

def main():

    boids = create_boids(100)
    running = True
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("fuchsia")

        for boid in boids:
            boid.draw(screen)


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    main() 