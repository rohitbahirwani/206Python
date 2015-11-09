import string;
import sys;
arrayOfReversi=[]
DataTuple=()

for i in range(999, 100, -1):
	for j in range(999, 100, -1):
		currentNum=i*j
		#print "i= ",i, " j=",j," currentNum= ", currentNum, " stringNumber=",stringNumber;
		if str(currentNum) == str(currentNum)[::-1]:
			DataTuple=(currentNum,i,j)
			arrayOfReversi.append(DataTuple)
maxReversi = max(arrayOfReversi);
print "The max Reversi is found as: ",maxReversi[1]," * ",maxReversi[2]," = ",maxReversi[0]	