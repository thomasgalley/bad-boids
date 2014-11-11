import boid_class 
from parameters import* 
from nose.tools import*

def test_initial_flock():
   flock=boid_class.boids(attraction_strength,boidproximitythreshold,matchspeed_distance,matchspeed_strength,number_of_boids)
   flock.initial_flock()
   for boid in flock.boids: 
      assert_greater(boid.xposition, boids_starting_x_position_range[0])
      assert_greater(boid.yposition, boids_starting_y_position_range[0])
      assert_greater(boid.xvelocity, boids_starting_x_velocity_range[0])
      assert_greater(boid.yvelocity, boids_starting_y_velocity_range[0])
      assert_less(boid.xposition, boids_starting_x_position_range[1])
      assert_less(boid.yposition, boids_starting_y_position_range[1])
      assert_less(boid.xvelocity, boids_starting_x_velocity_range[1])
      assert_less(boid.yvelocity, boids_starting_y_velocity_range[1])
