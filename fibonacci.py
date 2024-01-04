def fibonacci(n):
	a = 0
	b = 1
	if n <= 0:
		print("This is not a Positive Number")
	for i in range(n):
		print(a)
		c = a + b
		a = b
		b = c
n = int(input())
fibonacci(n)
		