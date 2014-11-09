import yaml
import random
config=yaml.load(open("config.yml")) 



number_of_boids=config['number_of_boids']
boids_starting_x_position_range= config['boids_starting_x_position_range']
boids_starting_y_position_range= config['boids_starting_y_position_range']
boids_starting_x_velocity_range=config['boids_starting_x_velocity_range']
boids_starting_y_velocity_range=config['boids_starting_y_velocity_range']

class boid(object):
	def __init__(self):
	   self.xposition=xposition
	   self.yposition=yposition
	   self.xvelocity=xvelocity
	   self.yvelocity=yvelocity

   
class boids(object):
   def __init__(self):

      self.boids=[boid() for i in range(number_of_boids)] 
      for i in self.boids:
         i.boid.self.xposition=random.uniform(*boids_starting_x_position_range)
         i.boid.self.yposition=random.uniform(*boids_starting_y_position_range)
         i.boid.self.xvelocity=random.uniform(*boids_starting_x_velocity_range)
         i.boid.self.yvelocity=random.uniform(*boids_starting_y_position_range)
   
   def velocity_change(self,threshold):
	   for boid in self.boids:
		for j in self.boids:
	            i.boid.xvelocity=i.boid.xvelocity+(j.boid.xposition-i.boid.xposition)*threshold
                    i.boid.yvelocity=i.boid.yvelocity+(j.boid.yposition-i.boid.yposition)*threshold
 
"""  
   def position_difference_test(self,threshold)
      if (position_x2-position_x1)**2 + (position_y2-position_y1)**2 < threshold:
      return True
""" 

"""
   
random.uniform(*boids_starting_x_position_range),random.uniform(*boids_starting_y_position_range),random.uniform(*boids_starting_x_velocity_range),random.uniform(*boids_starting_y_position_range)
   def velocity_change(self,threshold):
	   for i in self.boids:
		for j in self.boids:
	            i.boid.xvelocity=i.boid.xvelocity+(j.boid.xposition-i.boid.xposition)*threshold
                    i.boid.yvelocity=i.boid.yvelocity+(j.boid.yposition-i.boid.yposition)*threshold

   def position_difference_test(self,threshold)
      if (position_x2-position_x1)**2 + (position_y2-position_y1)**2 < threshold:
      return True


	   

"""


