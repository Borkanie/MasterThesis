import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import math

def drawRectangle(center,size,angle,ax,color="black"): 
    rectangle = patches.Rectangle((center[0],center[1]), size[0], size[1],color=color,angle=angle)
    ax.add_patch(rectangle)

def RotateArray(rotateArrayWIthAngle,angleDegrees):
    matrix = np.array([rotateArrayWIthAngle[0]*math.cos(angleDegrees)+rotateArrayWIthAngle[1]*math.sin(angleDegrees)
                        ,-rotateArrayWIthAngle[0]*math.sin(angleDegrees)+rotateArrayWIthAngle[1]*math.cos(angleDegrees)])
    return matrix

def drawCar(center,length,width,wheelAngle,chasseyAngle = 0):
    # we either have a matrix of four angles or we delete them all
    if len(wheelAngle) != 2 or (len(wheelAngle[0]) != 2 or len(wheelAngle[1]) != 2):
        wheelAngle = np.array((([0,0]),([0,0])))
    

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    #draw chasis
    drawRectangle(center,np.array([width,length]),chasseyAngle,ax)

    #draw wheel
    chassDegAngle = -chasseyAngle *math.pi/180

    #front left
    drawRectangle(center+RotateArray(np.array([width*1/8,length*7/8]),chassDegAngle),np.array([width/10,length/10]),chasseyAngle+wheelAngle[0][0],ax,"red")

    #front right
    drawRectangle(center+RotateArray(np.array([width*7/8,length*7/8]),chassDegAngle),np.array([width/10,length/10]),chasseyAngle+wheelAngle[0][1],ax,"blue")

    #back left
    drawRectangle(center+RotateArray(np.array([width*1/8,length*1/8]),chassDegAngle),np.array([width/10,length/10]),chasseyAngle+wheelAngle[1][0],ax,"green")

    #back right
    drawRectangle(center+RotateArray(np.array([width*7/8,length*1/8]),chassDegAngle),np.array([width/10,length/10]),chasseyAngle+wheelAngle[1][1],ax,"yellow")

    plt.grid(True)
    size = np.array([width,length])
    plt.xlim([-(size.max()+center.max()),size.max()+center.max()])
    plt.ylim([-(size.max()+center.max()),size.max()+center.max()])
    plt.show()
