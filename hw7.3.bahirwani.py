
inputfile = open('maxtriangle.txt')
InputNumbers = [[0]*100 for i in range(100)];
i=0
for line in inputfile:
	#print "line is ", line
	j=0
	for number in line.split():
		#print "number is ", number
		InputNumbers[i][j]=int(number)
		j+=1
	i+=1
	
# for i in range(100):
	# for j in range(100):
		# print InputNumbers[i][j]
	# print "\n"
	
	
TracingArray = [[0]*100 for i in range(100)]
for i in range(100):
	for j in range(100):
		TracingArray[i][j] = [InputNumbers[i][j],0]
	
# for i in range(100):
	# print TracingArray[3][i]
	# print "sum is ", InputNumbers[3][i]+sum(TracingArray[3][i])
	
for n in range(98,-1,-1):
	for k in range(0,n+1):
		#print (sum(TracingArray[n][k])+sum(TracingArray[n+1][k])) > (sum(TracingArray[n][k])+sum(TracingArray[n+1][k+1]))
		#print TracingArray[n+1][k]
		#if (InputNumbers[n][k]+sum(TracingArray[n+1][k])) > (InputNumbers[n][k]+sum(TracingArray[n+1][k+1])):
		
		if (sum(TracingArray[n][k])+sum(TracingArray[n+1][k])) > (sum(TracingArray[n][k])+sum(TracingArray[n+1][k+1])):
			# t=[InputNumbers[n][k],TracingArray[n+1][k]]
			# TracingArray[n][k]=[]
			# TracingArray[n][k].append(t)
			#TracingArray[n][k].append(TracingArray[n+1][k])
			for item in TracingArray[n+1][k]:
				TracingArray[n][k].append(item)
			#print "hello",TracingArray[n][k]
		else:
			# t=[InputNumbers[n][k],TracingArray[n+1][k+1]]
			# TracingArray[n][k]=[]
			# TracingArray[n][k].append(t)
			# TracingArray[n][k]=[TracingArray[n][k],t]
			for item in TracingArray[n+1][k+1]:
				TracingArray[n][k].append(item)
			#TracingArray[n][k].append(TracingArray[n+1][k+1])
			#print "hello again"
			#print "hello again",TracingArray[n][k]
# for i in range(5):
	# for j in range(5):
		# print TracingArray[i][j]
		
a=TracingArray[0][0]
while 0 in a:
	a.remove(0)
print "The path is as shown below:"
count=0
for item in a:
	if count<99:
		print item,"+",
	else:
		print item,
	count+=1
print " = ",sum(a)