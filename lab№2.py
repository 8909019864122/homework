#1
def fibonacci(i):
    if i in (1,2):
        return 1
    return fibonacci(i-1) + fibonacci(i-2)
print(fibonacci(6))

#2
def remove_common(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i)
    print('Список 1 : ', a)
    print('Список 2 : ', b)

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    b = [4,5,6,7,8,9]
    remove_common(a, b)

#3
a = [1,2,3,3,3,3,3]
for i in a:
    if a.count(i)<3:
        a.remove(i)
print(len(a), a)

#4
def sum(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total  + sum(element)
        else:
            total = total + element
    return total
print('Сумма элементов равна:', sum([[1,2],[3,4]]))

#5
def sequence(lst):
    temp, save = [], []
    for i in range(len(lst) - 1):
        if lst[i + 1] == lst[i] + 1:
            temp.append(lst[i]) if temp == [] else temp
            temp.append(lst[i + 1])
            if save <= temp:
                save = temp
        else:
            temp = []
    return save

sequence([1, 2, 3, 2, 4, 5, 6, 7])

#6
text = input()
count = [i for i in range(len(text))]
print(''.join(text[i].upper() if (i%2 != 0) else text[i] for i in count))

#7
n = int(input())
for i in range(1, n+1,2):
    if i==1:
        print('' * 3, '*' * i)
    elif i == 3:
        print('' * 2, '*' * i)
    else:
        print('', '*' * i)

for i in range(n-2, 0, -2):
    if i==3:
        print(''*2, '*' * i)
    else:
        print('' * 3, '*' * i)

#8
def matrix(num):
    mat = [[0 for i in range(num)] for j in range(num)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == 0 or j == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end='')
        print()
matrix(5)

#9
num = '55 68 74'
print(f'{sum(map(float, num.split())):g}')

#10
