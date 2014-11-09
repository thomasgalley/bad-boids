"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy
import yaml
from parameters import*


from Boid_flight import fly_to_middle, fly_away_from_boids, match_speed, move_boids


boids_initial_x_positions=[random.uniform(*boids_starting_x_position_range) for x in range(number_of_boids)]
boids_initial_y_positions=[random.uniform(*boids_starting_y_position_range) for x in range(number_of_boids)]
boid_initial_x_velocities=[random.uniform(*boids_starting_x_velocity_range) for x in range(number_of_boids)]
boid_initial_y_velocities=[random.uniform(*boids_starting_y_velocity_range) for x in range(number_of_boids)]

boids = numpy.zeros((number_of_boids),dtype=[('xposition','f8'),('yposition','f8'),('xvelocity','f8'),('yvelocity','f8')])

for i in range(number_of_boids):
   boids[i]=(boids_initial_x_positions[i],boids_initial_y_positions[i],boid_initial_x_velocities[i],boid_initial_y_velocities[i])


def update_boids(boids):
	       
        
        fly_to_middle(boids,attractionstrength/number_of_boids,number_of_boids)
	
        fly_away_from_boids(boids,number_of_boids,boidproximitythreshold,1)

        match_speed(boids,number_of_boids,matchspeed_distance,matchspeed_strength/number_of_boids)
	 
        move_boids(boids)
			

	
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


