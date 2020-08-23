#! python 3
# table_printer.py - organise some data with each colum right-justified

# 1 find the longest string in each of the iner list
# 2 store the maximun width of each collumn as a list of integers
# 3 

tableData = [['apples','orange','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


newTable = {0:[], 1:[], 2:[], 3:[]}

for list in tableData:
    for i in range(len(list)):
        newTable[i].append(list[i]) 
        
longest = 0 
for key, value in newTable.items():
    lenght = len(''.join(value))
    if lenght > longest:
        longest = lenght
        
for key, value in newTable.items():
    print(' '*(longest - len(''.join(value)))+ ' '.join(value))

#colWidths = [0] * len(tableData)
#colWidths[1]
#while x < len(tableData[0]):               #Determine number of lists in list
    #while y < len(tableData):              #Determine number of lists
        #print(tableData[y][x], end=' ')     #Print each element on line
       # y += 1                        #Up Y by one each cycle until while stops
    #print('\n')                       #Move to a new line
  #  x += 1                            #Increase x by one and reset Y, restarts 
   # y = 0
