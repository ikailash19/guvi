n=int(input())
for i in range(n):
	if 2**i==n:
		print("yes")
		exit()
print("no")
