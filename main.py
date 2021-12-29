import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from constraint_penalties.relaxed_barrier_penalty import RelaxedBarrierPenalty


# The parametrized function to be plotted
def function(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)


t = np.linspace(-20, 10, 3001)

# Define initial parameters
init_mu = 0.1
init_delta = 5

penalty = RelaxedBarrierPenalty(init_mu, init_delta)

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
ax.grid()
line, = plt.plot(t, penalty.cost_function(t), lw=1)
ax.set_xlabel('Time [s]')

# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axdelta = plt.axes([0.25, 0.1, 0.65, 0.03])
delta_slider = Slider(
    ax=axdelta,
    label='Delta',
    valmin=0.1,
    valmax=10,
    valinit=init_delta,
)

# Make a vertically oriented slider to control the amplitude
axmu = plt.axes([0.1, 0.25, 0.0225, 0.63])
mu_slider = Slider(
    ax=axmu,
    label="Mu",
    valmin=0,
    valmax=1000,
    valinit=init_mu,
    orientation="vertical"
)

# The function to be called anytime a slider's value changes


def update(val):
    penalty.update_params(mu_slider.val, delta_slider.val)
    line.set_ydata(penalty.cost_function(t))
    ax.relim()
    # update ax.viewLim using the new dataLim
    ax.autoscale_view()
    fig.canvas.draw_idle()


# register the update function with each slider
delta_slider.on_changed(update)
mu_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    delta_slider.reset()
    mu_slider.reset()


button.on_clicked(reset)


plt.show()


# if __name__ == "__main__":
#     main()
