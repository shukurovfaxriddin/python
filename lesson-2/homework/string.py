matn=input('Matin kriting :')
print(matn[::-1])


txt = "I'am John. I am from London"
residence = txt.split("from")[1].strip()

print("Javob:", residence)


txt = 'MsaatmiazD'

txt[0:20:2]
txt[-1:-20:-2]


ism=(input('Ismingizni kriting : ' ))
yosh=int(input('Tug\'ulgan yilni kriting : ' ))

print(f'{ism} siz {2025-yosh} yoshdasiz')


txt = 'LMaasleitbtui'

txt[0:20:2]
txt[1:20:2]


matn=input('Matin kriting :')
a=matn.count('a')
e=matn.count('e',)
i=matn.count('i')
o=matn.count('o')
u=matn.count('u')
A1=matn.count('A')
E1=matn.count('E',)
I1=matn.count('I')
O1=matn.count('O')
U1=matn.count('U')
sum=a+e+i+o+u+A1+E1+I1+O1+U1
print('Unli hariflar soni: ',sum)


raqamlar = input("Sonlarni vergul bilan kiriting ; ")

raqamlar = list(map(int, raqamlar.split(',')))

eng_katta = max(raqamlar)

print("Eng katta son:", eng_katta)


soz = input("So‘z kiriting: ").lower()  # Barcha harflarni kichik qiladi

if soz == soz[::-1]:
    print("Bu so‘z palindrom.")
else:
    print("Bu so‘z palindrom emas.")


# 1. Foydalanuvchidan email manzilini olish
email = input("Email manzilni kiriting: ")

# 2. '@' belgisi bo'yicha bo'lish
parts = email.split('@')

# 3. Domenni ajratish va chiqarish
if len(parts) == 2:
    domain = parts[1]
    print("Domain:", domain)
else:
    print("Noto‘g‘ri email manzil kiritildi.")


import random
import string

try:
    length = int(input("Parol uzunligini kiriting (kamida 6): "))
    if length < 6:
        print("Parol juda qisqa! Minimal uzunlik 6 ta belgi.")
    else:
        # 2. Belgilar to‘plamlari
        letters = string.ascii_letters    
        digits = string.digits             
        symbols = string.punctuation     
