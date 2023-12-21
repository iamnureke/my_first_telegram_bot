import requests
import sqlite3 as sq


class FakeStoreAPI:

    def __init__(self):
        self.url = 'https://fakestoreapi.com/products/'

    def get_all_products(self):
        return requests.get(self.url).json()

    def get_product_by_id(self, product_id):
        self.product_id = product_id
        return requests.get(f'{self.url}{self.product_id}').json()

    def get_limited_results(self, limit):
        self.limit = limit
        params = {"limit": self.limit}
        return requests.get(f'{self.url}', params=params).json()

    def get_sorted_products_by_id(self, key):
        self.key = key
        params = {"sort": self.key}
        return requests.get(f'{self.url}', params=params).json()

    def get_all_categories(self):
        return requests.get(self.url + 'categories').json()

    def get_product_in_specific_category(self, category):
        self.category = category
        return requests.get(f'{self.url}category/{self.category}').json()

    def get_products_by_category(self):
        allData = []
        for i in self.get_all_categories():
            allData.append(self.get_product_in_specific_category(i))
        return allData


class FakeStoreDb:
    def __init__(self):
        self.database = 'database.db'

    def create_product_table(self):
        with sq.connect(self.database) as connect:
            cursor = connect.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY,
                title TEXT,
                price REAL,
                category TEXT,
                description TEXT,
                image TEXT,
                rating_rate REAL,
                rating_count INTEGER
            )
            ''')

    def insert_product(self, title, description, price, category, image, rating_rate, rating_count):
        with sq.connect(self.database) as connect:
            cursor = connect.cursor()
            cursor.execute('''
                INSERT INTO product (title, description, price, category, image, rating_rate, rating_count) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (title, description, price, category, image, rating_rate, rating_count))

    def insert_all_products(self, products):
        for product in products:
            self.insert_product(
                product['title'],
                product['description'],
                product['price'],
                product['category'],
                product['image'],
                product['rating']['rate'],
                product['rating']['count']
            )

    def delete_table(self):
        with sq.connect(self.database) as connect:
            cursor = connect.cursor()
            cursor.execute('DROP TABLE IF EXISTS product')
