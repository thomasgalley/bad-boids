"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

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
boids=(boids_initial_x_positions,boids_initial_y_positions,boid_initial_x_velocities,boid_initial_y_velocities)

def velocity_change(velocity1,parameter1,parameter2,change_magnitude):
   velocitynew=velocity1+(parameter2-parameter1)*change_magnitude
   return velocitynew

def position_difference_test(position_x1,position_x2,position_y1,position_y2,threshold):
   if (position_x2-position_x1)**2 + (position_y2-position_y1)**2 < threshold:
      return True

def change_in_position(position,velocity,time_increment=1):
   new_position=position+velocity*time_increment
   return new_position


    

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(number_of_boids):
		for j in range(number_of_boids):
                        xvs[i]=velocity_change(xvs[i],xs[i],xs[j],0.01/number_of_boids)
                        #if including time increment in whole code, would need to be added in this bit			
	for i in range(number_of_boids):
		for j in range(number_of_boids):
			yvs[i]=velocity_change(yvs[i],ys[i],ys[j],0.01/number_of_boids)
	# Fly away from nearby boids
	for i in range(number_of_boids):
		for j in range(number_of_boids):
			if position_difference_test(xs[i],xs[j],ys[i],ys[j],100):
				xvs[i]=velocity_change(xvs[i],xs[j],xs[i],1)
				yvs[i]=velocity_change(yvs[i],ys[j],ys[i],1)
	# Try to match speed with nearby boids
	for i in range(number_of_boids):
		for j in range(number_of_boids):
			if position_difference_test(xs[i],xs[j],ys[i],ys[j],10000):
				xvs[i]=velocity_change(xvs[i],xvs[i],xvs[j],0.125/number_of_boids)
				yvs[i]=velocity_change(yvs[i],yvs[i],yvs[j],0.125/number_of_boids)
	# Move according to velocities
	for i in range(number_of_boids):
		xs[i]=change_in_position(xs[i],xvs[i])
		ys[i]=change_in_position(ys[i],yvs[i])


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
