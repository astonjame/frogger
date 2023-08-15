import froggerlib
import pygame

LANESIZE = 50
OBJECT_HEIGHT = 40
OBJECT_WIDTH = 40
HALFGAP = 5
STAGE1 = 10
ROAD1 = 9
ROAD2 = 8
ROAD3 = 7
ROAD4 = 6
STAGE2 = 5
RIVER1 = 4
RIVER2 = 3
RIVER3 = 2
RIVER4 = 1
GOAL = 0



class Frogger:
    def __init__( self, width, height ):
        self.width = width
        self.height = height
        self.gameover = False
        self.win = False
        
        # x, y, w, h, dx, dy, s, hg, vg
        self.frog = froggerlib.Frog(width/2 - 20,
                                    STAGE1*LANESIZE+HALFGAP,
                                    OBJECT_WIDTH,
                                    OBJECT_HEIGHT,
                                    width/2 - 20,
                                    STAGE1*LANESIZE+HALFGAP,
                                    40,
                                    LANESIZE,
                                    LANESIZE)
        self.stage1 = froggerlib.Stage(0, STAGE1*LANESIZE, width, LANESIZE)
        self.stage2 = froggerlib.Stage(0, STAGE2*LANESIZE, width, LANESIZE)
        
        # create four road objects and append them to the list
        self.roads = []
        for i in range(4):
            road = froggerlib.Road(0, ROAD1*LANESIZE - i*LANESIZE, width, LANESIZE)
            self.roads.append(road)
            
        self.waters = []
        for i in range(4):
            water = froggerlib.Water(0, RIVER1*LANESIZE - i*LANESIZE, width, LANESIZE)
            self.waters.append(water)
            
            
        self.grasses = []
        for i in range(5):
            x = (width/5) * i
            y = GOAL*LANESIZE
            w = 80
            h = LANESIZE
            grass = froggerlib.Grass(x, y, w, h)
            self.grasses.append(grass)
            
        self.homes = []
        for i in range(5):
            x = (width/5) * i
            y = GOAL*LANESIZE
            w = 800
            h = LANESIZE
            home = froggerlib.Home(x, y, w, 60)
            self.homes.append(home)
            
        
        
        # create 2 cars going right
        self.right_cars = []
        for i in range(2):
            # x=0, y=0, w=0, h=0, dx=0, dy=0, s=0
            x = width/2 * i
            y = ROAD1*LANESIZE + HALFGAP
            w = 50
            h = OBJECT_HEIGHT
            
            car = froggerlib.Car(x, y, w, h, width, y, 10)
            self.right_cars.append(car)
            
        
        # create 3 trucks going left
        self.left_trucks = []
        for i in range(3):
            x = width/3 * i
            y = ROAD4*LANESIZE + HALFGAP
            w = 80
            h = OBJECT_HEIGHT
            truck = froggerlib.Truck(x, y, w, h, -w, y, 10)
            self.left_trucks.append(truck)
        # create 2 race cars going right
        self.right_racecar = []
        for i in range(1):
            x = width * i
            y = ROAD3*LANESIZE + HALFGAP
            w = 40
            h = OBJECT_HEIGHT
            race = froggerlib.Truck(x, y, w, h, width, y, 20)
            self.right_racecar.append(race)
            
        self.left_dozer = []
        for i in range(2):
            x = width/2 * i
            y = ROAD2*LANESIZE + HALFGAP
            w = 100
            h = OBJECT_HEIGHT
            dozer = froggerlib.Dozer(x, y, w, h, -w, y, 5)
            self.left_dozer.append(dozer)
        
