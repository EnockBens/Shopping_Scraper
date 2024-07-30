# scraper/__init__.py

# This file is required to make Python treat the directory as a package.
# It can also be used to define what is available when the package is imported.

from .kilimall_scraper import scrape_kilimall
from .jiji_scraper import scrape_jiji
from .amazon_scraper import scrape_amazon
from .jumia_scraper import scrape_jumia

__all__ = ['scrape_kilimall', 'scrape_jiji' , 'scrape_amazon', 'scrape_jumia']
