from scipy.integrate import solve_ivp
import numpy as np

# Constants and initial conditions for the double pendulum
g = 9.81  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
m1 = 1.0  # mass of pendulum 1 in kg
m2 = 1.0  # mass of pendulum 2 in kg
initial_state = [np.pi / 2, 0, np.pi / 2, 0]  # initial state [theta1, omega1, theta2, omega2]

# Time vector
t = np.linspace(0, 10, 200)  # simulate for 10 seconds

# Differential equations for the double pendulum
def double_pendulum(t, y):
    theta1, z1, theta2, z2 = y

    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)

    theta1_dot = z1
    z1_dot = (m2 * g * np.sin(theta2) * c - m2 * s * (L1 * z1 ** 2 * c + L2 * z2 ** 2) -
              (m1 + m2) * g * np.sin(theta1)) / L1 / (m1 + m2 * s ** 2)

    theta2_dot = z2
    z2_dot = ((m1 + m2) * (L1 * z1 ** 2 * s - g * np.sin(theta2) + g * np.sin(theta1) * c) +
              m2 * L2 * z2 ** 2 * s * c) / L2 / (m1 + m2 * s ** 2)

    return theta1_dot, z1_dot, theta2_dot, z2_dot

# Solve the differential equations
sol = solve_ivp(double_pendulum, [t.min(), t.max()], initial_state, t_eval=t, method='RK45')

sol.y.shape  # Check the shape of the solution to confirm it's correct

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to get the (x, y) coordinates of the two pendulums
def get_xy_from_angles(theta1, theta2):
    # Pendulum 1 coordinates
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    # Pendulum 2 coordinates
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    return (x1, y1, x2, y2)

# Extract the angles from the solution
theta1s, theta2s = sol.y[0], sol.y[2]

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim((-3, 3))
ax.set_ylim((-3, 3))

# Create lines for the rods and a point for the pendulum mass
line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=1, ms=2)
time_template = 'Time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
history_x, history_y = [], []

# Initialize the animation
def init():
    line.set_data([], [])
    trace.set_data([], [])
    time_text.set_text('')
    return line, trace, time_text

# Animation function. This is called sequentially
def animate(i):
    x1, y1, x2, y2 = get_xy_from_angles(theta1s[i], theta2s[i])
   
    # Update the rod and mass positions
    line.set_data([0, x1, x2], [0, y1, y2])
   
    # Update the trace of the pendulum
    history_x.append(x2)
    history_y.append(y2)
    trace.set_data(history_x, history_y)
   
    # Update the time text
    time_text.set_text(time_template % (i*t.max()/len(theta1s)))
    return line, trace, time_text

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, blit=True, interval=50)

# Save the animation as a gif
gif_path = "double_pendulum.gif"
ani.save(gif_path, writer='imagemagick', fps=20)