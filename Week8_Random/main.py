#!/usr/bin/env python
import numpy as np
import time
import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

past_ms = []
past_lc = []
past_bb = []
running = True

def middle_squares(seed=1234):
    global past_ms
    
    if len(past_ms) == 0:
        n = seed
    else:
        n = past_ms[-1]

    n = int(str(n * n).zfill(8)[2:6])

    past_ms.append(n)
        
    return n

def linear_congen(seed=1, m=134456, a=8121, c=28411):
    global past_lc

    if len(past_lc) == 0:
        n = seed
    else:
        n = (a*past_lc[-1] + c) % m
    
    past_lc.append(n)

    return n

def blumblumshub(seed=1, m=47*46):
    global past_bb
    if len(past_bb) == 0:
        n = seed
    else:
        n = past_bb[-1]
        n = (n*n) % m

    past_bb.append(n)

    return n

def on_key(event):
    global running
    running = False

def main():
    global running
    # Initialize the plot
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)  # Adjust plot for buttons if needed

    x_data, ms_data, lc_data, bb_data = [], [], [], []
    line_ms, = ax.plot(x_data, ms_data, '-o', label="Middle Squares")
    line_lc, = ax.plot(x_data, lc_data, '-x', label="Linear Congruential")
    line_bb, = ax.plot(x_data, bb_data, '-s', label="Blum Blum Shub")

    ax.legend()
    ax.set_title("Random Number Generators")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Generated Value")

    t = 0
    speed = 10
    seed_value = 1234

    running = True

    fig.canvas.mpl_connect('key_press_event', on_key)  # Escape on key press
    fig.canvas.mpl_connect('close_event', on_key)  # Escape on plot close

    while running:  # Loop to add 20 points
        x_data.append(t)  # Add the new x value
        ms_data.append(middle_squares(seed=seed_value))
        lc_data.append(linear_congen(seed=seed_value)/10)
        bb_data.append(blumblumshub(seed=seed_value))
            
        line_ms.set_data(x_data, ms_data)
        line_lc.set_data(x_data, lc_data)
        line_bb.set_data(x_data, bb_data)
        
        ax.relim()  # Recalculate limits
        ax.autoscale_view()  # Autoscale the view to include the new data
            
        plt.draw()  # Redraw the plot
        plt.pause(1/speed)  # Pause for half a second

        t += 1

    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the final plot

        
if __name__ == "__main__":
    main()