import yaml
import random
config=yaml.load(open("config.yml")) 



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
           

            

   
           
           



