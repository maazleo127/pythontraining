ls=[14,24,34,44,52,61,78,87,98]
n=int(input('enter ur number'))
first=0
last=len(ls)-1
while first<=last:
    mid=(first+last)//2
    if ls[mid]==n:
        print('number is in',mid,'location')
        break
    elif ls[mid>n]:
        last=mid-1
    else:
        first=mid+1

if first>last:
    print('number not available')