import math

T=int(input())
def get_answer(string,K):

	score=0
	for i in range(math.floor(len(string)/2)):
		if (string[i]!=string[-(i+1)]):
			score+=1
	return abs(score-K)



for test in range(T):
	N,K=map(int,input().split())
	string=input()
	print(f"Case #{test+1}: { get_answer(string,K)}")

