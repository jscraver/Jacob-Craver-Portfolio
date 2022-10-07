import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define screen and ball dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 2

# Define number of test subjects
PEOPLE = 100

# Make ball lists
ball_list = []
iball_list = []

# Class to define healthy people
class Healthy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.color = GREEN

# Class to define infected people
class Infected:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.color = RED

# Function to create healthy people
def make_healthy():
    ball = Healthy()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of rectangle
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
 
    return ball

# Function to create infected people
def make_infected():
    iball = Infected()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    iball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    iball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of ball
    iball.change_x = random.randrange(-2, 3)
    iball.change_y = random.randrange(-2, 3)
 
    return iball

# Function to check if a healthy person is close enough to an infected person to become infected
def proximity_check():
    for iball in iball_list:
        for ball in ball_list:
            if iball.x-5 <= ball.x <= iball.x+5:
                if iball.y-5 <= ball.y <= iball.y+5:
                    iball = Infected()
                    iball.x = ball.x
                    iball.y = ball.y
                    iball.change_x = ball.change_x
                    iball.change_y = ball.change_y
                    iball_list.append(iball)
                    ball_list.remove(ball)
                    
def main():
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Simulitis")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Create healthy people
    for i in range(PEOPLE-1):
        ball = make_healthy()
        ball_list.append(ball)
        
    # Create an infected person
    iball = make_infected()
    iball_list.append(iball)
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! End simulation and generate statistics.
                if event.key == pygame.K_SPACE:
                    done = True
 
        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
                
        for iball in iball_list:
            # Move the ball's center
            iball.x += iball.change_x
            iball.y += iball.change_y
 
            # Bounce the ball if needed
            if iball.y > SCREEN_HEIGHT - BALL_SIZE or iball.y < BALL_SIZE:
                iball.change_y *= -1
            if iball.x > SCREEN_WIDTH - BALL_SIZE or iball.x < BALL_SIZE:
                iball.change_x *= -1
                
        # Check if a healthy ball can become infected by an infected ball
        proximity_check()     
                     
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
 
        # Draw the balls
        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)

        for iball in iball_list:
            pygame.draw.circle(screen, iball.color, [iball.x, iball.y], BALL_SIZE)

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()

# Print the number of healthy people and infected people when the simulation ended
print "\nHealthy: {}".format(len(ball_list))
print "Infected: {}".format(len(iball_list))
