"""
Loads a text file.
Tokenizes text (words, punctuation).
Passes the tokens to each enabled rule.
Aggregates results and prints reports.
"""

from ebooklib import epub
from bs4 import BeautifulSoup

