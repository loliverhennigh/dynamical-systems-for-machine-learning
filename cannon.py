
import numpy as np
import random
import math

class Cannon:
    # A little ball trajectory simulation like the old Cannon games.
    # The data it generates can either be in the form of pixel images
    # of size 28x28 (like mnist!) or position of ball as two numbers 
    # between 0 and 1.

    def __init__(self):
        # ball starts at 0.5 and 0.0
        self.x_pos = .0 
        self.y_pos = .5 
        self.x_vel = random.random()
        self.y_vel = 5*random.random() 
        # you can play with this
        self.grav = 4.0
        self.dt = .01 
        self.damp = 0 #probably set this to 0 for most applications

    # very basic physics
    def restart(self):
        self.x_pos = .0 
        self.y_pos = .5 
        self.x_vel = random.random()
        self.y_vel = 5*random.random() 

    # very basic physics
    def update_pos(self):
        self.x_pos = self.x_pos + self.dt * self.x_vel
        self.y_pos = self.y_pos + self.dt * self.y_vel
        self.x_vel = self.x_vel + self.dt * (self.grav - (self.damp * self.x_vel))
        self.y_vel = self.y_vel + self.dt * self.damp * self.x_vel
        #self.y_vel = self.y_vel + self.dt * (self.grav - (self.damp * self.y_vel))
        print('self.x_pos')
        print(self.x_pos)
        print('self.y_pos')
        print(self.y_pos)
        print('self.x_vel')
        print(self.x_vel)
        print('self.y_vel')
        print(self.y_vel)
        print('self.speed()')
        print(self.speed())
        # bounce
        if (0 > self.x_pos):
            self.x_vel = -self.x_vel 
            self.x_pos = 0 
        if (1 < self.x_pos):
            self.x_vel = -self.x_vel 
            self.x_pos = 1 
        if (0 > self.y_pos):
            self.y_vel = -self.y_vel 
            self.y_pos = 0 
        if (1 < self.y_pos):
            self.y_vel = -self.y_vel 
            self.y_pos = 1 
 
    # generate pixell images
    def image_28x28(self):
        # same algorith as seen on
        # https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
        im = np.zeros((28,28))
        radius = 4
        x0 = (self.x_pos * 28) // 1
        y0 = (self.y_pos * 28) // 1
        x = radius  
        y = 0
        decisionOver2 = 1 - x
        while(y <= x):
            im[(x+x0) % 28, (y+y0) % 28] = 1.0
            im[(y+x0) % 28, (x+y0) % 28] = 1.0
            im[(-x+x0) % 28, (y+y0) % 28] = 1.0
            im[(-y+x0) % 28, (x+y0) % 28] = 1.0
            im[(-x+x0) % 28, (-y+y0) % 28] = 1.0
            im[(-y+x0) % 28, (-x+y0) % 28] = 1.0
            im[(x+x0) % 28, (-y+y0) % 28] = 1.0
            im[(y+x0) % 28, (-x+y0) % 28] = 1.0
            y = y + 1
            if (decisionOver2 <=0):
                decisionOver2 = decisionOver2 + 2*y + 1
            else:
                x = x - 1
                decisionOver2 = decisionOver2 + 2*(y-x) + 1
        im = im.reshape(28*28)
        return im 

    def generate_28x28(self, batch_size, num_steps):
        # makes a np array of size batch_size x num_steps
        # this will be what most learing algorithms need
        # from there data
        x = np.zeros([batch_size, num_steps, 28*28])
        y = np.zeros([batch_size, num_steps, 28*28])
        for i in xrange(batch_size):
            self.restart()
            x[i, 0, :] = self.image_28x28()
            for j in xrange(num_steps-1):
                #time.sleep(.5)
                self.update_pos()
                x[i, j + 1, :] = self.image_28x28()
                y[i, j, :] = x[i, j + 1, :] 
            self.update_pos()
            y[i, num_steps-1, :] = self.image_28x28()
        return x, y 

    def speed(self):
        return math.sqrt(self.x_vel ** 2 + self.y_vel ** 2)

if __name__ == "__main__":
    k = Cannon()




