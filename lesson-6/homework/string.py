txt = input("Matn kiriting: ")

result = ""
count = 0
i = 0

while i < len(txt):
    result += txt[i]
    count += 1

    if count == 3:
        if i + 1 < len(txt):  
            if txt[i] not in 'aeiouAEIOU' and txt[i + 1] != '_':
                result += "_"
            else:
                if i + 1 < len(txt):
                    result += txt[i + 1] + "_"
                    i += 1  
        count = 0
    i += 1

if result.endswith("_"):
    result = result[:-1]

print(result)




n=int(input('son krit:'))

for i in range(n):
    print(i*i)



number = 1
while number <= 10:
    print(number)
    number += 1


rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()



n=int(input('son krit:'))
son=0
for i in range(1,n+1):
    son=son+i

print(f'Enter number {n}')
print(f'Sum is: {son}')







n = int(input("Son kiriting: "))

for i in range(1, 11):
    print(n * i)



n = int(input("Son kiriting: "))
son = 0

while n > 0:
    son += 1
    n = n // 10  

print(f'Output: {son}')






numbers = [12, 75, 150, 180, 145, 525, 50]

for items in numbers:
    if 75 <= items <=150 and items%5==0:
        print(items)





for i in range(5, 0, -1):          
    for j in range(i, 0, -1):     
        print(j, end=' ')
    print()  





list1 = [10, 20, 30, 40, 50]
for items in list1[::-1]:
        print(items)





for v in range(-10,0):
    print(v)



for v in range(0,10):
    if v==4:
        print(v)
        print('Done!')
        break
    print(v)







a=int(input('start num : '))
b=int(input('start num : '))
index=0
h=0
for num in range(a, b + 1):
    index = num
    for v in range(2, index):
        if index%v==0:
            h+=1   
    if h <= 2:
        print(index)



a = int(input('start: '))
b = int(input('end: '))

for num in range(a, b + 1):
    if num < 2:
        continue  
    h = 0
    for v in range(1, num + 1):
        if num % v == 0:
            h += 1
    if h == 2:  
        print(num)



a, b = 0, 1

n = 10

print("Fibonacci sequence:")

for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b  




n = int(input("Son kiriting: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")






list1 = list(input("Son kiriting: "))
list2 = list(input("Son kiriting: "))

result = []

for item in list1:
        if item not in list2:
            result.append(item)

for item in list2:
        if item not in list1:
            result.append(item)

print(result) 

