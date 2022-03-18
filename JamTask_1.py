T = int(input())

array=[]

for t in range(T):
	input()
	temp=0
	tmp=0
	arr=[]
	inp = sorted(list(map(int,input().split())))
	for i in inp:
		if (i>tmp):
			tmp=i
			temp+=1
			arr.append(temp)
		else:
			arr.append(temp)
	array.append(sum(arr))

for test in range(T):
    print(f"Case #{test+1}: {array[test]}")



