import sys
import math
import time
import math

class Point :
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

def Read_Points_From_Command_Line_File():
    points = []
    number_of_args = len(sys.argv)
    file = open(sys.argv[1],"r")
    
    for line in file:
        line.strip()
        x_y = line.split(" ")
        points.append(Point(float(x_y[0]),float(x_y[1])))

    return points
    
def Write_to_File(filename, s):
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')

list = Read_Points_From_Command_Line_File()


#*********************variables to be used in both*******************#
def Xsrt(Point):
    return Point.x

def Ysrt(Point):
    return Point.y

input_size_G = len(list)

sortByX = sorted(list, key = Xsrt)
sortByY = sorted(list, key = Ysrt)
#*********************************************************************#

#minimum = 10000;
def brute_force_minimum(input_size_G, list):
  if(input_size_G < 2):
    return 10000
  minimum = math.sqrt(((((list[0].x) - (list[1].x))**2) + (((list[0].y) - (list[1].y))**2)))
  #BRUTE FORCE
  for i in range(0, input_size_G - 2):
    for j in range(i+1, input_size_G - 1):
        if(math.sqrt(((((list[i].x) - (list[j].x))**2) + (((list[i].y) - (list[j].y))**2))) < minimum):
            minimum = math.sqrt(((((list[i].x) - (list[j].x))**2) + (((list[i].y) - (list[j].y))**2)))
        #print j
        ++j
    #print i
    ++i
  return minimum

#minimum_brute = brute_force_minimum(input_size_G, list)
#print minimum_brute
#*********************************************************#
#***http://www.tutorialspoint.com/python/time_clock.htm***#
#def procedure():
#    time.sleep(2.5)

#measure process time
#t0 = time.clock()
#brute_force_minimum(input_size_G, list)
#print time.clock() - t0, "brute_force seconds process time"

# measure wall time
#t0 = time.time()
#brute_force_minimum(input_size_G, list)
#print time.time() - t0, "brute_force seconds wall time"
#***http://www.tutorialspoint.com/python/time_clock.htm***#
#*********************************************************#



#**********************************************************#
def Extra(x_mid, distancehalf, MIDPOINT):
  innerX = []
  for i in range(0, input_size_G - 1):
    if((x_mid - distancehalf) > list[i].x) or ((x_mid + distancehalf) < (list[i].x)): 
      i = i
    else:
      innerX.append(list[i])
  #innerX.append(MIDPOINT)
  size_innerX = len(innerX)

  #print innerX
  minmid = brute_force_minimum(size_innerX, innerX)
  return minmid
#**********************************************************#
def outerMin(sortByX, input_size, list):
  if(input_size < 4):
    minimum_outer = math.sqrt(((((sortByX[0].x) - (sortByX[1].x))**2) + (((sortByX[0].y) - (sortByX[1].y))**2)))
    if(input_size == 3):
      min2 = math.sqrt(((((sortByX[0].x) - (sortByX[2].x))**2) + (((sortByX[0].y) - (sortByX[2].y))**2)))
      min3 = math.sqrt(((((sortByX[1].x) - (sortByX[2].x))**2) + (((sortByX[1].y) - (sortByX[2].y))**2)))
      if((min2 < minimum_outer) and (min2 < min3) ):
        minimum_outer = min2
      if((min3 < minimum_outer) and (min3 < min2)):
        minimum_outer = min3
    return minimum_outer
    

  left = []
  right = []
  #midpoint based on x
  x_mid = sortByX[input_size/2].x
  #print x_mid
  
  #print sortByX
  #left/right
  for i in range(0, (input_size/2)):          #no mid point included, yet
    left.append(sortByX[i])
  for i in range((input_size/2), input_size):  #midpoint included
    right.append(sortByX[i])
    
    
  left_size = len(left)
  right_size = len(right)


  left_min = outerMin(left, left_size, list)
  right_min = outerMin(right, right_size, list)

  min_L_R_distance = left_min;
  if(right_min < min_L_R_distance):
    min_L_R_distance = right_min 
  
  return min_L_R_distance
  
  
  
  
  
  
  
#**********************************************************#  
#**********************************************************#  
#**********************************************************#  
def NN():
  min_L_R_distance = outerMin(sortByX, input_size_G, list)
  #print min_L_R_distance
  distancehalf = min_L_R_distance
  finalDistance = distancehalf
  
  
  x_mid = sortByX[input_size_G/2].x
  MIDPOINT = sortByX[input_size_G/2]
  distancemiddle = Extra(x_mid, distancehalf, MIDPOINT)
  
  if(distancemiddle < finalDistance):
    finalDistance = distancemiddle
  
  #print " *** "
  #print distancemiddle

  return finalDistance
#**********************************************************#  
#**********************************************************#  
#********************#END HERE#****************************#





finalDistance = NN()
print "finalDistance DIVIDE AND CONQUER"
print finalDistance
finalDistance = brute_force_minimum(input_size_G, list)
print "finalDistance BRUTE FORCE"
print finalDistance
#*********************************************************#
#***http://www.tutorialspoint.com/python/time_clock.htm***#
def procedure():
    time.sleep(2.5)

#measure process time
t0 = time.clock()
#brute_force_minimum(list)
NN()
print time.clock() - t0, "divide and conquer process time"

# measure wall time
#t0 = time.time()
#brute_force_minimum(list)
#NN()
#print time.time() - t0, "divide and conquer wall"
#***http://www.tutorialspoint.com/python/time_clock.htm***#
#*********************************************************#


Write_to_File(sys.argv[1] + "_distance.txt", finalDistance)
