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
    
def show_all_books():
    books = load_books()
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} — {book['author']} (оценка: {book['rating']}, дата: {book['date']})")

def show_average_rating():
    books = load_books()
    if books:
        avg = sum(book['rating'] for book in books) / len(books)
        print(f"Средняя оценка: {avg:.2f}")
    else:
        print("Книг нет.")

def show_author_stats():
    books = load_books()
    authors = {}
    for book in books:
        author = book['author']
        authors[author] = authors.get(author, 0) + 1
    for author, count in authors.items():
        print(f"{author}: {count} книг")


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
