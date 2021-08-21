# Making necessary imports to the file
import numpy as np 
import matplotlib.pyplot as plt 


horizontal_axis = 10
vertical_axis = 10

# This will create the initial conditions for the universe where our game will be played
def initial_conditions():
    initial_matrix = np.zeros((horizontal_axis, vertical_axis))
    initial_matrix[4,4] = 1
    initial_matrix[4,5] = 1
    initial_matrix[4,6] = 1
    # initial_matrix[5,5] = 1
    # initial_matrix[5,6] = 1
    # initial_matrix[5,7] = 1
    # initial_matrix[i,j] = 1
    return initial_matrix

print(initial_conditions())

# Initializing the next state of the Game Of Life
next_state = np.zeros((horizontal_axis, vertical_axis))

# Loading the initial conditions
current_state = initial_conditions()

# One time step of the game
def one_timestep(current_state):    

    next_state = np.zeros((horizontal_axis, vertical_axis))
    
    # The dreaded nested for loop part
    for vertical_idx in range(vertical_axis):
        for horizontal_idx in range(horizontal_axis):
            
            # Live cell with two neighbours, dead cell with three neighbours
            if np.sum(current_state[horizontal_idx-1:horizontal_idx+2, vertical_idx-1:vertical_idx+2]) == 3:
                next_state[horizontal_idx, vertical_idx] = 1

            # Live cell with three neighbours
            elif np.sum(current_state[horizontal_idx-1:horizontal_idx+2, vertical_idx-1:vertical_idx+2]) == 4 : #- current_state[horizontal_idx, vertical_idx] == 3 :
                next_state[horizontal_idx, vertical_idx] = 1

            # This is the dying case, anything other than the above is dead
            else :
                next_state[horizontal_idx, vertical_idx] = 0
    
    return next_state

# Running the game over prescribed number of timesteps
def Game_Of_Life(n_iters, current_state):

    # The loop over all iterations
    for idx in range(n_iters):
        print(current_state)
        current_state = one_timestep(current_state)


# Executing the file
Game_Of_Life(10, current_state)


### Things to do :
### Make code better - rn we're calling an empty slate for every iteration