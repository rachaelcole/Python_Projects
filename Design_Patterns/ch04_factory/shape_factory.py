# When we want to call a method such that we pass in a stringand get a new object as a return value, we are 
# essentially creating a factory method. The type of object is determined by the string passed to the factory
# method. This helps make code more scalable because you can add functionality to programs by adding a new
# class and extending the factory method to accept a new string and return the class you created.

from logger import Logger
import pygame

class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        raise NotImplementedError()
    
    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        elif direction == 'down':
            self.y += 4
        elif direction == 'left':
            self.x -= 4
        elif direction == 'right':
            self.x += 4
    
    @staticmethod
    def factory(type, x, y):
        if type == "circle":
            return Circle(x, y)
        if type == 'square':
            return Square(x, y)
        assert 0, 'Bad shape requested: ' + type


class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(self.x, self.y, 20, 20))


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), 10)


if __name__ == "__main__":
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)

    obj = Shape.factory('square', 100, 100)
    player_quits = False

    logfile = Logger('logs.txt')

    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True
            
            # Get the key the user presses
            pressed = pygame.key.get_pressed()
            
            # If an arrow key pressed, move the object in that direction:
            if pressed[pygame.K_UP]: obj.move('up')
            if pressed[pygame.K_DOWN]: obj.move('down')
            if pressed[pygame.K_LEFT]: obj.move('left')
            if pressed[pygame.K_RIGHT]: obj.move('right')

            # If 'C' key pressed, change shape to a circle if it is a square:
            if pressed[pygame.K_c]: 
                if type(obj) == Square:
                    x = obj.x
                    y = obj.y
                    logfile.debug(f'Obj coords (x, y): ({x}, {y})')
                    obj = Shape.factory('circle', x, y)
            
            # If 'S' key pressed, change shape to a square if it is a circle:
            if pressed[pygame.K_s]:
                if type(obj) == Circle:
                    x = obj.x
                    y = obj.y
                    logfile.debug(f'Obj coords (x, y): ({x}, {y})')
                    obj = Shape.factory('square', x, y)

            screen.fill((0,0,0))
            obj.draw()
        pygame.display.flip()


# Reference: 
# Badenhurst, Wessel. "Chapter 4: Factory Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 61-73.
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_4. 