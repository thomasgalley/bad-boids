import random

number_of_boids= 50

boids_starting_x_position_range= [-450,50.0]
boids_starting_y_position_range= [300.0,600.0]
boids_starting_x_velocity_range= [0,10.0]
boids_starting_y_velocity_range= [-20.0,20.0]
attractionstrength=0.01
boidproximitythreshold=100
matchspeed_distance=10000
matchspeed_strength=0.125

boids_initial_x_positions=[random.uniform(*boids_starting_x_position_range) for x in range(number_of_boids)]
boids_initial_y_positions=[random.uniform(*boids_starting_y_position_range) for x in range(number_of_boids)]
boid_initial_x_velocities=[random.uniform(*boids_starting_x_velocity_range) for x in range(number_of_boids)]
boid_initial_y_velocities=[random.uniform(*boids_starting_y_velocity_range) for x in range(number_of_boids)]
