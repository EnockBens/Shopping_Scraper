# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# Import the scraping functions from your scraper package
from scraper import scrape_killimall, scrape_jiji, scrape_amazon

# Import your configuration settings
import config

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an SQLAlchemy object and bind it to the app
db = SQLAlchemy(app)

# Define a model for the Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), nullable=False)  # Product name
    url = db.Column(db.String(200), nullable=False)  # Product URL
    price = db.Column(db.String(20), nullable=False)  # Product price
    source = db.Column(db.String(50), nullable=False)  # Source of the product

    def __init__(self, name, url, price, source):
        self.name = name
        self.url = url
        self.price = price
        self.source = source

# Create all the database tables
with app.app_context():
    db.create_all()

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle the search form submission
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']  # Get the query from the form
    killimall_results = scrape_killimall(query)  # Get results from Killimall
    jiji_results = scrape_jiji(query)  # Get results from Jiji
    amazon_results = scrape_amazon(query)  # Get results from Amazon
    results = killimall_results + jiji_results + amazon_results  # Combine the results
    
    # Debug: Print the results to the console
    print(results)
    
    return render_template('results.html', results=results)  # Render the results page

# Define the route to handle purchasing a product
@app.route('/buy/<int:product_id>')
def buy(product_id):
    product = Product.query.get_or_404(product_id)  # Get the product by ID or return 404
    return redirect(product.url)  # Redirect to the product URL

# Run the Flask app
if __name__ == '__main__':
    app.run(port= 5006 ,debug=True)



