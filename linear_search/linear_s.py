array=[1,2,3,4,5,6,7,8,9]
n=len(array)
x=10
def linearSearch(array, n, x):
	
	for i in range(0, n):
		if (array[i] == x):
			return i
	
z=linearSearch(array,n,x)
print(z)
