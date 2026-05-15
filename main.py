import json
from datetime import datetime

def load_books():
    try:
        with open('books.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book():
    books = load_books()
    title = input("Название книги: ")
    author = input("Автор: ")
    rating = int(input("Оценка (1–5): "))
    date = datetime.now().strftime("%Y-%m-%d")

    new_book = {
        "title": title,
        "author": author,
        "rating": rating,
        "date": date
    }
    books.append(new_book)
    save_books(books)
    print("Книга добавлена!")

if __name__ == "__main__":
    add_book()
