import json
books = [
    {'title': '1984', 'author': 'Оруэлл', 'year': '1949' },
    {'title': 'Человек в футляре', 'author': 'Чехов', 'year': '1898' },
    {'title': 'Превращение', 'author': 'Кафка', 'year': '1912' },
    {'title': 'Повелитель мух', 'author': 'Голдинг', 'year': '1954' },
    {'title': 'Морфий', 'author': 'Булгаков', 'year': '1917' }
]

json_str = json.dumps(books)
count =0
for book in books:
    count +=1
    print('-'*20, f'Книга {count}', '-'*20)
    print(f'Название: {book['title']}, Автор: {book['author']}')
    print('-'*20, f'{book['year']}', '-'*20)