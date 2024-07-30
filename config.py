import os

DB_USER = os.getenv('DB_USER', 'benz')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'Kipkorir2015')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'scraper')

DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
