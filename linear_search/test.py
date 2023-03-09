# # # # x={True:'maaz'}
# # # # print(x)
# # # dict={}
# # # # print(type(dict))
# # # set=()
# # # # print(type(set))
# # # list_one = ['January', 'February', 'March']

# # # # use the extend method 
# # # list_one.extend(['April', 'May', 'June'])

# # # # displaying the list
# # # print(list_one)

# # # # Let's write a program in Python to understand
# # # # difference between the two discussed methods

# # # # the first step would be assigning two lists
# # list_one = [2, 3, 4]
# # list_two = [2, 3, 4]

# # x = [5, 6]

# # # use the two different methods
# # list_one.append(x)
# # list_two.extend(x)

# # # displaying the lists using the print statement.
# # print(list_one)
# # #printing the second list
# # print(list_two)
# num=complex(1,5)
# print(num)

for i in range(1,11):  #outerloop
    for j in range(1,11): #inner loop
        print(i*j,end=" , ")
    print() #outer loop
    