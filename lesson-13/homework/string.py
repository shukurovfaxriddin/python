1#
from datetime import datetime
from dateutil.relativedelta import relativedelta 

kun = int(input("Tug'ilgan kuningizni kiriting (1-31): "))
oy = int(input("Tug'ilgan oyingizni kiriting (1-12): "))
yil = int(input("Tug'ilgan yilingizni kiriting: "))

t_kun = datetime(yil, oy, kun)
hozir = datetime.today()

farq = relativedelta(hozir, t_kun)

print(f"Siz {farq.years} yil, {farq.months} oy, {farq.days} kun yashagansiz.")
#2
from datetime import datetime
from dateutil.relativedelta import relativedelta

kun = int(input("Tug‘ilgan kuningizni kiriting (1-31): "))
oy = int(input("Tug‘ilgan oyingizni kiriting (1-12): "))
yil = int(input("Tug‘ilgan yilingizni kiriting: "))

t_kun = datetime(yil, oy, kun)

bugun = datetime.today()

k_t_kun = datetime(bugun.year, oy, kun)

if k_t_kun < bugun:
    k_t_kun = datetime(bugun.year + 1, oy, kun)

farq = k_t_kun - bugun

print(f"Keyingi tug‘ilgan kuningiz: {k_t_kun.strftime('%Y-%m-%d')}")
print(f"Undan oldin {farq.days} kun qoldi.")
#3
from datetime import datetime,timedelta
meet_date = input("Suhbat kelishilgan shaqti(YYYY-MM-DD HH:MM formatda): ")
boshlanish_vaqti  = datetime.strptime(meet_date, "%Y-%m-%d %H:%M")

hour = int(input("Suhbat vaqti(soat): "))
min = int(input("Suhbat vaqti(minut): "))
time_meet = timedelta(hours=hour,minutes=min)
end = boshlanish_vaqti + time_meet
print(end)
#4
from datetime import datetime
import pytz

# 1. Sana va vaqtni kiriting
sana_vaqt = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
kirish_zona = input("Sizning vaqt zonangiz (masalan, Asia/Tashkent): ")
maqsad_zona = input("Qaysi zonaga o‘tkazmoqchisiz? (masalan, US/Eastern): ")

# 2. datetime formatga o‘tkazish
kirish_format = datetime.strptime(sana_vaqt, "%Y-%m-%d %H:%M")

# 3. Vaqt zonasini o‘rnatish
kirish_tz = pytz.timezone(kirish_zona)
maqsad_tz = pytz.timezone(maqsad_zona)

# 4. Naive datetime → aware datetime
aware_vaqt = kirish_tz.localize(kirish_format)

# 5. Konvertatsiya
natija_vaqt = aware_vaqt.astimezone(maqsad_tz)

# 6. Natijani chiqarish
print(f"{kirish_zona} vaqti: {aware_vaqt.strftime('%Y-%m-%d %H:%M')}")
print(f"{maqsad_zona} vaqti: {natija_vaqt.strftime('%Y-%m-%d %H:%M')}")
#5
from datetime import datetime
import time

future_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if future_time <= now:
        print("⏰ Vaqt tugadi!")
        break

    remaining = future_time - now

    days = remaining.days
    seconds = remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = (seconds % 60)

    print(f"⏳ {days} kun, {hours} soat, {minutes} minut, {sec} soniya qoldi.", end="\r")

    time.sleep(1)
#6
import re

email = input("Email manzilingizni kiriting: ")

# Oddiy email format regex
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("✅ Email manzili to'g'ri yozilgan.")
else:
    print("❌ Email manzili noto'g'ri.")
#7
import re

number = input("Telefon raqamni kiriting (10 ta raqam): ")

if re.fullmatch(r"\d{10}", number):
    formatted = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", number)
    print("Formatlangan raqam:", formatted)
else:
    print("❌ Noto‘g‘ri format! Iltimos, aynan 10 ta raqam kiriting.")
#7
import re
number = input("Telefon raqamni kiriting (faqat raqamlar): ")
area_code=''
first_part=''
second_part=''
if len(number) == 10:
    a = re.findall('.{1,3}', number)
    area_code=a[0]
    uniq = ""
    for char in number:
        if char not in area_code:
            uniq += char
    d=uniq[::-1]
    b,c = re.findall('.{1,4}', d)
    b=b[::-1]
    c=c[::-1]
else:
    print("❌ Noto‘g‘ri format! Iltimos, aynan 10 ta raqam kiriting.")
print(f"({area_code}){c}-{b}")


#8
import re
Login = input("Login: ")
Parol = input("Parol: ")
hato=[]

if len(Parol)<8 :
    hato.append(f"Sizning Parolingizda-{Parol}  kamida 8 ta belgi bo'lishi shart")
if not re.search(r"(?=.*[a-z])",Parol):
    hato.append(f"Sizning Parolingizda-{Parol}  kamida 1 kichik harif bo'lishi kerak")
if not re.search(r"(?=.*[A-Z])",Parol):
    hato.append(f"Sizning Parolingizda-{Parol}  kamida 1 katta harif bo'lishi kerak")
if not re.search(r"\d", Parol):
    hato.append(f"Sizning Parolingizda-{Parol}  kamida 1 raqam  bo'lishi kerak")
if not re.search(r"(?=.*[^a-zA-Z0-9])",Parol):
    hato.append(f"Sizning Parolingizda-{Parol}  kamida 1 mahsus belgi bo'lishi kerak")
if not hato:
    print(f"Sizning login - '{Login}' va parolingiz - '{Parol}' movfoqiyatli qo'shildi")
else:
    print("Sizning parolingizda quyidagi hatoliklar mavjut :")
    for err in hato:
        print(err)


#9
import re
print("Python is fun. Python is powerful. I love Python.")
word = input("Qaysi so‘zni qidiraylik? ")
text = "Python is fun. Python is powerful. I love Python."

# \b — so‘z chegarasi (faqat to‘liq so‘zlarni topadi)
matches = re.findall(rf"\b{re.escape(word)}\b", text, re.IGNORECASE)

print(f'"{word}" so‘zi {len(matches)} marta uchradi.')
# 10
import re

text = input("Matnni kiriting (sana bilan): ")

pattern = r"\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b"

dates = re.findall(pattern, text)

if dates:
    print("Topilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("Sana topilmadi.")
