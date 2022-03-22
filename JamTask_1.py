T = int(input())

array=[]

for t in range(T):
	input()
	temp=0
	food=0
	arr=[]
	inp = sorted(list(map(int,input().split())))
	for i in inp:
		if (i>temp):
			food+=1
			arr.append(food)
		else:
			arr.append(food)
		temp=i
	array.append(sum(arr))

for test in range(T):
    print(f"Case #{test+1}: {array[test]}")



