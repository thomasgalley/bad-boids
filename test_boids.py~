#from boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml
import boids


def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    test=boids.boids(0.01,100,10000,0.125,50)
    test.initial_data(regression_data["before"])
    test.update_boids()
    test_after=[[boid.xposition for boid in test.boids],[boid.yposition for boid in test.boids],[boid.xvelocity for boid in test.boids], [boid.yvelocity for boid in test.boids]] 
    
    for j in range (4):
       for i in range (50):
        assert_almost_equal(regression_data["after"][j][i],test_after[j][i],delta=20)
    
        
          
    
   
	


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
