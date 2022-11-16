import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl


def drawRectangle(center,size,angle,ax): 
    rectangle = patches.Rectangle((center[0],center[1]), size[0], size[1],color="black",angle=angle)
    ax.add_patch(rectangle)
    
    
def drawCar(center,length,width,wheelAngle,chasseyAngle = 0):
    # we either have a matrix of four angles or we delete them all
    if len(wheelAngle) != 2 or (len(wheelAngle[0]) != 2 or len(wheelAngle[1]) != 2):
        wheelAngle = np.array((([0,0]),([0,0])))
    

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    #draw chasis
    drawRectangle(center,np.array([width,length]),chasseyAngle,ax)

    plt.grid(True)
    plt.xlim([0,10])
    plt.ylim([0,10])
    plt.show()
    
