alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
T = int(input())



for t in range(T):
	string="A"
	input()
	blocks= list(map(int,input().split()))
	for i in range(len(blocks)):
		#case of increasing
		if (i%2==0):
			for j in range(blocks[i]):
				string+=alphabet[j+1]
		#case decreasing
		else:
			for k in range(blocks[i]-1,-1,-1):
				string+=alphabet[k]

	print(string)

	

for test in range(T):
    print(f"Case #{test+1}: {T}")



