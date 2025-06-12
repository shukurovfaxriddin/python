##1
import threading

# Tub sonni aniqlovchi funksiya
def is_prime(n):
    if n < 2:
        return False
    for number in range(2, int(n**0.5)+1):
        if n % number == 0:
            return False
    return True

# Har bir threadda bajariladigan funksiya
def numbers_list(start, end, tub_sonlar, murakkab_sonlar):
    for number in range(start, end+1):
        if is_prime(number):
            tub_sonlar.append(number)
        else:
            murakkab_sonlar.append(number)

def main(start, end):
    # Natijalarni saqlash uchun listlar
    tub1, murakkab1 = [], []
    tub2, murakkab2 = [], []

    mid = (start + end) // 2

    # Ikkita thread yaratiladi
    thread1 = threading.Thread(target=numbers_list, args=(start, mid, tub1, murakkab1))
    thread2 = threading.Thread(target=numbers_list, args=(mid+1, end, tub2, murakkab2))

    # Threadlar ishga tushiriladi
    thread1.start()
    thread2.start()

    # Threadlar tugashini kutamiz
    thread1.join()
    thread2.join()

    # Natijalarni birlashtiramiz
    all_tub = sorted(tub1 + tub2)
    all_murakkab = sorted(murakkab1 + murakkab2)

    print("Topilgan tub sonlar:", all_tub)
    # print("Topilgan murakkab sonlar:", all_murakkab)

# Dasturni chaqirish
main(1, 100)
##2

import threading
from collections import Counter

partial_results = []
lock = threading.Lock()

def count_words(lines):
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)
    with lock:
        partial_results.append(local_counter)

def main(filename, thread_count=4):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // thread_count
    threads = []

    for i in range(thread_count):
        start = i * chunk_size
        end = None if i == thread_count - 1 else (i + 1) * chunk_size
        thread_lines = lines[start:end]
        t = threading.Thread(target=count_words, args=(thread_lines,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_counter = Counter()
    for c in partial_results:
        total_counter.update(c)

    for word, count in total_counter.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main("sample.txt")
