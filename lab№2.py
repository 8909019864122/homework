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
w = n*2-1
a = [ ]

for y in range(w):
   a.append([])
   for x in range(w):
       d = n - abs(x+1-n) - abs(y+1-n)
       a[y].append( '*' if d > 0 else " ")

for l in a:
    print(*l,sep='')

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
            print(mat[i][j]," ", end='')
        print( sep=", ")
matrix(5)


#9
def findSum(str1):
    temp = '0'
    Sum = 0

    for c in str1:
        if (c.isdigit()):
            temp += c
        else:
            Sum += int(temp)
            temp = '0'
    return Sum + int(temp)
str1 = '54 мрм5 56'
print(findSum(str1))

#10
import re
def string_sum(text):
    temp = []
    result = []
    keys, values = range(48, 58), range(0, 10)
    nums = dict(zip(keys, values))

    for i in re.findall('\d+', text):
        for j in i:
            if ord(j) in nums:
                temp.append(nums[ord(j)])
        temp = sum(10 ** i[0] * i[1] for i in enumerate(reversed(temp)))
        result.append(temp)
        temp = []
    return sum(result)

string_sum('175 конфет и 84 леденца')
