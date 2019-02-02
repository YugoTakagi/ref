from class_item.target_item.bezier import bezier
from class_item.target_item.accel_designer import accel_designer
from class_item.target_item.integrate_number import integrate_number

#from color_class import pycolor as pc
import numpy as np
import matplotlib.pyplot as plt
import csv


class target(object):
    """docstring for target"""
    def __init__(self):
        pass
    def target_make(self, a, VEL, BEZIER, x_start, time_start):
        ##init##################################################################
        acd = accel_designer()
        inb = integrate_number()
        bz = bezier(number_of_points=1000)

        npBEZIER = np.array(BEZIER)
        ######################     making X REF     ############################
        X = [npBEZIER.T[0], npBEZIER.T[1], x_start]
        A, V, XX, curve_length, t = acd.making_accel(a, VEL, X, time_start)
        IN_INDEX, len_in_index = inb.integrate(X, XX)
        npREF, REF = bz.new_bezier_plt(BEZIER, IN_INDEX, len_in_index)

        ######################     making V REF     ############################
        alfa = self.making_angle(npREF,len(npREF))
        vx, vy= self.making_vx_and_vy(V,alfa,len(npREF))
        ##csv###################################################################
        with open('csv_item/vx_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vx)
        with open('csv_item/vy_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(vy)
        with open('csv_item/alfa_ref.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerow(alfa)
        ########################################################################
        self.vx = vx
        self.vy = vy
        self.alfa = alfa
        print("> target fin")
        return npBEZIER, BEZIER, npREF, REF, t, curve_length, vx, vy, alfa
    def making_vx_and_vy(self,V,ALFA,time):
        vx = []
        vy = []
        for index in np.arange(start=0, stop=time-1, step=1, dtype= int):#linspace_time:
            if (index -1) <= 0:
                vx.append(V[index] * np.sin(ALFA[index]))
                vy.append(V[index] * np.cos(ALFA[index]))
                #print("index = {}".format(index))
            else:
                vx.append(V[index] * np.sin(ALFA[index-1]))
                vy.append(V[index] * np.cos(ALFA[index-1]))
                #print("index = {}".format(index))
        return vx, vy
    def making_angle(self, NEW_LOBS, len_new_index_for_bezier):
        alfa=[]
        x_ref = NEW_LOBS.T[0]
        y_ref = NEW_LOBS.T[1]
        IND = np.arange(start=0, stop=len_new_index_for_bezier-1, step=1, dtype= int)
        for index in IND:
            if (index - 1) <= 0:
                dx = x_ref[index]
                dy = y_ref[index]
            else:
                dx = x_ref[index] - x_ref[index-1]
                dy = y_ref[index] - y_ref[index-1]
            if dy>0:
                alfa.append(np.arctan(dx/dy))
            else:
                alfa.append(np.pi - np.arctan(-dx/dy))
        return alfa
