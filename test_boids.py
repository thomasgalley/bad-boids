from boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	


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
