"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy
import yaml
#from Change_in_velocity import velocity_change_x

config=yaml.load(open("config.yml")) 

# Deliberately terrible code for teaching purposes

number_of_boids=config['number_of_boids']
boids_starting_x_position_range= config['boids_starting_x_position_range']
boids_starting_y_position_range= config['boids_starting_y_position_range']
boids_starting_x_velocity_range=config['boids_starting_x_velocity_range']
boids_starting_y_velocity_range=config['boids_starting_y_velocity_range']

boids_initial_x_positions=[random.uniform(*boids_starting_x_position_range) for x in range(number_of_boids)]
boids_initial_y_positions=[random.uniform(*boids_starting_y_position_range) for x in range(number_of_boids)]
boid_initial_x_velocities=[random.uniform(*boids_starting_x_velocity_range) for x in range(number_of_boids)]
boid_initial_y_velocities=[random.uniform(*boids_starting_y_velocity_range) for x in range(number_of_boids)]

boids = numpy.zeros((number_of_boids),dtype=[('xposition','f8'),('yposition','f8'),('xvelocity','f8'),('yvelocity','f8')])

for i in range(number_of_boids):
   boids[i]=(boids_initial_x_positions[i],boids_initial_y_positions[i],boid_initial_x_velocities[i],boid_initial_y_velocities[i])



def velocity_change(velocity1,parameter1,parameter2,change_magnitude):
   velocitynew=velocity1+(parameter2-parameter1)*change_magnitude
   return velocitynew

def position_difference_test(position_x1,position_x2,position_y1,position_y2,threshold):
   if (position_x2-position_x1)**2 + (position_y2-position_y1)**2 < threshold:
      return True

def change_in_position(position,velocity,time_increment=1):
   new_position=position+velocity*time_increment
   return new_position

#def velocity_change_x(boids,change_magnitude):
   for boid['xposition'] in boids['xposition']:
      boids['xvelocity']=boids['xveloctiy']+(boid['xposition']-boids['xposition'])*change_magnitude
   return boids['xvelocity']

#for boid in boids: 
 #  print boids


    

def update_boids(boids):
	#boids['xposition'],boids['yposition'],boids['xvelocity'],boids['yvelocity']=boids
        
        #boids= numpy.array((number_of_boids),dtype=[('xposition','f8'),('yposition','f8'),('xvelocity','f8'),('yvelocity','f8')])
        #for i in range(number_of_boids): 
           #boids[i]=(boid['xposition'],boid['yposition'],boid['xvelocity'],boid['yvelocity'])
        # Fly towards the middle
        
        

        for boid in boids:
           for j in range(number_of_boids):
              #boid['xvelocity']=velocity_change(boid['xvelocity'],boid['xposition'],boids['xposition'][j],0.01/number_of_boids)
              boid['yvelocity']=velocity_change(boid['yvelocity'],boid['yposition'],boids['yposition'][j],0.01/number_of_boids)
	


      
	#Fly away from nearby boids
        for boid in boids:
           for j in range(number_of_boids):
                        if position_difference_test(boid['xposition'],boids['xposition'][j],boid['yposition'],boids['yposition'][j],100):
				boid['xvelocity']=velocity_change(boid['xvelocity'],boids['xposition'][j],boid['xposition'],1)
				boid['yvelocity']=velocity_change(boid['yvelocity'],boids['yposition'][j],boid['yposition'],1)
	
			

	# Try to match speed with nearby boids
	for boid in boids:
		for j in range(number_of_boids):
			if position_difference_test(boid['xposition'],boids['xposition'][j],boid['yposition'],boids['yposition'][j],10000):
				boid['xvelocity']=velocity_change(boid['xvelocity'],boid['xvelocity'],boids['xvelocity'][j],0.125/number_of_boids)
				boid['yvelocity']=velocity_change(boid['yvelocity'],boid['yvelocity'],boids['yvelocity'][j],0.125/number_of_boids)

	# Move according to velocities
	for boid in boids:
		boid['xposition']=change_in_position(boid['xposition'],boid['xvelocity'])
		boid['yposition']=change_in_position(boid['yposition'],boid['yvelocity'])


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))

scatter=axes.scatter(boids['xposition'],boids['yposition'])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids['xposition'],boids['yposition']))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()


