def velocity_change(velocity1,parameter1,parameter2,change_magnitude):
   velocitynew=velocity1+(parameter2-parameter1)*change_magnitude
   return velocitynew


def position_difference_test(position_x1,position_x2,position_y1,position_y2,threshold):
   if (position_x2-position_x1)**2 + (position_y2-position_y1)**2 < threshold:
      return True

def change_in_position(position,velocity,time_increment=1):
   new_position=position+velocity*time_increment
   return new_position
