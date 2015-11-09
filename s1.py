triangle = []
# read the data file
data_file = open("maxtriangle.txt", "r")
# for each line in the data file, append a row (list) to the triangle
for line in data_file:
   row = [int(i) for i in line.split(" ")] # convert the line to a list
   triangle.append(row)

print "First triangle",triangle
triangle2=triangle
# for each cell in the triangle, add the max of the cells below-left and
# below-right. the cell at the top will contain the greatest sum from bottom
# to top
stra=""
a=""
for i in range(len(triangle)-2,-1,-1):
	a=""
	for j in range(i+1):
		triangle[i][j] +=  max([triangle[i+1][j],triangle[i+1][j+1]])
		a=max([triangle[i+1][j],triangle[i+1][j+1]])
	stra += " + ",a
       #print max([triangle[i+1][j],triangle[i+1][j+1]])


print "maximum path: %d" % (triangle[0][0])
print stra

print "Second triangle",triangle