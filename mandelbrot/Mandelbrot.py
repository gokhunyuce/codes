#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 21:59:56 2025

@author: gokhunmelih.yuce
+905375167847
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

t0 = time.time()

# Set parameters 

x0, x1 = -2.0, 1.0 
y0, y1 = -1.5, 1.5 
n = 1000
max_iter = 100


"""
x0 = float(input("x0: "))
x1 = float(input("x1: "))
y0 = float(input("y0: "))
y1 = float(input("y1: "))
n = int(input("resolution: "))
max_iter = int(input("maximum iteration: "))
"""
print("Computing Mandelbrot frames...")

# Create grid
x, y = np.linspace(x0, x1, n), np.linspace(y0, y1, n)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y


# Initialize arrays
Z = np.zeros_like(C)
K = np.zeros(C.shape, dtype=int)

# Precompute all frames
frames = []
for i in range(max_iter):
    mask = np.abs(Z) <= 2
    Z[mask] = Z[mask]**2 + C[mask]
    K[mask] = i + 1
    frames.append(K.copy())
    print(f"Computed frame {i+1}/{max_iter}", end='\r')
    
print("\nSetting up animation...")

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))
img = ax.imshow(frames[0], extent=[x0, x1, y0, y1], 
               cmap='hot', origin='lower', vmin=0, vmax=max_iter)
plt.colorbar(img)
title = ax.text(0.5, 1.05, "", transform=ax.transAxes, ha="center")

# Animation function
def animate(i):
    img.set_array(frames[i])
    title.set_text(f"Mandelbrot Set (Iteration {i+1})")
    return [img, title]

ani = FuncAnimation(fig, animate, frames=len(frames),
                   interval=50, blit=True)

# For regular Python scripts:
ani.save('mandelbrot.gif', writer='pillow', fps=15)
plt.show()

t1 = time.time()

print(t1-t0,"seconds took")

    