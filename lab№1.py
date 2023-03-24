# 1
a = [1, 2, 3, 4, 5]
print(a[0], a[2], a[-2])

#2
a=[1,2,3,4,5,6,7,8,9]
N=int(input())
if N<=len(a):
    print(a[N]**N)
else:
    print(-1)

# 3
a='xcvbnjh'
s='f'
k=0
for i in range (0, len(a)-1)
    if a[i]==s:
        k+=1
    if k==2:
        print(i)
        break

# 4
number = '101100110100'
number = number[::-1]
print(number)
count = 0
for n in number:
    if n == '0':
        count += 1
    else:
        break
print(count)

#5
n = input()[::-1]
print(n)

#6
b = [0, 0, 0, 0, 0]
b = input()
check = False
for i in range(0, len(b)-1):
    if b[i] == b[i+1]:
        check = True
    else:
        check = False
        break
print(check)

#7
password = input()
if password.isalnum() == False:
    print('Небезопасный пароль')
else:
    count_Upper = False
    count_Lower = False
    for symbol in password:
        if symbol == symbol.upper():
            count_Upper = True
        if symbol == symbol.lower():
            count_Upper = True
    if count_Upper or count_Lower == False:
        print('Небезопасный пароль')
    else:
        print('Безопасный пароль')

#8
l = [7, 4, 8, 2, [3, 1, 3, [7, 2]], 3, 9, [1, 2]]
def flatten(x):
    a = []
    for i in x:
        if isinstance(i, list):
            a.extend(flatten(i))
        else:
            a.append(i)
            return a
print (flatten(l))

#9


#10

