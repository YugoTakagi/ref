from class_item.target import target
from class_item.target_item.bezier import bezier

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv
#'''
import matplotlib.animation as animation
from matplotlib import animation
#'''
class game(object):
    """docstring for game_class."""
    dt = 0
    def __init__(self, dt):
        self.dt = dt
    def run(self, anime):
        print("+++ game start")
        ##init #################################################################
        bz = bezier(number_of_points=5000)
        tg = target(self.dt)
        ##init accel_designer###################################################
        xs = 0.0                                #x start
        ts = 0.0                                #t start
        VEL1=[3.0, 0.0, 1.0]                    #vell_want, vell_start, vell_end
        VEL2=[3.0, 1.0, 2.0]                    #vell_want, vell_start, vell_end
        VEL3=[4.0, 2.0, 3.0]                    #vell_want, vell_start, vell_end
        VEL4=[4.0, 3.0, 3.0]                    #vell_want, vell_start, vell_end
        ##init bezier###########################################################
        BEZIER_ANCER1 = np.array([[0,0],[0,1.4],[-1.43,0.1],[-1.43,1.5]], dtype=np.float)
        BEZIER_ANCER2 = np.array([[-1.43,1.5],[-1.43,2.9],[-0.01,1.6],[-0.01,3.0]], dtype=np.float)
        BEZIER_ANCER3 = np.array([[-0.01,3.0],[-0.01,4.4],[-1.43,3.1],[-1.43,4.5]], dtype=np.float)
        BEZIER_ANCER4 = np.array([[-1.43,4.5],[-1.43,5.9],[-0.725,4.6],[-0.725,6.0]], dtype=np.float)

        BEZIER1 = bz.bezier_making(BEZIER_ANCER1, 3)
        BEZIER2 = bz.bezier_making(BEZIER_ANCER2, 3)
        BEZIER3 = bz.bezier_making(BEZIER_ANCER3, 3)
        BEZIER4 = bz.bezier_making(BEZIER_ANCER4, 3)

        ##def target_make(self, a, BEZIER, VEL, x_start, time_start):   * a := float
        NEW_LOB1, t1, x1, vx1, vy1, alfa1 = tg.target_make(5.0, VEL1, BEZIER1, xs, ts)
        NEW_LOB2, t2, x2, vx2, vy2, alfa2 = tg.target_make(5.0, VEL2, BEZIER2, x1, t1)
        NEW_LOB3, t3, x3, vx3, vy3, alfa3 = tg.target_make(5.0, VEL3, BEZIER3, x1+x2, t1+t2)
        NEW_LOB4, t4, x4, vx4, vy4, alfa4 = tg.target_make(5.0, VEL4, BEZIER4, x1+x2+x3, t1+t2+t3)


        REF = []
        REF.extend(NEW_LOB1)
        REF.extend(NEW_LOB2)
        REF.extend(NEW_LOB3)
        REF.extend(NEW_LOB4)
        npREF = np.array(REF)

        print("game time  := {}[s]".format(t1+t2+t3+t4))
        print("game lenge := {}[m]".format(x1+x2+x3+x4))
        self.plot(npREF)

        if anime == True:
            self.plot_size(npREF)
            ##init anime########################################################
            vx=[]
            vx.extend(vx1)
            vx.extend(vx2)
            vx.extend(vx3)
            vx.extend(vx4)
            vy=[]
            vy.extend(vy1)
            vy.extend(vy2)
            vy.extend(vy3)
            vy.extend(vy4)
            alfa=[]
            alfa.extend(alfa1)
            alfa.extend(alfa2)
            alfa.extend(alfa3)
            alfa.extend(alfa4)
            self.anime_ff(vx, vy, alfa)
            ####################################################################
        print("+++ end game")
    def plot(self, npREF):
        plt.show()
        #plt.hold(True)
        plt.plot(npREF.T[0],npREF.T[1], marker=".", color="#4278C5")
        plt.title("ref")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
    def plot_size(self, npREF):
        ########################################################################
        ########################################################################
        ###########################     model     ##############################
        ########################################################################
        #'''
        ax = plt.axes()
        COUNT = np.arange(start=0, stop=426, step=1, dtype= int)
        ssp=[-0.5,-0.5]
        for count in COUNT:
            r = patches.Rectangle(xy=(npREF.T[0][count] -0.35,npREF.T[1][count] -0.35), width=0.7, height=0.7, ec='#F5A9A9', fill=False)
            ax.add_patch(r)
            #c = patches.Circle(xy=(npNEW_LOB.T[0][count],npNEW_LOB.T[1][count]), radius=0.4, ec='#F5A9A9',fill=False)
            #ax.add_patch(c)
        ############################     field     #############################
        ########################################################################
        sotowaku = patches.Rectangle(xy=(-13.3+0.5,-0.5), width=13.3, height=10, ec='#FAAC58',fill=False)
        ax.add_patch(sotowaku)
        forest = patches.Rectangle(xy=(-2.45+0.5,-0.5), width=2.45, height=8, ec='#FAAC58',fill=False)
        ax.add_patch(forest)
        bridge = patches.Rectangle(xy=(-1.725 +0.5, 6.5 -0.5), width=1, height=1.5, ec='#FAAC58',fill=False)
        ax.add_patch(bridge)
        bri1 = patches.Circle(xy=(-1.725 +0.5, 6.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri1)
        bri2 = patches.Circle(xy=(-1.725 +0.5, 6.5+1.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri2)


        d = patches.Circle(xy=(-1*(1.225+ssp[0]),2+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(d)
        e = patches.Circle(xy=(-1*(1.225+ssp[0]),3.5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(e)
        f = patches.Circle(xy=(-1*(1.225+ssp[0]),5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(f)
        #'''
        ########################################################################
        ########################################################################
        ########################################################################
        plt.axis("equal")
        plt.grid(True)
        plt.show()
    def anime_ff(self, vx, vy, alfa):
        #'''#FF
        fig = plt.figure()
        ims = []
        X = []
        Y = []
        x=0
        y=0
        ssp=[-0.5,-0.5]
        #V = self.target.get_V()
        for index in np.arange(start=1, stop=len(vx)-1, step=1, dtype= int):
            x = x + vx[index] * self.dt
            y = y + vy[index] * self.dt
            X.append(x)
            Y.append(y)

            #vehi = np.matrix([[0.4, 0.4, -0.4, -0.4],[0.4, -0.4, -0.4, 0.4]])
            vehi = np.matrix([[0, 0.35, 0.35, -0.35, -0.35, 0],[0.7, 0.35, -0.35, -0.35, 0.35, 0.7]])
            Rot = np.matrix([[np.cos(-alfa[index]),-np.sin(-alfa[index])],[np.sin(-alfa[index]),np.cos(-alfa[index])]])
            STATE = [[x],[y]]
            newvehi = Rot * vehi + STATE
            img = plt.plot(X,Y,marker=".",color="#FAAC58") + plt.plot(newvehi[0,:],newvehi[1,:],marker="p",color="#FAAC58")

            plt.title("FF")
            #plt.title("V = {}m/s".format(V[index]))
            #print("V = {}m/s".format(V[index]))
            #plt.title("V = "+ str(V[index])[:4])
            plt.axis("equal")
            plt.grid(True)
            ims.append(img)
        plt.pause(1)
        ani = animation.ArtistAnimation(fig, ims, interval=1)
        ####
        ax = plt.axes()
        ############################     field     #############################
        ########################################################################
        sotowaku = patches.Rectangle(xy=(-13.3+0.5,-0.5), width=13.3, height=10, ec='#FAAC58',fill=False)
        ax.add_patch(sotowaku)
        forest = patches.Rectangle(xy=(-2.45+0.5,-0.5), width=2.45, height=8, ec='#FAAC58',fill=False)
        ax.add_patch(forest)
        bridge = patches.Rectangle(xy=(-1.725 +0.5, 6.5 -0.5), width=1, height=1.5, ec='#FAAC58',fill=False)
        ax.add_patch(bridge)
        bri1 = patches.Circle(xy=(-1.725 +0.5, 6.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri1)
        bri2 = patches.Circle(xy=(-1.725 +0.5, 6.5+1.5 -0.5), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(bri2)


        d = patches.Circle(xy=(-1*(1.225+ssp[0]),2+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(d)
        e = patches.Circle(xy=(-1*(1.225+ssp[0]),3.5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(e)
        f = patches.Circle(xy=(-1*(1.225+ssp[0]),5+ssp[1]), radius=0.08, ec='#FAAC58',fill=False)
        ax.add_patch(f)
        ########################################################################
        ########################################################################
        #'''
        plt.show()
