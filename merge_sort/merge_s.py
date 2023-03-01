
def mergesort(a,s,e):            #a is list s is starting and e is ending
    if s<e:
        m=(s+(e-1))//2
        mergesort(a,s,m)
        mergesort(a,m+1,e)
        merge(a,s,m,e)
def merge(a,s,m,e):
    n1=m-s+1
    n2=e-m
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        L[i]=a[s+i]
    for j in range(0,n2):
        R[j]=a[m+1+j]
    i=0
    j=0
    k=s
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        a[k]=L[i]
        i +=1
        k +=1
    while j<n2:
        a[k]=R[j]
        j +=s
        k +=1

num=[66 ,55, 44, 33 ,22 ,11 ]
n=len(num)
mergesort(num,0,n-1)   #zero position last position
for i in range(len(num)):
    print(num(i),end=' ')