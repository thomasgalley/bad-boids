import yaml
import random
config=yaml.load(open("config.yml")) 
from Boid_differences import*
import numpy

number_of_boids=config['number_of_boids']
boids_starting_x_position_range= config['boids_starting_x_position_range']
boids_starting_y_position_range= config['boids_starting_y_position_range']
boids_starting_x_velocity_range=config['boids_starting_x_velocity_range']
boids_starting_y_velocity_range=config['boids_starting_y_velocity_range']

class boid(object):
	def __init__(self,xposition,yposition,xvelocity,yvelocity):
	   self.xposition=xposition
	   self.yposition=yposition
	   self.xvelocity=xvelocity
	   self.yvelocity=yvelocity
       
        def random_boid(self):
            return boid(random.uniform(*boids_starting_x_position_range),random.uniform(*boids_starting_y_position_range),random.uniform(*boids_starting_x_velocity_range),random.uniform(*boids_starting_y_position_range))
        
C=[boid(0,0,0,0).random_boid() for i in range (number_of_boids)]




class boids(object):
 
       def __init__(self,attraction_strength,boidproximitythreshold,matchspeed_distance,matchspeed_strength,number_of_boids):
          self.attraction_strength=attraction_strength
          self.boidproximitythreshold=boidproximitythreshold
          self.matchspeed_distance=matchspeed_distance
          self.matchspeed_strength=matchspeed_strength
          self.boids= [0]*number_of_boids

       def initial_flock(self,number_of_boids):
           
           self.boids=([boid(0,0,0,0).random_boid() for i in range (number_of_boids)])





"""

B=boid(1,2,3,5)
print B.xposition


B=boid(1,2,3,5)
C=B.random_boid()
print C.xposition

B=boid(1,2,3,5).random_boid()

b = boids(1,2,3,4,50)
b.initial_flock(50)
print b.matchspeed_strength



print boid(1,2,3,5).random_boid().xposition

"""



"""  
        def velocity_change_1(self,boid1,magnitude):
            return velocity_change(self.xvelocity,self.xposition,boid1.xposition,magnitude)

        
"""

            
      

   
           
           



