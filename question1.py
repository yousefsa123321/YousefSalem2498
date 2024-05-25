#A
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

d = {L1[i]: L2[i] for i in range(len(L1))}
print(d)

#B
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)

#C
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:
    if item.startswith('B'):
        print(item)
#DNS
d = {i: i+1 for i in range(11)}
print(d)
