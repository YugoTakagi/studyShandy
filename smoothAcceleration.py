import sympy as sym
from sympy.plotting import plot
sym.init_printing(use_unicode=True)
import numpy as np
import matplotlib.pyplot as plt
(x) = sym.symbols('x')

class SmoothAccelerationClass(object):
    """docstring for SmoothAccelerationClass
    This class can make smooth acceleration file.

    def design() is main of this class.
    """
    def __init__(self, a, vel_want, vel_start, vel_end, curve, x_start, time_start):
        self.a = a
        self.vel_want = vel_want
        self.vel_start = vel_start
        self.vel_end = vel_end

        self.x = curve.T[0]
        self.y = curve.T[1]

        self.xs = x_start

        self.time_start = time_start
        self.t1 = 0.0
        self.t2 = 0.0
        self.t3 = 0.0
        self.t = 0.0
        self.dt = 0.02

        self.loc1 = 0.0
        self.loc2 = 0.0
        self.loc3 = 0.0

        self.vel1 = 0.0
        self.vel2 = 0.0
        self.vel3 = 0.0
    def design(self):
        """docstring for design()
        this function is main of SmoothAccelerationClass.

        return arrayAcc, arrayVel, arrayLoc
        arrayAcc := array of accel(time)
        arrayVel := array of velosity(time)
        arrayLoc := array of location(time)
        """
        curve_len = self.curve_length(self.x, self.y)
        self._time_designer(curve_len)
        print(self.t1, self.t2, self.t3)
        arrayTime = np.arange(self.time_start, self.time_start +self.t, self.dt)
        arrayAcc = []
        arrayVel = []
        arrayLoc = []
        for ts in arrayTime:
            arrayAcc.append(self._acc(ts, self.a))
            arrayVel.append(self._vel(ts))
            arrayLoc.append(self._loc(ts))
        plt.plot(arrayTime, arrayAcc, marker=".", color="tomato")
        plt.plot(arrayTime, arrayVel, marker=".", color="skyblue")
        plt.plot(arrayTime, arrayLoc, marker=".", color="g")
        plt.show()
        return arrayAcc, arrayVel, arrayLoc
    def curve_length(self, x, y):
        curve_length = 0
        for index in range(len(x)-1):
            if (index - 1) <= 0:
                dx = 0.0
                dy = 0.0
            else:
                dx = x[index] - x[index - 1]
                dy = y[index] - y[index - 1]
            ds = np.sqrt(dx**2 + dy**2)
            curve_length += ds
        return curve_length
    def _get_end_time(self):
        return self.t
    def _acc(self,ts, a):
        if 0.0 <= ts and ts <= self.t1:
            return self.a[0]
        elif self.t1< ts and ts <= self.t2:
            return self.a[1]
        elif self.t2 < ts and ts <= self.t3:
            return self.a[2]
        else:
            pass
    def _vel(self,ts):
        if 0.0 <= ts and ts <= self.t1:
            # return sym.integrate(self.acc(ts,self.a),(x, 0, ts))
            self.vel1 = self.a[0]*ts +self.vel_start
            return self.vel1
        elif self.t1< ts and ts <= self.t2:
            # return sym.integrate(self.acc(ts,self.a),(x, self.t1, ts)) +sym.integrate(self.acc(self.t1,self.a),(x, 0, self.t1))
            self.vel2 = self.vel1
            return self.vel2
        elif self.t2 < ts and ts <= self.t3:
            # return sym.integrate(self.acc(ts,self.a),(x, self.t2, ts)) +sym.integrate(self.acc(self.t2,self.a),(x, self.t1, self.t2)) +sym.integrate(self.acc(self.t1,self.a),(x, 0, self.t1))
            self.vel3 = self.a[2]*(ts-(self.t2)) +self.vel2
            return self.vel3
        else:
            pass
    def _loc(self,ts):
        if 0.0 <= ts and ts <= self.t1:
            self.loc1 = (self.a[0]*ts**2)/2.0 +self.vel_start*ts +self.xs
            return self.loc1
            # self.loc1 = sym.integrate(sym.integrate(self.acc(ts,self.a),x),(x, 0, ts))
            # return self.loc1
        elif self.t1< ts and ts <= self.t2:
            self.loc2 = (self.a[0]*self.t1 + self.vel_start)*(ts-self.t1) +self.loc1
            return self.loc2
            # self.loc2 = sym.integrate(sym.integrate(self.acc(ts,self.a),x)+self.loc1,(x, self.t1, ts)) +self.loc1
            # return self.loc2
        elif self.t2 < ts and ts <= self.t3:
            self.loc3 = (self.a[2]*(ts-(self.t2))**2)/2.0 +self.a[0]*self.t1*(ts-(self.t2)) + (self.vel_start *(ts-(self.t2))) +self.loc2
            return self.loc3
            # return sym.integrate(sym.integrate(self.acc(ts,self.a),x)+sym.integrate(self.acc(ts,self.a),x)+self.loc1,(x, 0, ts-self.t2)) +self.loc2
        else:
            pass
    def _time_designer(self,curve_length):
        self.t1 = (self.vel_want - self.vel_start)/self.a[0]
        self.t3 = abs((self.vel_want - self.vel_end)/self.a[2])
        l = curve_length
        l1 = (self.vel_start + self.vel_want)*self.t1 / 2.0
        l3 = (self.vel_want + self.vel_end)*self.t3 / 2.0

        self.t2 = (l - l1 -l3)/self.vel_want +self.t1
        self.t3 += self.t2
        self.t = self.t3
        if self.t2<0:
            #print pycolor.RED + "T2 error" +pycolor.END
            print("\n")
            print("t2 error := {}".format(self.t2))
