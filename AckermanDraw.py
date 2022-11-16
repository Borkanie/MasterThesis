import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import math

def drawRectangle(center,size,angle,ax,color="black"): 
    rectangle = patches.Rectangle((center[0],center[1]), size[0], size[1],color=color,angle=angle)
    ax.add_patch(rectangle)
    
    
def drawCar(center,length,width,wheelAngle,chasseyAngle = 0):
    # we either have a matrix of four angles or we delete them all
    if len(wheelAngle) != 2 or (len(wheelAngle[0]) != 2 or len(wheelAngle[1]) != 2):
        wheelAngle = np.array((([0,0]),([0,0])))
    

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    #draw chasis
    chasisDiag = math.sqrt(width ** 2 + length ** 2)
    radius = chasisDiag/2
    chasisCenter=np.array([center[0]+radius*math.cos(chasseyAngle+45),center[1]+radius*math.sin(chasseyAngle+45)])
    drawRectangle(center,np.array([width,length]),chasseyAngle,ax)

    #draw wheel
    chasisWidth = width * math.cos(chasseyAngle)
    chasislength = length * math.cos(chasseyAngle)
    chassDegAngle = chasseyAngle *math.pi/180
    #front left
    offset = np.array([1.2+(chasisDiag-0.1)*math.cos(chassDegAngle+math.pi*3/4)/2,
                       (chasisDiag-0.5)*math.sin(chassDegAngle+math.pi*3/4)/2])
    wheelCenter = chasisCenter + offset
    drawRectangle(wheelCenter,np.array([width/10,length/10]),chasseyAngle+wheelAngle[0][0],ax,"red")
    
    #front right
    wheelCenter = np.array([chasisCenter[0]+chasisWidth*3/8,center[1]+chasislength*3/8])
    drawRectangle(wheelCenter,np.array([width/10,length/10]),chasseyAngle+wheelAngle[0][1],ax,"blue")
    
    #back left
    wheelCenter = np.array([center[0]-chasisWidth*3/8,center[1]-chasislength*3/8])
    drawRectangle(wheelCenter,np.array([width/10,length/10]),chasseyAngle+wheelAngle[1][0],ax,"green")
    
    #back right
    wheelCenter = np.array([chasisCenter[0]+chasisWidth*3/8,center[1]-chasislength*3/8])
    drawRectangle(wheelCenter,np.array([width/10,length/10]),chasseyAngle+wheelAngle[1][1],ax,"yellow")
    
    plt.grid(True)
    plt.xlim([-5,5])
    plt.ylim([-5,5])
    plt.show()
    
drawCar(np.array([0,0]),4,2,np.array(([15,15],[0,0])),chasseyAngle=45)