
```markdown
# Shopping Scraper

## Overview

Shopping Scraper is a web application that allows users to search for products on two popular e-commerce websites: Killimall and Jiji. The application scrapes product information based on user queries and displays the results in a user-friendly interface. Users can then choose to purchase the products by being redirected to the respective product pages.

## Features

- Search for products on Killimall and Jiji.
- Display search results with product name, price, source, and a buy link.
- Redirect users to the official product page for purchase.
- Integrate with a PostgreSQL database to store product information.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- BeautifulSoup
- PostgreSQL
- HTML/CSS

## Setup and Installation

### Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/EnockBens/shopping_scraper.git
   cd shopping_scraper
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv shopping_scraper_env
   source shopping_scraper_env/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database:**

   - Create a new PostgreSQL database.
   - Update the `config.py` file with your database URI.

5. **Initialize the database:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the application:**

   ```bash
   flask run
   ```

   The application will be available at http://127.0.0.1:5000.

## Project Structure

```
shopping_scraper/
├── app.py
├── config.py
├── requirements.txt
├── scraper/
│   ├── __init__.py
│   ├── killimall_scraper.py
│   └── jiji_scraper.py
├── templates/
│   ├── index.html
│   └── results.html
└── static/
    └── style.css
```

## File Descriptions

- `app.py`: The main application file that sets up the Flask app, routes, and database models.
- `config.py`: Configuration file for database URI and other settings.
- `requirements.txt`: List of required Python packages.
- `scraper/`: Directory containing the scraper scripts for Killimall and Jiji.
  - `killimall_scraper.py`: Script to scrape product data from Killimall.
  - `jiji_scraper.py`: Script to scrape product data from Jiji.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Template for the homepage.
  - `results.html`: Template for displaying search results.
- `static/`: Directory for static files (CSS, JavaScript).

## Usage

- Navigate to the homepage (http://127.0.0.1:5000).
- Enter a product query in the search bar and click "Search".
- View the search results on the results page.
- Click the "Buy" link to be redirected to the product page on the respective e-commerce site.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/yourusername/shopping_scraper/blob/master/LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- Your Name
- Your Email
- Your GitHub Profile
```

