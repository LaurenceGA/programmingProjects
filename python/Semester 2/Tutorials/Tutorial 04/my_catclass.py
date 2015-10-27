import pygame
import random

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)


class caterpillar:
    def __init__(self):
        x = random.randrange(0, 960)
        self.face_xcoord = x
        self.face_ycoord = 250
        self.body = segment_queue()
        self.food = food_list()

        # Growing the caterpillar may mess up with stat
        self.wellbeing = 0      # How the caterpillar is feeling

        td = random.randrange(0, 2)
        if td == 0:
            self.travel_direction = 'left'
        else:
            self.travel_direction = 'right'
           
    def grow(self):
        """
        td is a modifier used to modify the calculation
        td = 0 for left and td = 1 for right
        """
        td = 0 if self.travel_direction == 'left' else 1

        if self.body.length == 0:
            # 35 only taken away if traveling right, 40 added only if traveling left
            xpos = self.face_xcoord - 35*td - (td-1)*40
        else:
            # 35 * body length (plus initial segment) only if traveling right
            # 40 + 35 * body length only added if traveling right
            xpos = self.face_xcoord - (35*(self.body.length+1)*td) - (td-1)*(40 + 35*self.body.length)

        self.body.addSegment(xpos, self.face_ycoord)

    def reverse(self):
        # Reverse travel direction
        td = 1 if self.travel_direction == 'left' else -1
        # Swap left/right
        self.travel_direction = 'left' if self.travel_direction == 'right' else 'right'

        # Reverse body
        self.body.reverse_queue()

        # Put head where it needs to be
        self.face_xcoord += td * (40 + self.body.length*35)
    
    def move_forward(self):
        if self.body.isEmpty():
            return

        # To reduce calculation repetitions
        td = -1 if self.travel_direction == 'left' else 1

        if 0 <= self.face_xcoord <= 960:    # 1000 (screen width) - 40 (face width)
            self.face_xcoord += 2*td    # + or - depending on direction

            # Traverse body and add to xcoord
            cur_seg = self.body.head
            while cur_seg is not None:
                cur_seg.xcoord += 2*td
                cur_seg = cur_seg.next

            # Eat food
            # Traverse list
            # td = 0 if td == -1 else -1
            current_food = self.food.head
            previous_food = None
            while current_food is not None:
                if abs(current_food.xcoord - self.face_xcoord - 12) <= 5:  # -12 so food eaten under caterpillar's mouth
                    # Eat the food
                    if current_food.foodtype == 'nice':
                        self.wellbeing += 1
                        self.grow()
                    else:
                        self.wellbeing -= 1
                        self.shrink_back()

                    # Remove the food item
                    if previous_food is not None:
                        previous_food.next = current_food.next
                    else:
                        self.food.head = self.food.head.next

                    self.food.length -= 1

                previous_food = current_food
                current_food = current_food.next
        else:
            self.reverse()

    def shrink_back(self):

        td = -1 if self.travel_direction == 'left' else 1

        self.body.remove_first()
        self.face_xcoord -= 35*td

    def drop_food(self):
        # Should be done with random.choice, but done as brief said to instead
        if random.randrange(0, 2) == 0:
            food_type = 'nice'
        else:
            food_type = 'nasty'

        self.food.addItem(random.randrange(0, 980), self.face_ycoord + 35, food_type)
        
    def draw_caterpillar(self, screen):
        self.draw_face(screen)
        self.draw_body(screen)
        self.draw_food(screen)

    def draw_face(self, screen):
        x = self.face_xcoord 
        y = self.face_ycoord
        pygame.draw.ellipse(screen, red, [x, y, 40, 45])
        pygame.draw.ellipse(screen, black, [x+6, y+10, 10, 15])
        pygame.draw.ellipse(screen, black, [x+24, y+10, 10, 15])
        pygame.draw.line(screen, black, (x+11, y), (x+9, y-10), 3)
        pygame.draw.line(screen, black, (x+24, y), (x+26, y-10), 3)
        
    def draw_body(self, screen):
        # Traverse the segment queue
        current_node = self.body.head
        if self.wellbeing > 1:
            colour = yellow
        elif self.wellbeing < -1:
            colour = purple
        else:
            colour = green

        i = 0
        while current_node is not None:
            if colour in (purple, black):
                colour = black if i % 2 == 0 else purple
            current_node.draw_segment(screen, colour)
            current_node = current_node.next
            i += 1
           
    def draw_food(self, screen):
        # Traverse the segment queue
        current_node = self.food.head
        while current_node is not None:
            current_node.draw_fooditem(screen) 
            current_node = current_node.next 


class segment_queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.length == 0
      
    def addSegment(self, x, y): 
        segment = body_segment(x, y)    # Create our new segment

        # If the list is empty the new one becomes the first and last
        if self.length == 0:
            self.head = self.last = segment
        else:
            # Otherwise stick on end
            last = self.last
            last.next = segment
            self.last = segment

        self.length += 1
    
    def reverse_queue(self):
        b = None
        temp = self.head
        while temp is not None:
            a = temp.next
            temp.next = b
            b = temp
            temp = a
        # Clean up
        self.last = self.head
        self.head = b

    def remove_first(self):
        if not self.isEmpty():
            self.head = self.head.next
            self.length -= 1


class body_segment:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.next = None
        
    def draw_segment(self, screen, colour):
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen, colour,[x, y, 35, 40])
        pygame.draw.line(screen, black, (x+8, y+35), (x+8, y+45), 3)
        pygame.draw.line(screen, black, (x+24, y+35), (x+24, y+45), 3)


class food_list:
    def __init__(self):
        self.length = 0
        self.head = None
        
    def addItem(self, x, y, kind): 
        food = food_item(x, y, kind)
        food.next = self.head
        self.head = food
        self.length += 1


class food_item:
    def __init__(self, x, y, kind):
        self.xcoord = x
        self.ycoord = y
        self.foodtype = kind
        self.next = None   
        
    def draw_fooditem(self, screen):
        x = self.xcoord
        y = self.ycoord
        if self.foodtype == 'nice':
            pygame.draw.ellipse(screen,yellow,[x, y, 15, 15])
        else:
            pygame.draw.ellipse(screen,purple,[x, y, 15, 15])

