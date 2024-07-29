from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from scraper.killimall_scraper import scrape_killimall
from scraper.jiji_scraper import scrape_jiji
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    source = db.Column(db.String(50), nullable=False)

    def __init__(self, name, url, price, source):
        self.name = name
        self.url = url
        self.price = price
        self.source = source

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    killimall_results = scrape_killimall(query)
    jiji_results = scrape_jiji(query)
    results = killimall_results + jiji_results
    
    # Debug: Print the results
    print(results)
    
    return render_template('results.html', results=results)

@app.route('/buy/<int:product_id>')
def buy(product_id):
    product = Product.query.get_or_404(product_id)
    return redirect(product.url)

if __name__ == '__main__':
    app.run(debug=True)
