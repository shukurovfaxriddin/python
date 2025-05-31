##1
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

except ValueError:
    print("Please enter valid integers.")
  ##2
  try:
    age = int(input("Yoshingizni kiriting: "))
    print("Sizning yoshingiz:", age)

except ValueError:
    print("Iltimos, faqat butun son kiriting.")
  ##3
  filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
##4
bir = int(input("Enter the filename: "))
ikki = int(input("Enter the filename: "))

try:
    print("Sizning yoshingiz:", bir,ikki)

except TypeError :
    print("Iltimos, faqat butun son kiriting.")

##5
try:
    with open("C:\\Windows\\System32\\config.txt", "w") as f:  # Linux'dagi tizim fayli
        f.write("test")
except PermissionError:
    print("Xatolik: Sizda bu faylga yozish uchun ruxsat yo\'q.")
##6
#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
a='hello'
try:
    print(a[6])
except IndexError as f:
    print(f"Error: Index out of range. {f}")

##7
try:
    number = int(input("Iltimos, biror raqam kiriting: "))
    print(f"Siz kiritgan raqam: {number}")
except KeyboardInterrupt:
    print("Kiritish bekor qilindi (KeyboardInterrupt).")
except ValueError:
    print("Iltimos, faqat raqam kiriting.")

##8
# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    number = int(input("Iltimos, biror raqam kiriting: "))
    number1 = int(input("Iltimos, biror raqam kiriting: "))
    result=number/number1
    print(f"Natija: {result}")
except ArithmeticError  as f:
    print(f" Arifmetik xatolik yuz berdi: {f}")
except ValueError:
    print("Iltimos, faqat raqam kiriting.")


##9
try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content:\n")
        print(content)
except UnicodeDecodeError as e:
    print(f"Encoding error: {e}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

##10
my_list = [1, 2, 3, 4, 5]

try:
    my_list.appendd(6)
except AttributeError as e:
    print(f"AttributeError: {e}")

##11
#Write a Python program to read an entire text file.
try:
    with open("file.txt", "r") as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except FileNotFoundError:
    print("Fayl topilmadi. Iltimos, fayl nomini tekshiring.")

##12
#Faylning birinchi n qatorini o'qish uchun Python dasturini yozing.
try:
    n = int(input('Nechta birinchi qatorni o‘qishni xohlaysiz? '))
    with open("test.csv", "r", encoding="utf-8") as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break  # Fayl tugadi
            print(f"{i+1}-qator: {line.strip()}")
except FileNotFoundError:
    print("Fayl topilmadi. Iltimos, fayl nomini tekshiring.")
except ValueError:
    print("Iltimos, butun son kiriting.")

##13
try:
    with open("test.csv",'a') as f:
            file = f.write('s\n')
    with open("test.csv",'r') as f:
        print(f.readlines())
except FileNotFoundError:
    print("Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

##14
#Напишите программу на Python для чтения последних n строк файла.
try:
    n = int(input("Oxirgi nechta qatorni o\'qishni xohlaysiz? "))

    with open("test.csv", "r") as f:
        lines = f.readlines()

        last_lines = lines[-n:]
        for line in last_lines:
            print(line.strip())

except FileNotFoundError:
    print("Fayl topilmadi.")
except ValueError:
    print("Iltimos, butun son kiriting.")
##15
#Write a Python program to read a file line by line and store it into a list.

l1=[]
with open("test.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            l1.append(line)
print(l1)
##16
with open("test.csv",'r') as f:
        print(f.readlines())

##17
# Fayl nomi: example.txt bo'lishi mumkin
with open("test.csv", "r", encoding="utf-8") as file:
    content = ""
    for line in file:
        content += line  

print("Fayldagi matn:")
print(content)

##18
array = []
with open("test.csv", "r") as file:
    for line in file:
        array.append(line.rstrip('\n'))
print(array)

##20
# Write a Python program to find the longest words.
words = [word.strip() for word in l1]
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Longest word(s):", longest_words)

##21
#Write a Python program to count the number of lines in a text file.
with open("test.csv", 'r') as file:
    line_count = sum(1 for _ in file)
print(f"Number of lines in the file: {line_count}")

##22
#Write a Python program to count the frequency of words in a file.
from collections import Counter

with open("test.csv", 'r') as file:
    text = file.read()

words = text.split()
word_counts = Counter(words)

for word, count in word_counts.items():
    print(f"'{word}': {count}")

##23
#Write a Python program to get the file size of a plain file.
import os

file_path = "test.csv"

try:
    size = os.path.getsize(file_path)
    print(f"File size: {size} bytes")
except FileNotFoundError:
    print("Fayl topilmadi.")

##24
# Write a Python program to write a list to a file.
with open("test.csv", "w") as file:
    for item in l1:
        file.write(item)
print("List has been written to output.txt")

##25
#Write a Python program to copy the contents of a file to another file.

source_file = "test.csv"
destination_file = "copy_test.csv"

try:
    with open(source_file, "r") as src, open(destination_file, "w") as dst:
        for line in src:
            dst.write(line)
    print(f"Contents copied from {source_file} to {destination_file}.")
except FileNotFoundError:
    print("Source file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

##25
# Write a Python program to combine each line from the first file with the corresponding line in the second file.

combined_lines = []
try:
    with open("test.csv", 'r') as file1, open("test.csv", 'r') as file2:
        for line1, line2 in zip(file1, file2):
            combined_line = line1.rstrip('\n') + " " + line2.rstrip('\n')
            combined_lines.append(combined_line)
    print("Combined lines:")
    for line in combined_lines:
        print(line)
except FileNotFoundError as e:
    print(f"File not found: {e}")

##26
##Write a Python program to read a random line from a file.

import random

try:
    with open("test.csv", "r") as file:
        lines = file.readlines()
        if lines:
            random_line = random.choice(lines).strip()
            print(f"Random line: {random_line}")
        else:
            print("File is empty.")
except FileNotFoundError:
    print("File not found.")

##27
#Write a Python program to assess if a file is closed or not.
with open("test.csv", "r") as file:
    print(f"File closed inside 'with' block? {file.closed}")

print(f"File closed after 'with' block? {file.closed}")

##28
# Write a Python program to remove newline characters from a file.
try:
    with open("test.csv", "r") as file:
        content_no_newlines = file.read().replace('\n', '')
    print("Content without newlines:")
    print(content_no_newlines)
except FileNotFoundError:
    print("File not found.")

##29

def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            for ch in [',', '\n']:  # istasangiz "." ";" ham qo‘shishingiz mumkin
                text = text.replace(ch, ' ')
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return 0

# Misol uchun test
filename = input("Fayl nomini kiriting: ")
word_count = count_words_in_file(filename)
print(f"So‘zlar soni: {word_count}")

##30
# Write a Python program to extract characters from various text files and put them into a list.
filenames = ["test.csv", "copy_test.csv"]

characters = []
for fname in filenames:
    try:
        with open(fname, 'r') as file:
            content = file.read()
            characters.extend(list(content))
    except FileNotFoundError:
        print(f"File not found: {fname}")

print("Extracted characters:", characters)

##31
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write(f"This is file {filename}\n")

print("26 text files (A.txt to Z.txt) have been created.")

##32
#Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
import string

def write_alphabet_to_file(filename, letters_per_line):
    alphabet = string.ascii_lowercase
    with open(filename, "w") as file:
        for i in range(0, len(alphabet), letters_per_line):
            line = alphabet[i:i+letters_per_line]
            file.write(line + "\n")
    print(f"Alphabet written to {filename} with {letters_per_line} letters per line.")

# Example usage:
write_alphabet_to_file("alphabet.txt", 5)
