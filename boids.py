"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy

# Deliberately terrible code for teaching purposes

number_of_boids=50
boids_starting_x_position_range=[-450,50.0]
boids_starting_y_position_range=[300.0,600.0]
boids_starting_x_velocity_range=[0,10.0]
boids_starting_y_velocity_range=[-20.0,20.0]

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

print boids


    

def update_boids(boids):
	#boids['xposition'],boids['yposition'],boids['xvelocity'],boids['yvelocity']=boids
        
        #boids= numpy.array((number_of_boids),dtype=[('xposition','f8'),('yposition','f8'),('xvelocity','f8'),('yvelocity','f8')])
        #for i in range(number_of_boids): 
           #boids[i]=(boids['xposition'][i],boids['yposition'][i],boids['xvelocity'][i],boids['yvelocity'][i])
        # Fly towards the middle
        
        for i in range(number_of_boids):
           for j in range(number_of_boids):
              boids['xvelocity'][i]=velocity_change(boids['xvelocity'][i],boids['xposition'][i],boids['xposition'][j],0.01/number_of_boids)
              boids['yvelocity'][i]=velocity_change(boids['yvelocity'][i],boids['yposition'][i],boids['yposition'][j],0.01/number_of_boids)
	


      
	#Fly away from nearby boids
        for i in range(number_of_boids):
           for j in range(number_of_boids):
                        if position_difference_test(boids['xposition'][i],boids['xposition'][j],boids['yposition'][i],boids['yposition'][j],100):
				boids['xvelocity'][i]=velocity_change(boids['xvelocity'][i],boids['xposition'][j],boids['xposition'][i],1)
				boids['yvelocity'][i]=velocity_change(boids['yvelocity'][i],boids['yposition'][j],boids['yposition'][i],1)
	
			

	# Try to match speed with nearby boids
	for i in range(number_of_boids):
		for j in range(number_of_boids):
			if position_difference_test(boids['xposition'][i],boids['xposition'][j],boids['yposition'][i],boids['yposition'][j],10000):
				boids['xvelocity'][i]=velocity_change(boids['xvelocity'][i],boids['xvelocity'][i],boids['xvelocity'][j],0.125/number_of_boids)
				boids['yvelocity'][i]=velocity_change(boids['yvelocity'][i],boids['yvelocity'][i],boids['yvelocity'][j],0.125/number_of_boids)

	# Move according to velocities
	for i in range(number_of_boids):
		boids['xposition'][i]=change_in_position(boids['xposition'][i],boids['xvelocity'][i])
		boids['yposition'][i]=change_in_position(boids['yposition'][i],boids['yvelocity'][i])

print update_boids(boids)
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


