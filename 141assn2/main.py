import sys
import math
import time
import math

#class Point :
#    def __init__(self, x_val, y_val):
#        self.x = x_val
#        self.y = y_val
#
#    def __repr__(self):
#        return "(%.2f, %.2f)" % (self.x, self.y)
####input from last assn####
def Read_floats_From_Command_Line_File():
    floats = []
    number_of_args = len(sys.argv)
    file = open(sys.argv[1],"r")
    rowindex = -1;    
    for line in file:
    	rowindex = rowindex + 1
        line = line.strip()
        num  = line.split(", ")
        if line[0] == 0:
          return floats;
       	floats.append([])
	for i in range (0, len(num)):
          	floats[rowindex].append(float(num[i]))

    #print floats
    return floats
    
def Write_to_File(filename, s):
    output = open(filename ,'w')
    output.write(str(s))
    output.write('\n')

#list = Read_floats_From_Command_Line_File()
####input from last assn####


def main(input):
  #final = []
  for rowSize in range(0, len(input[0])):
    rowSize = rowSize + 1
  for columnSize in range(0, len(input)):
    columnSize = columnSize + 1
  
  carving = []
  for i in range(0, rowSize):
    carving.append([])
    for j in range(0, columnSize):
      carving[i].append(1000000000)
        

  for i in range(0, columnSize):
    carving[0][i] = input[0][i]
	
  
  
  for row in range(0, rowSize - 1):
		for column in range(0, columnSize - 1):
			curr = carving[row][column]
			if(column - 1 >= 0):
				BLgood = 1
			else: 
				BLgood = 0
			if(column + 1 < columnSize):
				BRgood = 1
			else:
				BRgood = 0
			BMgood = 1 


			if(BLgood == 1):
				BL = curr + input[row + 1][column - 1]
			else: 
				BL = 1000000
			#print BLgood 
			if(BRgood == 1):
				BR = curr + input[row + 1][column + 1]
			else:
				BR = 1000000
			if(BMgood == 1):
				BM = curr + input[row + 1][column + 0]
			else:
				BM = 1000000


			Min = BL
			if((BR < BL) and (BR < BM)):
				Min = BR
			if((BM < BL) and (BM < BR)):
				Min = BM

					
			if((BLgood == 1) and (BL < carving[row + 1][column - 1])):
				carving[row + 1][column - 1] = BL
			if((BMgood == 1) and (BM < carving[row + 1][column + 0])):
				carving[row + 1][column + 0] = BM
			if((BRgood == 1) and (BR < carving[row + 1][column + 1])):
				carving[row + 1][column + 1] = BR

	

  Min = 1000000
  minColIndex = 0;
  #carving[rowSize - 1][2] = 10
  for i in range(0, columnSize - 1):
  	if(carving[rowSize - 1][i] < Min):
  		minColIndex = i
  		Min = carving[rowSize - 1][i]
      
#now start from the bottom go up until you find the way back.      
  #print carving						
  #print Min
  #print minColIndex
  small = 1000000000
  currIndex = minColIndex
  newRow = 0;
  DRow = 0;            #current row
  ORow = rowSize - 1   #old row, input row
  back = []
  #back.append([])
  back.append([])
  back[DRow].append(ORow)
  back[DRow].append(minColIndex)
  back[DRow].append(input[ORow][currIndex])
  DRow = ORow
  #DRow = rowSize - 1
  for DRow in range(rowSize - 2, -1, -1):
    #ORow = ORow - 1
    #print DRow
    if(currIndex - 1 >= 0):
      TLgood = 1
    else: 
      TLgood = 0
    if(currIndex + 1 < columnSize):
      TRgood = 1
    else:
      TRgood = 0
    TMgood = 1
      
      
    if(TLgood == 1):
      TL = input[DRow][currIndex - 1]
    else: 
			TL = 1000000000
		#print BLgood 
    if(TRgood == 1):
      TR = input[DRow][currIndex + 1]
    else:
      TR = 1000000000
    if(BMgood == 1):
      TM = input[DRow][currIndex + 0]
    else:
      TM = 1000000000


    small = TL
    #currIndex = currIndex - 1
    if((TR < TL) and (TR < TM)):
      small = TR
      currIndex = currIndex + 1
    if((TM < TL) and (TM < TR)):
      small = TM
      currIndex = currIndex
    if(TL == small):
      currIndex = currIndex - 1
      
    back.append([])
    #print DRow
    #print newRow
    back[newRow].append(DRow)
    back[newRow].append(currIndex)
    back[newRow].append(input[DRow][currIndex]) 
    
  
#def output(back, Min):
  #print back[0][3]
  #print len(back)
  string = ""
  string += "Min stream: "
  string += str(Min)
  string += "\n"
  string += "["
  index = 3
  last = ((rowSize) * index)
  for pos in range(1, last + 1):
    string += str(back[0][pos - 1])
    string += " "
    if((pos % 3 == 0) and (pos > 1)):
      string += "]"
      string += "\n"
    #if(pos % 4 == 0):
      string += "["
    Write_to_File(sys.argv[1] + "_trace.txt", string)

  #return rowSize;


stuff = Read_floats_From_Command_Line_File()
main(stuff)
#output(back)
