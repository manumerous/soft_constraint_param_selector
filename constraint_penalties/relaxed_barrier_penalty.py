from numpy import log as ln
import numpy as np


class RelaxedBarrierPenalty():
    def __init__(self, mu, delta):
        self.update_params(mu, delta)

    def update_params(self, mu, delta):
        self.mu = mu
        self.delta = delta

    def cost_function(self, constraint_value):
        penalty = np.zeros(len(constraint_value))
        for i in range(len(constraint_value)):
            if (constraint_value[i] > self.delta):
                penalty[i] = -self.mu * ln(constraint_value[i])
            else:
                penalty[i] = -self.mu * ln(self.delta) + self.mu / 2.0 * \
                    (((constraint_value[i] - 2*self.delta)/self.delta)**2 - 1)
        return penalty
