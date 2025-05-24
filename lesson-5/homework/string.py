def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

is_leap(2024)
is_leap(1900)
is_leap(2000)
is_leap(2023) 




son = int(input('Son kiriting: '))
if son%2!=0:
    print('Weird')
elif son%2==0 and 2 <= son <= 5:
    print('NOT Weird')
elif son%2==0 and 6 <= son <= 20:
    print('Weird')
elif son%2==0 and son > 20:
    print('Not Weird')



a = int(input("a = "))
b = int(input("b = "))

if a > b:
    a, b = b, a

if a % 2 != 0:
    a += 1  

print(list(range(a, b + 1, 2)))
