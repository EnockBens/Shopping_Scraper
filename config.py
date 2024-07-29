import os

DB_USER = os.getenv('DB_USER', 'your_db_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_db_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'shopping_scraper')

DATABASE_URI = 'postgresql://benz:Kipkorir2015@localhost/scraper'

