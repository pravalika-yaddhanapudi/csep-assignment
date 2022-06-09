def myfunc(arr, low, high, x):
	if high >= low:

		mid = low+ (high - low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return myfunc(arr, low, mid-1, x)
		else:
			return myfunc(arr, mid + 1, high, x)

	else:
		return -1

arr=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   l=int(input())
   arr.append(l)
print(arr)
x=int(input("enter element which we want"))


result = myfunc(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index % d" % result)
else:
	print("Element is not present in array")

