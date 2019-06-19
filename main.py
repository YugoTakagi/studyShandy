from BezierCurve import BezierClass
from smoothAcceleration import SmoothAccelerationClass
from integrate_number import IntegrateNumberClass
import numpy as np

def main():#main function
    #####__making curve__#######################################################
    bc = BezierClass(points = 1000)
    BEZIER_ANCER = np.array([[0,0],[0.0,1.4],[-1.43,0.1],[-1.43,1.5]], dtype=np.float)
    BEZIER = bc.bezier_making(BEZIER_ANCER, 3)
    ############################################################################


    #####__making smooth accel__################################################
    a = [2.0,0,-2.0]
    x_start = 0.0
    # def __init__(self, a(array), vel_want, vel_start, vel_end, curve, x_start, time_start)
    sacc = SmoothAccelerationClass(a,1.3,0.0,0.0,BEZIER,x_start,0.0)
    arrayAcc, arrayVel, arrayLoc = sacc.design()
    ############################################################################


    #####__integrate number of points__#########################################
    # def __init__(self, X(array), TVP_of_S, x_start):
    ign = IntegrateNumberClass(BEZIER, arrayLoc, x_start)
    indexs, lenInd = ign.integrate()
    newNpArray, newArray = ign.new_plt(BEZIER,indexs,lenInd)
    ############################################################################

if __name__ == '__main__':
    main()#run main function.
