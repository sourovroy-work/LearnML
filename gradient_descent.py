import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

x_poly = np.linspace(-3,5,81)
def cost_function(X):
    return 2*X**2-4*X
def gradient(X):
    return  (4*X) -4
y_poly = cost_function(x_poly)

def f(iterations,learning_rate):
    x_path = np.empty(iterations,)
    x_path[0] = 0 #x_start
    for i in range (1,iterations):
        derivative =gradient(x_path[i-1])
        x_path[i] = x_path[i-1]-(derivative*learning_rate)
    x_path
    plt.plot(x_poly,y_poly)
    plt.plot(x_path,cost_function(x_path),'-o')
    
interactive_plot = interactive(f,iterations = (1,20),learning_rate= (0.01,1,.1))
interactive_plot
