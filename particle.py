# Physics 91SI
# Spring 2017
# Lab 8

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets position vector
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,)) #tuple
        self.acc = np.zeros((2,)) 

class Molecule:
	def __init__(self, p1_pos, p1_m , p2_pos , p2_m, spring_constant, equillibrium_length):
		self.p1 = Particle(p1_pos,p1_m)
		self.p2 = Particle(p2_pos,p2_m)
		self.L0 = equillibrium_length		
		self.k = spring_constant
	def get_displ(self):
		return np.subtract(self.p2.pos,self.p1.pos)
	def get_force(self):
		displacement = self.get_displ()
		displacement_magnitude= np.sqrt(displacement[0]**2+ displacement[1]**2)
		force_magnitude= self.k*(displacement_magnitude - self.L0)
		force_x = force_magnitude * (displacement[0] / displacement_magnitude)
		force_y = force_magnitude * (displacement[1] / displacement_magnitude)
		return [force_x, force_y]


