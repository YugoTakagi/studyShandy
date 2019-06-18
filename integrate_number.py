import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class IntegrateNumberClass(object):
    """docstring for arrange_the_point
    This class can integrate number of points.
    """
    def __init__(self, X, smoothLocAraay, x_start):
        self.maxmum_interval = 0
        self.minmumInterval = 0

        self.before_x = X.T[0]
        self.before_y = X.T[1]
        self.xs  = x_start
        self.slarray = smoothLocAraay
    def integrate(self):
        #print('----------start integrate number-----------')
        ARRANGE_INDEXS = []
        sum_s = 0.0
        index_of_tvp = 0
        ds_befor=0
        for index in np.arange(0, len(self.before_x), 1):
            if (index-1) < 0:
                ds = self.xs
            else:
                dx = self.before_x[index] - self.before_x[index-1]
                dy = self.before_y[index] - self.before_y[index-1]
                ds = np.sqrt(dx**2 + dy**2)
            sum_s = sum_s + ds
            ds_befor = ds
            if sum_s >= self.slarray[index_of_tvp]:
                ARRANGE_INDEXS.append(index)
                index_of_tvp += 1
                if len(ARRANGE_INDEXS) == len(self.slarray):
                    # print("> integrate fin")
                    break
        print(">> integrate({}): {} -> {}".format(len(self.slarray),len(self.before_x),len(ARRANGE_INDEXS)))
        #print('-------------------------------------------')
        return ARRANGE_INDEXS, len(ARRANGE_INDEXS)
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
    def new_plt(self, list_of_bezier, new_index_for_bezier, len_new_index_for_bezier):
        newArray = []
        for ind in np.arange(start=0, stop=len_new_index_for_bezier, step=1, dtype= int):
            newArray.append(list_of_bezier[new_index_for_bezier[ind]])
        newNpArray = np.array(newArray)

        plt.plot(newNpArray.T[0], newNpArray.T[1], marker=".")
        plt.axis("equal")
        plt.grid(True)
        plt.title("new curve")
        plt.show()

        return newNpArray, newArray
