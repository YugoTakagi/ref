import numpy as np
import math
import matplotlib.pyplot as plt
import csv

from .bezier import bezier

class accel_designer(object):
    """docstring foraccel_designer."""
    #curve_length = 0
    #t = 0
    def __init__(self):
        pass
    def making_accel(self, a, VEL, X, time_start):
        ########################################################################
        ####|              a   := kasoku do(float)                         |####
        ####|              X   := [x_ref, y_ref, s_start]                  |####
        ####|              VEL := [vel_want, vell_start, vell_end]         |####
        ####|              time_start                                      |####
        ########################################################################
        curve_length = self.making_curve_length(X[0], X[1])
        t, t1, t2, t3 = self.time_designer(a, VEL, curve_length)
        TIMES = [t, t1, t2, t3]
        A, V, XX = self.quantity_designer(a, VEL, X, curve_length, TIMES, time_start)
        self.plot(A, V, XX, TIMES, time_start)# plt.plot all
        print("> making accel fin")
        return A, V, XX, curve_length, t
    def making_curve_length(self, x_ref, y_ref):
        curve_length = 0
        for index in np.arange(start=0, stop=len(x_ref)-1, step=1, dtype= int):
            if (index - 1) <= 0:
                #dx = x_ref[index]
                #dy = y_ref[index]
                dx = 0.0
                dy = 0.0
            else:
                dx = x_ref[index] - x_ref[index - 1]
                dy = y_ref[index] - y_ref[index - 1]
            ds = np.sqrt(dx**2 + dy**2)
            curve_length += ds
        return curve_length
    def time_designer(self, a, VEL, curve_length):
        vel_want = VEL[0]
        vel_start = VEL[1]
        vel_end = VEL[2]
        t1 = (vel_want - vel_start)/a
        t3 = (vel_want - vel_end)/a

        l = curve_length
        l1 = (vel_start + vel_want)*t1 / 2.0
        l3 = (vel_want + vel_end)*t3 / 2.0

        t2 = (l - l1 -l3)/vel_want
        t = t1+t2+t3
        #print("t1, t2, t3 = {}, {}, {}".format(t1,t2,t3))
        if t2<=0:
            #print pycolor.RED + "T2 error" +pycolor.END
            print("\n")
            print("t2 error := {}".format(t2))
            #print("curve_length = {}".format(curve_length))
        return t, t1, t2, t3
    def quantity_designer(self, a, VEL, X, curve_length, TIMES, time_start):
        A = []
        V  = []
        XX = []

        t  = TIMES[0]
        t1 = TIMES[1]
        t2 = TIMES[2]
        t3 = TIMES[3]

        vel_want  = VEL[0]
        vel_start = VEL[1]
        vel_end   = VEL[2]

        x_start = X[2]
        for ind in np.arange(0.0, t, 0.008):
            if ind<=t1:
                A.append(a)
                v1 = a*ind +vel_start
                V.append(v1)
                x1 = (a*ind**2)/2.0 +vel_start*ind +x_start
                XX.append(x1)
            elif ind<=t1+t2:
                A.append(0.0)
                v2 = v1
                V.append(v2)
                x2 = (a*t1 + vel_start)*(ind-t1) +x1
                XX.append(x2)
            elif ind<= t:
                A.append(-a)
                v3 = -a*(ind-(t1+t2)) +v2
                V.append(v3)
                x3 = (-a*(ind-(t1+t2))**2)/2.0 +a*t1*(ind-(t1+t2)) + (vel_start *(ind-(t1+t2))) +x2
                XX.append(x3)
            else:
                #print pycolor.RED + "a-t error" +pycolor.END
                print("a-t error")
        return A, V, XX
    def a_designer(self, t, TIMES, ITEM):
        t0 = 0
        t1 = TIMES[1]
        t2 = TIMES[2]
        t3 = TIMES[3]
        am = ITEM[0]
        if (t <= t0):
            return 0
        elif (t <= t1):
            #return 1.0 / tc * a * (t - t0)
            return am
        elif (t <= t2):
            return 0
        elif (t <= t3):
            #return -1.0 / tc * a * (t - t3)
            return -am
        else:
            return 0
    def v_designer(self, t, TIMES, ITEM):
        t0 = 0
        t1 = TIMES[1]
        t2 = TIMES[2]
        t3 = TIMES[3]
        am = ITEM[0]
        v0 = ITEM[4]
        if (t <= t0):
            return v0
        elif (t <= t1):
            #return v0 + 0.5 / tc * a * (t - t0) * (t - t0)
            return a*ind +vel_start
        elif (t <= t2):
            return v0
        elif (t <= t3):
            #return v3 - 0.5 / tc * a * (t - t3) * (t - t3)
            return -am*t + v0
        else:
            return -am*t + v0
    def x_designer(self, t, TIMES, ITEM):
        t0 = 0
        t1 = TIMES[1]
        t2 = TIMES[2]
        t3 = TIMES[3]
        am = ITEM[0]
        v0 = ITEM[4]
        x0 = 0
        if (t <= t0):
            return x0 + v0 * (t - t0)
        elif (t <= t1):
            #return x0 + v0 * (t - t0) + a / 6 / tc * (t - t0) * (t - t0) * (t - t0)
            return (a*ind**2)/2.0 + x_start
        elif (t <= t2):
            return v0*t + x0
        elif (t <= t3):
            #return x3 + v3 * (t - t3) - a / 6 / tc * (t - t3) * (t - t3) * (t - t3)
            return 0.5*-am*t**2 + v0*t + x0
        else:
            return 0.5*-am*t**2 + v0*t + x0
    def plot(self, A, V, XX, TIMES, time_start):
        t = TIMES[0]
        time = np.arange(start= time_start, stop= t + time_start, step= 0.008, dtype= np.float)
        #print('len(time)={}'.format(len(time)))
        #print('len(V)={}'.format(len(V)))
        plt.plot(time, A, color ="red", marker="o", label='A')#marker=".", ls=""
        plt.plot(time, V, color ="#FE9A2E", marker="o", label='V')#linewidth=3
        plt.plot(time,XX, color ="Green", marker="o", label='X')
        plt.title("accel_designer")
        plt.legend()
        #plt.show()
    def get_curve_length(self):
        return self.curve_length
    def get_t(self):
        return self.t

    ''' # IDEA:
    for ind in np.arange(0.0, t, 0.008):
        ad = self.a_designer(ind, TIMES, ITEM)
        vd = self.v_designer(ind, TIMES, ITEM)
        xd = self.x_designer(ind, TIMES, ITEM)
        A.append(ad)
        V.append(vd)
        XX.append(xd)
    '''
