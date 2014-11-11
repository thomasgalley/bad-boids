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
            return boid(random.uniform(*boids_starting_x_position_range),random.uniform(*boids_starting_y_position_range),random.uniform(*boids_starting_x_velocity_range),random.uniform(*boids_starting_y_velocity_range))
        





class boids(object):
 
       def __init__(self,attraction_strength,boidproximitythreshold,matchspeed_distance,matchspeed_strength,number_of_boids):
          self.attraction_strength=attraction_strength
          self.boidproximitythreshold=boidproximitythreshold
          self.matchspeed_distance=matchspeed_distance
          self.matchspeed_strength=matchspeed_strength
          self.number_of_boids=number_of_boids
          self.boids= [boid(0,0,0,0)]*number_of_boids

       def initial_flock(self):
           
           self.boids=[boid(0,0,0,0).random_boid() for i in range (self.number_of_boids)]

       def fly_to_centre(self):
           for boid in self.boids:
             for member in self.boids:
                boid.xvelocity=velocity_change(boid.xvelocity,boid.xposition,member.xposition,self.attraction_strength/self.number_of_boids)
                boid.yvelocity=velocity_change(boid.yvelocity,boid.yposition,member.yposition,self.attraction_strength/self.number_of_boids)

       def fly_away_from_boids(self):
        for boid in self.boids:
           for member in self.boids:
                        if position_difference_test(boid.xposition,member.xposition,boid.yposition,member.yposition,self.boidproximitythreshold):
				boid.xvelocity=velocity_change(boid.xvelocity,boid.xposition,member.xposition,1)
				boid.yvelocity=velocity_change(boid.yvelocity,boid.yposition,member.yposition,1)

       def match_speed(self):
          for boid in self.boids:
             for member in self.boids:
	         if position_difference_test(boid.xposition,member.xposition,boid.yposition,member.yposition,self.matchspeed_distance):
	              boid.xvelocity=velocity_change(boid.xvelocity,boid.xposition,member.xposition,self.matchspeed_strength/self.number_of_boids)
		      boid.yvelocity=velocity_change(boid.yvelocity,boid.yposition,member.yposition,self.matchspeed_strength/self.number_of_boids)


       def move_boids(self):
           for boid in self.boids:
		boid.xposition=change_in_position(boid.xposition,boid.xvelocity)
		boid.yposition=change_in_position(boid.yposition,boid.yvelocity)

       def update_boids(self):
	       
        
          self.fly_to_centre()
	
          self.fly_away_from_boids()

          self.match_speed()
	 
          self.move_boids()










            
      

   
           
           



