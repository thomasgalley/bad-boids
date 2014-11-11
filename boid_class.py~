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
        





class boids(object):
 
       def __init__(self,attraction_strength,boidproximitythreshold,matchspeed_distance,matchspeed_strength,number_of_boids):
          self.attraction_strength=attraction_strength
          self.boidproximitythreshold=boidproximitythreshold
          self.matchspeed_distance=matchspeed_distance
          self.matchspeed_strength=matchspeed_strength
          self.boids= [boid(0,0,0,0)]*number_of_boids

       def initial_flock(self,number_of_boids):
           
           self.boids=[boid(0,0,0,0).random_boid() for i in range (number_of_boids)]

       def fly_to_centre(self,number_of_boids):
           for boid in self.boids:
             for member in self.boids:
                boid.xvelocity=velocity_change(boid.xvelocity,boid.xposition,member.xposition,self.attraction_strength/number_of_boids)
                boid.yvelocity=velocity_change(boid.yvelocity,boid.yposition,member.yposition,self.attraction_strength/number_of_boids)

       def fly_away_from_boids(self,number_of_boids):
        for boid in self.boids:
           for member in self.boids:
                        if position_difference_test(boid.xposition,member.xposition,boid.yposition,member.yposition,self.boidproximitythreshold):
				boid.xvelocity=velocity_change(boid.xvelocity,boid.xposition,member.xposition,1)
				boid.yvelocity=velocity_change(boid.yvelocity,boid.yposition,member.yposition,1)







            
      

   
           
           



