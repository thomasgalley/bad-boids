"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import numpy

from parameters import*
import boid_class

flock=boid_class.boids(attraction_strength,boidproximitythreshold,matchspeed_distance,matchspeed_strength,number_of_boids)
flock.initial_flock(number_of_boids)


			

	
figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))

scatter=axes.scatter([boid.xposition for boid in flock.boids],[boid.yposition for boid in flock.boids])

def animate(frame):
   flock.update_boids(number_of_boids)
   scatter.set_offsets(zip([boid.xposition for boid in flock.boids],[boid.yposition for boid in flock.boids]))


anim = animation.FuncAnimation(figure, animate,
                               frames=200, interval=50)

if __name__ == "__main__":
    plt.show()


