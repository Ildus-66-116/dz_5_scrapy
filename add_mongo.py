from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['books_in_labirint']
books = db.books_labirint

with open('./jobparser/labirint.json', 'r') as f:
    data = json.load(f)
count = 0
bad_count = 0

for book in data:
    try:
        books.insert_one(book)
        count += 1
        print(f'Добавлено {count} данных')
    except:
        print(book)
        bad_count += 1
client.close()

print(f'Не добавлено {bad_count} данных')
