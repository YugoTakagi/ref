import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv


class bezier(object):
    """docstring for bezier"""
    number_of_points = 0
    def __init__(self,number_of_points=0):
        self.number_of_points = number_of_points
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
    def bezier_making(self, bezier_set, num):
        list_of_bezier = []
        for t in np.linspace(0, 1, self.number_of_points):
            list_of_bezier.append(self.bezier(num,t,bezier_set))
        '''
        plt.plot(LOBS.T[0], LOBS.T[1], marker="o")
        #plt.plot(bezier_set1.T[0], bezier_set1.T[1], '--o')
        plt.axis("equal")
        plt.grid(True)
        plt.show()
        #'''
        return list_of_bezier

    def new_bezier_plt(self, list_of_bezier, new_index_for_bezier, len_new_index_for_bezier):
        IND = np.arange(start=0, stop=len_new_index_for_bezier-1, step=1, dtype= int)
        new_lob = []
        for ind in IND:
            new_lob.append(list_of_bezier[new_index_for_bezier[ind]])
        NEW_LOBS = np.array(new_lob)

        with open('csv_item/x_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(NEW_LOBS.T[0])
        with open('csv_item/y_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(NEW_LOBS.T[1])
        '''
        with open('csv_item/test.csv', 'w') as f:
            writer = csv.writer(f)
            #writer.writeheader()
            writer.writerow(NEW_LOBS.T[0])
            writer.writerow(NEW_LOBS.T[1])
        '''
        '''
        plt.plot(NEW_LOBS.T[0], NEW_LOBS.T[1], marker="o")
        plt.axis("equal")
        plt.grid(True)
        plt.title("new bezier")
        plt.show()
        #'''
        return NEW_LOBS, new_lob
