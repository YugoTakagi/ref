import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class integrate_number(object):
    """docstring for arrange_the_point."""
    maxmum_interval = 0
    minmumInterval = 0
    def __init__(self):
        pass
    def integrate(self, X, TVP_of_S):
        #print('----------start integrate number-----------')
        ARRANGE_INDEXS = []
        sum_s = 0.0
        index_of_tvp = 0
        ds_befor=0

        before_x = X[0]
        before_y = X[1]
        x_start  = X[2]
        for index in np.arange(0, len(before_x), 1):
            if (index-1) < 0:
                #dx = before_x[index]
                #dy = before_y[index]
                #ds = np.sqrt(dx**2 + dy**2)
                ds = x_start
            else:
                dx = before_x[index] - before_x[index-1]
                dy = before_y[index] - before_y[index-1]
                ds = np.sqrt(dx**2 + dy**2)
            sum_s = sum_s + ds
            ds_befor = ds
            if sum_s >= TVP_of_S[index_of_tvp]:
                #print("sum[{}] , s[{}] = {} , {}".format(index, index_of_tvp, sum_s, TVP_of_S[index_of_tvp]))
                ARRANGE_INDEXS.append(index)
                index_of_tvp += 1
                if len(ARRANGE_INDEXS) == len(TVP_of_S):
                        #print("2> integrate fin")
                        break
        print("integrate({}): {} -> {}".format(len(TVP_of_S),len(before_x),len(ARRANGE_INDEXS)))
        #print('-------------------------------------------')
        return ARRANGE_INDEXS, len(ARRANGE_INDEXS)
    def arrange_test(self, before_x, before_y, TVP_of_S):
        INDEX = []
        SUM = []
        print('+--+-start arrange-+--+')
        while True:
            while True:
                dx = before_x[self.index] - before_x[self.index-1]
                dy = before_y[self.index] - before_y[self.index-1]
                ds = np.sqrt(dx**2 + dy**2)
                self.sum_s_before = self.sum_s
                self.sum_s = self.sum_s_before + ds
                INDEX.append(self.index)
                SUM.append(self.sum_s)
                if self.sum_s >= TVP_of_S[self.index_of_tvp]:
                    if abs(TVP_of_S[self.index_of_tvp]-self.sum_s) <= abs(TVP_of_S[self.index_of_tvp]-self.sum_s_before):
                        self.ARRANGE_INDEXS.append(self.index)
                        break
                    elif abs(TVP_of_S[self.index_of_tvp]-self.sum_s) > abs(TVP_of_S[self.index_of_tvp]-self.sum_s_before):
                        self.ARRANGE_INDEXS.append(self.index-1)
                        #if self.index-1>0:
                        self.index = self.index-1
                        break
                    else:
                        print("Help me!!")
                        break
                else:
                    if self.index + 1 == len(before_x):
                        break
                    else:
                        self.index += 1
            if self.index_of_tvp + 1 == len(TVP_of_S):
                break
            else:
                self.index_of_tvp += 1



        plt.plot(INDEX,SUM, marker=".", color="#B40404")
        plt.title("arrange sum-index")
        plt.grid(True)
        plt.show()

        print(self.ARRANGE_INDEXS)
        print('len(TVP_of_S) = {}'.format(len(TVP_of_S)))
        print('len(before_x) = {}'.format(len(before_x)))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
    def maximumInterval(self, TVP_of_S):
        INDEX_OF_TVPS = np.arange(start=0.0, stop=len(TVP_of_S)-1, step=1, dtype= int)
        for index in INDEX_OF_TVPS:
            if (index-1) <= 0:
                self.maxmum_interval = TVP_of_S[index]
            else:
                interval = TVP_of_S[index] - TVP_of_S[index-1]
                if self.maxmum_interval<interval:
                    self.maxmum_interval = interval
                else:
                    pass
        print('self.maxmum_interval = {}'.format(self.maxmum_interval))
    def minmumInterval(self, TVP_of_S):
        INDEX_OF_TVPS = np.arange(start=0.0, stop=len(TVP_of_S)-1, step=1, dtype= int)
        for index in INDEX_OF_TVPS:
            if (index-1) <= 0:
                self.minmum_interval = TVP_of_S[index]
            else:
                interval = TVP_of_S[index] - TVP_of_S[index-1]
                if self.minmum_interval>interval:
                    self.minmum_interval = interval
                else:
                    pass
        print('self.minmum_interval = {}'.format(self.minmum_interval))
