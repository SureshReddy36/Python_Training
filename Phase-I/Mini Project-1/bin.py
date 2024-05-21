def peakelement(arr,n):
    start=0
    end=n-1
    while(start<=end):
        mid=start+end-start//2
        if (arr[mid]>=arr[mid-1]) and (arr[mid]>=arr[mid+1]):
            return arr[mid]
        elif arr[mid]<arr[mid-1]:
            end=mid-1
        else:
            start=mid+1
    return -1
n=int(input("Enter the length of the list :"))
arr=list(int,input().split())
print("Enter the elements to be inserted into the list:")
#for i in range(n):
    #arr.append(int(input()))
peak=peakelement(arr,n)
print("The peak element:",peak)