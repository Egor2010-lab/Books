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
    
    # Запрашиваем данные о книге
    title = input("Название книги: ").strip()
    author = input("Автор: ").strip()
    
    # Валидация оценки (только числа от 1 до 5)
    while True:
        try:
            rating = int(input("Оценка (1–5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Пожалуйста, введите число от 1 до 5.")
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    # Формируем дату добавления
    date = datetime.now().strftime("%Y-%m-%d")
    
    # Создаём словарь с данными книги и добавляем в список
    new_book = {
        "title": title,
        "author": author,
        "rating": rating,
        "date": date
    }
    books.append(new_book)
    
    # Сохраняем обновлённый список книг и выводим сообщение
    save_books(books)
    print("Книга добавлена!")

def show_all_books():
    books = load_books()
    if not books:
        print("Список книг пуст.")
        return
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
    if authors:
        for author, count in authors.items():
            print(f"{author}: {count} книг")
    else:
        print("Нет данных об авторах.")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Средняя оценка")
        print("4. Статистика по авторам")
        print("5. Выйти")
        
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == '1':
            add_book()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            show_average_rating()
        elif choice == '4':
            show_author_stats()
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()
