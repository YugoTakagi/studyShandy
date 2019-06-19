import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv


class BezierClass(object):
    """docstring for BezierClass
    this class making bezier curve.
    """
    def __init__(self,points=0):
        self.points = points
    def comb(self, n, k):
        m = 1
        if n < 2 * k:
            k = n - k
        for i in range(1, k + 1):
            m = m * (n - i + 1) / i
        return m
    def bernstein(self, n, i, t):
        return self.comb(n, i) * t**i * (1 - t)**(n-i)
    def bezier(self, n, t, q):
        p = np.zeros(2)
        for i in range(n + 1):
            p += self.bernstein(n, i, t) * q[i]
        return p
    def bezier_making(self, anchors, dim):
        """docstring for bezier_making()
        this function is main of BezierClass.

        return bezier
        bezier := array[[x1,y1],[x2,y2],...] of bezier curve
        """
        bezier_curve = []
        for t in np.linspace(0, 1, self.points):
            bezier_curve.append(self.bezier(dim,t,anchors))

        bezier = np.array(bezier_curve)
        plt.plot(bezier.T[0], bezier.T[1], marker=".")
        plt.plot(anchors.T[0], anchors.T[1], '--*')
        plt.axis("equal")
        plt.grid(True)
        plt.show()

        return bezier
