n,k=map(int,input().split())
n+=1
lis=[]
for j in range(n,k):
	i=2
	k=1
	while(i<j):
		if(j%i==0):
			k=0
			break
		else:
			i+=1
	if(k==1):
		lis.append(j)
for i in range(0,len(lis)):
	print(int(lis[i]),end=' ')