#

        self.left_alligator = []
        for i in range(4):
            x = width/4 * i
            y = RIVER1*LANESIZE + HALFGAP
            w = 90
            h = OBJECT_HEIGHT
            alligator = froggerlib.Alligator(x, y, w, h, -w, y, 5)
            self.left_alligator.append(alligator)
        
        self.right_turtle = []
        for i in range(6):
            # x=0, y=0, w=0, h=0, dx=0, dy=0, s=0
            x = width/6 * i
            y = RIVER2*LANESIZE + HALFGAP
            w = 50
            h = OBJECT_HEIGHT
            
            turtle = froggerlib.Turtle(x, y, w, h, width, y, 7)
            self.right_turtle.append(turtle)
        
                   
            
        self.left_log = []
        for i in range(3):
            # x=0, y=0, w=0, h=0, dx=0, dy=0, s=0
            x = width/2 * i
            y = RIVER3*LANESIZE + HALFGAP
            w = 120
            h = OBJECT_HEIGHT
            
            log = froggerlib.Log(x, y, w, h, -w, y, 7)
            self.left_log.append(log)
            
        self.right_alligator = []
        for i in range(4):
            x = width/4 * i
            y = RIVER4*LANESIZE + HALFGAP
            w = 80
            h = OBJECT_HEIGHT
            alligator = froggerlib.Alligator(x, y, w, h, width, y, 5)
            self.right_alligator.append(alligator)
        
        
    def evolve( self, dt ): 
        if self.gameover: #(first check that you do each frame)
            return
        
        for car in self.right_cars:
            car.move()
            if car.atDesiredLocation():
                car.setX(-car.getWidth())
            if car.hits(self.frog):
                self.gameover = True
                
        for truck in self.left_trucks:
            truck.move()
            if truck.atDesiredLocation():
                truck.setX(self.width+truck.getWidth())
            if truck.hits(self.frog):
                self.gameover = True
                
        for dozer in self.left_dozer:
            dozer.move()
            if dozer.atDesiredLocation():
                dozer.setX(self.width+truck.getWidth())
            if dozer.hits(self.frog):
                self.gameover = True
                
        for race in self.right_racecar:
            race.move()
            if race.atDesiredLocation():
                race.setX(-race.getWidth())
            if race.hits(self.frog):
                self.gameover = True
                
        if self.frog.outOfBounds(800,600):
            self.gameover = True
                
                
# water rideables

        for alligator in self.left_alligator:
            alligator.move()
            if alligator.atDesiredLocation():
                alligator.setX(self.width+truck.getWidth())
            alligator.supports(self.frog)
        
        for log in self.left_log:
            log.move()
            if log.atDesiredLocation():
                log.setX(self.width+truck.getWidth())
            log.supports(self.frog)

        for turtle in self.right_turtle:
            turtle.move()
            if turtle.atDesiredLocation():
                turtle.setX(-race.getWidth())
            turtle.supports(self.frog)
        
        for alligator in self.right_alligator:
            alligator.move()
            if alligator.atDesiredLocation():
                alligator.setX(-race.getWidth())
            alligator.supports(self.frog)
                
        for grass in self.grasses:
            for home in self.homes:
                if not home.overlapWithLocatable(grass) and home.hits(self.frog):
                    self.gameover = True
                    self.win = True
                if grass.hits(self.frog):
                    self.gameover = True
                    self.win = False



        for water in self.waters:
            if water.hits(self.frog):
                self.gameover = True
        
        self.frog.move()
        
    def fancyDraw(self, surface, obj, color):
        rect = pygame.Rect(int(obj.getX()), int(obj.getY()),
                           int(obj.getWidth()), int(obj.getHeight()))
        pygame.draw.rect(surface, color, rect)
        
    def draw( self, surface ):
        surface.fill((0,0,0))

        
        
        self.fancyDraw(surface, self.stage1, (0,200,0))
        self.fancyDraw(surface, self.stage2, (0,200,0))
        
        for road in self.roads:
            self.fancyDraw(surface, road, (69,69,69))

            
        for home in self.homes:
            self.fancyDraw(surface, home, (0, 150, 255))
            
        for grass in self.grasses:
            self.fancyDraw(surface, grass, (0,200,0))

            
        for water in self.waters:
            self.fancyDraw(surface, water, (0, 150, 255))
        
        for car in self.right_cars:
            self.fancyDraw(surface, car, (255,0,0))
            
        for truck in self.left_trucks:
            self.fancyDraw(surface, truck, (25,25,150))
            
        for race in self.right_racecar:
            self.fancyDraw(surface,race,(255,10,10))
            
        for dozer in self.left_dozer:
            self.fancyDraw(surface,dozer,(255, 211, 67))
            
        for alligator in self.left_alligator:
            self.fancyDraw(surface,alligator,(0, 163, 108))
            
        for alligator in self.right_alligator:
            self.fancyDraw(surface,alligator,(0, 163, 108))
            
        for log in self.left_log:
            self.fancyDraw(surface,log,(62, 39, 35 ))
            
        for turtle in self.right_turtle:
            self.fancyDraw(surface,turtle,(27, 94, 32))
            
            
        
        
        
        self.fancyDraw(surface, self.frog, (88, 255, 51))
        if self.gameover:
            if self.win:
                surface.fill((0,255,0))
                font = pygame.font.Font(None, 50)
                text = font.render("You Win!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
                surface.blit(text, text_rect)
            else:
                # Display game over screen (optional)
                surface.fill((255,0,0))
                font = pygame.font.Font(None, 50)
                text = font.render("You Lose :(", True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
                surface.blit(text, text_rect)
        
        return
    
    def act_on_pressUP(self):
        self.frog.up()
        
    def act_on_pressDOWN(self):
        self.frog.down()
        
    def act_on_pressLEFT(self):
        self.frog.left()
        
    def act_on_pressRIGHT(self):
        self.frog.right()
    
