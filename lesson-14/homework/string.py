# 1
import json
with open("students_data.json", "r") as file:
    students_data = json.load(file)

for student in students_data:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"Email: {student['email']}")
    print("\n")# 1
import json
with open("students_data.json", "r") as file:
    students_data = json.load(file)

for student in students_data:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"Email: {student['email']}")
    print("\n")
  # 2
import requests

url=r"https://api.openweathermap.org/data/2.5/find?q=Tashkent&appid=5796abbde9106b7da4febfae8c44c232&units=metric"

r1=requests.get(url)

# r1.headers['content-type']

d1=r1.json()

print(d1['list'][0]['name'])
print('temperature :',d1['list'][0]['main']['temp'])
print('humidity :',d1['list'][0]['main']['humidity']*1.0)
print('description:', d1['list'][0]['weather'][0]['description'])
import json
import os

# Fayl nomi
FILE_NAME = 'books.json'

# JSON faylni o'qish
def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

# JSON faylga yozish
def save_books(books):
    with open(FILE_NAME, 'w') as file:
        json.dump(books, file, indent=4)

# 1. Kitob qo'shish
def add_book():
    books = load_books()
    try:
        book_id = int(input("ID ni kiriting: "))
    except ValueError:
        print("ID butun son bo‘lishi kerak.")
        return

    title = input("Sarlavha (title): ")
    author = input("Muallif (author): ")
    year = input("Yili (year): ")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year
    }

    books.append(new_book)
    save_books(books)
    print("✅ Kitob qo‘shildi!")

# 2. Kitob yangilash
def update_book():
    books = load_books()
    try:
        book_id = int(input("Yangilamoqchi bo‘lgan kitob ID sini kiriting: "))
    except ValueError:
        print("ID noto‘g‘ri.")
        return

    for book in books:
        if book['id'] == book_id:
            print(f"Joriy ma'lumot: {book}")
            book['title'] = input("Yangi sarlavha: ")
            book['author'] = input("Yangi muallif: ")
            book['year'] = input("Yangi yil: ")
            save_books(books)
            print("✅ Kitob yangilandi!")
            return

    print("❌ Bunday ID bilan kitob topilmadi.")

# 3. Kitob o‘chirish
def delete_book():
    books = load_books()
    try:
        book_id = int(input("O‘chirmoqchi bo‘lgan kitob ID sini kiriting: "))
    except ValueError:
        print("ID noto‘g‘ri.")
        return

    new_books = [book for book in books if book['id'] != book_id]

    if len(new_books) == len(books):
        print("❌ Bunday ID topilmadi.")
    else:
        save_books(new_books)
        print("✅ Kitob o‘chirildi!")

# 4. Barcha kitoblarni ko‘rish
def list_books():
    books = load_books()
    if not books:
        print("📂 Hech qanday kitob yo‘q.")
        return

    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

# Menyu
def main():
    while True:
        print("\n--- 📚 Kitoblar Menyusi ---")
        print("1. Kitob qo‘shish")
        print("2. Kitob yangilash")
        print("3. Kitob o‘chirish")
        print("4. Kitoblarni ko‘rish")
        print("0. Chiqish")
        
        choice = input("Tanlang: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            list_books()
        elif choice == '0':
            print("Dasturdan chiqildi.")
            break
        else:
            print("❗️Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")

if __name__ == "__main__":
    main()
import requests
import random

# Sizning API kalitingiz
API_KEY = '1237d3d5'

# Oldindan belgilangan janr bo‘yicha film nomlari
movies_by_genre = {
    "Action": ["Mad Max: Fury Road", "John Wick", "The Dark Knight", "Gladiator", "Die Hard"],
    "Comedy": ["The Hangover", "Superbad", "Step Brothers", "The Mask", "Groundhog Day"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club", "The Godfather", "A Beautiful Mind"],
    "Sci-Fi": ["Inception", "Interstellar", "The Matrix", "Arrival", "Blade Runner 2049"]
}

# Foydalanuvchidan janrni so‘rash
genre = input("Enter a movie genre (Action, Comedy, Drama, Sci-Fi): ").strip().title()

# Janr mavjudligini tekshirish
if genre not in movies_by_genre:
    print("Sorry, we don't have recommendations for that genre.")
else:
    # Tanlangan janrdan random film
    movie_title = random.choice(movies_by_genre[genre])
    
    # API chaqiruvi qilish
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Natijani chiqarish
    if data['Response'] == 'True':
        print("\n🎬 Movie Recommendation:")
        print(f"Title: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"Genre: {data['Genre']}")
        print(f"IMDb Rating: {data['imdbRating']}")
        print(f"Plot: {data['Plot']}")
    else:
        print("Movie not found in OMDb database.")
