def oneoddoccuring(arr):
    result=0
    for element in arr:
        result=result^element
    return result


arr=[]
n=int(input("How many elements do you want? "))
while(n):
    num=int(input("Enter a number: "))
    arr.append(num)
    n-=1

print("The oddoccuring number is", oneoddoccuring(arr))