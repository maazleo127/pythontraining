def insertion_s(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j]=arr[j],arr[j-1]
            j-=1

arr=[16,33,44,23,77,99,55]  #the program is running from 1 to -5 so its iteration
insertion_s(arr) #its from -1 and others and will get answer
print(arr)