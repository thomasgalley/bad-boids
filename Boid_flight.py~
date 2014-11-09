from Boid_differences import velocity_change, position_difference_test,change_in_position

def fly_to_middle(boids,threshold,number_of_boids):
    for boid in boids:
           for j in range(number_of_boids):
              boid['xvelocity']=velocity_change(boid['xvelocity'],boid['xposition'],boids['xposition'][j],threshold)
              boid['yvelocity']=velocity_change(boid['yvelocity'],boid['yposition'],boids['yposition'][j],threshold)



def fly_away_from_boids(boids,number_of_boids,threshold1,threshold2):
        for boid in boids:
           for j in range(number_of_boids):
                        if position_difference_test(boid['xposition'],boids['xposition'][j],boid['yposition'],boids['yposition'][j],threshold1):
				boid['xvelocity']=velocity_change(boid['xvelocity'],boids['xposition'][j],boid['xposition'],threshold2)
				boid['yvelocity']=velocity_change(boid['yvelocity'],boids['yposition'][j],boid['yposition'],threshold2)

def match_speed(boids,number_of_boids,threshold1,threshold2):
   for boid in boids:
       for j in range(number_of_boids):
	   if position_difference_test(boid['xposition'],boids['xposition'][j],boid['yposition'],boids['yposition'][j],threshold1):
	       boid['xvelocity']=velocity_change(boid['xvelocity'],boid['xvelocity'],boids['xvelocity'][j],threshold2)
	       boid['yvelocity']=velocity_change(boid['yvelocity'],boid['yvelocity'],boids['yvelocity'][j],threshold2)


def move_boids(boids):
   for boid in boids:
		boid['xposition']=change_in_position(boid['xposition'],boid['xvelocity'])
		boid['yposition']=change_in_position(boid['yposition'],boid['yvelocity'])
