#!/usr/bin/python3

# Physics 91SI
# molecule 2017
# Lab 8

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle

# TODO: Implement this function
def init_molecule():
    molly = particle.Molecule([0.2,0.2], 1,[0.8, 0.8], 2, 1, 0.5)
    print(molly.get_displ())
    print(molly.get_force())

    return molly




def time_step(dt, mol):
    """Sets new positions and velocities of the particles attached to mol"""
    ##equations from wikipedia page on leapfrog integration. assuming dt is constant
    a_i1= [x*(1/mol.p1.m) for x in mol.p1.acc]
    a_i2 = [x*(-1/mol.p2.m) for x in mol.p2.acc]

    new_pos_p1 = [p+q+r for p,q,r in zip(mol.p1.pos, [x*dt for x in mol.p1.vel], [0.5*dt*dt*a for a in a_i1])]
    mol.p1.pos = new_pos_p1

    new_pos_p2 = [p+q+r for p,q,r in zip(mol.p2.pos,[x*dt for x in mol.p2.vel], [0.5*dt*dt*a for a in a_i2])]
    mol.p2.pos = new_pos_p2

    a_i1_new= [x*(1/mol.p1.m) for x in mol.get_force()]
    a_i2_new = [x*(-1/mol.p2.m) for x in mol.get_force()]


    new_vel_p1 = [p+q for p,q in (mol.p1.vel, [0.5*(x+y)*dt for x,y in zip (a_i1, a_i1_new)])]
    mol.p1.vel = new_vel_p1
    new_vel_p2 = [p+q for p,q in zip(mol.p2.vel, [0.5*(x+y)*dt for x,y in zip (a_i2, a_i2_new)])]
    mol.p2.vel = new_vel_p2

    print(mol.p1.pos)
    print(mol.p1.vel) 
    print(mol.p2.pos)
    print(mol.p2.vel)

#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    ax.clear()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
