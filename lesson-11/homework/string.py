annotated-types==0.7.0
anyio==4.9.0
asttokens==3.0.0
certifi==2025.4.26
charset-normalizer==3.4.2
colorama==0.4.6
comm==0.2.2
contourpy==1.3.2
cycler==0.12.1
debugpy==1.8.14
decorator==5.2.1
distro==1.9.0
executing==2.2.0
fonttools==4.58.2
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
ipykernel==6.29.5
ipython==9.2.0
ipython_pygments_lexers==1.1.1
jedi==0.19.2
jiter==0.10.0
jupyter_client==8.6.3
jupyter_core==5.7.2
kiwisolver==1.4.8
matplotlib==3.10.3
matplotlib-inline==0.1.7
nest-asyncio==1.6.0
numpy==2.3.0
openai==1.82.0
packaging==25.0
pandas==2.3.0
parso==0.8.4
pillow==11.2.1
platformdirs==4.3.8
prompt_toolkit==3.0.51
psutil==7.0.0
pure_eval==0.2.3
pydantic==2.11.5
pydantic_core==2.33.2
Pygments==2.19.1
pyparsing==3.2.3
python-dateutil==2.9.0.post0
pytz==2025.2
pywin32==310
pyzmq==26.4.0
requests==2.32.4
six==1.17.0
sniffio==1.3.1
stack-data==0.6.3
tornado==6.4.2
tqdm==4.67.1
traitlets==5.14.3
typing-inspection==0.4.1
typing_extensions==4.13.2
tzdata==2025.2
urllib3==2.4.0
wcwidth==0.2.13

#1. Virtual muhitni yaratish
python -m venv myenv
# 2. Virtual muhitni faollashtirish (aktivatsiya qilish)
myenv\Scripts\activate
# 3. Python paketlarini o‘rnatish
pip install requests
pip install pandas
pip install matplotlib
# 4. O‘rnatilgan kutubxonalarni tekshirish
pip list
# 5. requirements.txt faylini yaratish (ixtiyoriy)
pip freeze > requirements.txt

####2
# math_operations.py

def add(a, b):
    """Ikki sonni qo‘shish"""
    return a + b

def subtract(a, b):
    """Ikki sonni ayirish"""
    return a - b

def multiply(a, b):
    """Ikki sonni ko‘paytirish"""
    return a * b

def divide(a, b):
    """Ikki sonni bo‘lish"""
    if b == 0:
        return "Nolga bo‘lish mumkin emas"
    return a / b


# string_utils.py

def reverse_string(s):
    """Matnni teskariga aylantirish"""
    return s[::-1]

def count_vowels(s):
    """Matndagi unli harflar sonini hisoblash"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)




# main.py

import math_operations
import string_utils

# Math funksiyalar
print(math_operations.add(5, 3))          # 8
print(math_operations.subtract(10, 4))    # 6
print(math_operations.multiply(6, 7))     # 42
print(math_operations.divide(15, 3))      # 5.0

# String funksiyalar
print(string_utils.reverse_string("hello"))     # olleh
print(string_utils.count_vowels("OpenAI"))      # 4

####3

geometry/
├── __init__.py
└── circle.py

# geometry/circle.py

import math

def calculate_area(radius):
    """Doiraning yuzasini hisoblaydi"""
    return math.pi * radius * radius

def calculate_circumference(radius):
    """Doiraning uzunligini hisoblaydi"""
    return 2 * math.pi * radius
# __init__.py:
# Bu fayl paket ekanligini bildiradi. Bo‘sh qoldirish mumkin yoki circle modulini ichkariga import qilish mumkin:
# geometry/__init__.py

from .circle import calculate_area, calculate_circumference


file_operations paketi tuzilmasi:



file_operations/
├── __init__.py
├── file_reader.py
└── file_writer.py

# file_reader.py:

# file_operations/file_reader.py

def read_file(file_path):
    """Fayldan ma'lumot o‘qish"""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Fayl topilmadi."


# file_writer.py:
# file_operations/file_writer.py

def write_file(file_path, content):
    """Faylga ma'lumot yozish"""
    with open(file_path, 'w') as f:
        f.write(content)
    return "Yozildi."


# file_operations/__init__.py

from .file_reader import read_file
from .file_writer import write_file



# main.py

from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Geometry test
r = 5
print(f"Doira yuzi: {calculate_area(r)}")
print(f"Doira uzunligi: {calculate_circumference(r)}")

# File operations test
write_file("test.txt", "Salom, bu test fayl!")
print(read_file("test.txt"))
