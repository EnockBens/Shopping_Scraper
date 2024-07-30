# scraper/__init__.py

# This file is required to make Python treat the directory as a package.
# It can also be used to define what is available when the package is imported.

from .killimall_scraper import scrape_killimall
from .jiji_scraper import scrape_jiji
from .amazon_scraper import scrape_amazon

__all__ = ['scrape_killimall', 'scrape_jiji' , 'scrape_amazon']
