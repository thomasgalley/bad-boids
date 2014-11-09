import yaml
import random
config=yaml.load(open("config.yml")) 

# Deliberately terrible code for teaching purposes

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
"""
           
boids=[boid(random.uniform(*boids_starting_x_position_range),random.uniform(*boids_starting_y_position_range),random.uniform(*boids_starting_x_velocity_range),random.uniform(*boids_starting_y_position_range)) for i in range(number_of_boids)]   

for boid in boids:
   print boid.xvelocity  

"""

class boids(object):
   def __init__(self,number_of_boids):
      self.number_of_boids=number_of_boids
      self.boids=[boid(random.uniform(*boids_starting_x_position_range),random.uniform(*boids_starting_y_position_range),random.uniform(*boids_starting_x_velocity_range),random.uniform(*boids_starting_y_position_range)) for i in range(number_of_boids)] 
   
   def velocity_change(self,threshold):
	   for i in self.boids:
		for j in self.boids:
	            i.boid.xvelocity=i.boid.xvelocity+(j.boid.xposition-i.boid.xposition)*threshold
	   return boid.xvelocity
"""
class boids(object):
   def __init__(self,number_of_boids):
      self.number_of_boids=number_of_boids
      boids=[boid(random.uniform(*boids_starting_x_position_range),random.uniform(*boids_starting_y_position_range),random.uniform(*boids_starting_x_velocity_range),random.uniform(*boids_starting_y_position_range)) for i in range(self.number_of_boids)]   
	   
   def velocity_change(self,threshold):
	   for i in self.boids:
		for j in self.boids:
	            i.boid.xvelocity=i.boid.xvelocity+(j.boid.xposition-i.boid.xposition)*threshold
	   return boid.xvelocity
		

		



print boid.xvelocity



# boid in boids:
  # print boid.velocity_change(0.01*number_of_boids)

""" 

