#方法一
for i in range(2,100):
	if i==2:
		print(i)
		continue
	for l in range(2,i):
		if i%l==0:
			break
	else:
		print(i)
		
print("====================================================")		
#方法二：优化算法
for i in range(2,100):
	if i==2:
		print(i)
		continue
	for l in range(2,int(i**0.5)+1):
		if i%l==0:
			break
	else:
		print(i)
		
#判断是否为质数的函数
def is_prime(n):
	if n<2:
		return False
	if i==2:
		return True
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	else:
		return True
