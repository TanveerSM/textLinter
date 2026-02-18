"""
Loads a text file.
Tokenizes text (words, punctuation).
Passes the tokens to each enabled rule.
Aggregates results and prints reports.
"""

from ebooklib import epub

from bs4 import BeautifulSoup
from rules.repeated_words import find_repeated_words



book = epub.read_epub(r'') #file path

text_content = ""
for item in book.get_items():
    if isinstance(item, epub.EpubHtml):
        soup = BeautifulSoup(item.get_content(), 'html.parser')

        current_subtitle = None
        paragraphs = soup.find_all(['h1', 'h2', 'h3', 'p'])  # headings + paragraphs

        para_counter = 0  # reset counter when subtitle changes
        for element in paragraphs:
            if element.name in ['h1', 'h2', 'h3']:
                current_subtitle = element.get_text().strip()
                para_counter = 0  # reset paragraph numbering for new subtitle
            elif element.name == 'p':
                para_counter += 1
                para_text = element.get_text()
                repeated_in_para = find_repeated_words(para_text)
                if repeated_in_para:
                    print(f"Chapter '{item.get_id()}', Subtitle '{current_subtitle}', Paragraph {para_counter}:")
                    for word, start, end in repeated_in_para[:5]:
                        snippet = para_text[start:end]
                        print(f"  Repeated word: '{word}' -> '{snippet}'")

