"""
Loads a text file.
Tokenizes text (words, punctuation).
Passes the tokens to each enabled rule.
Aggregates results and prints reports.
"""

from ebooklib import epub
from bs4 import BeautifulSoup
from linter.rules import find_repeated_words
import spacy
nlp = spacy.load("en_core_web_sm")


def runLinter(file):

    book = epub.read_epub(file)
    results = []

    for item in book.get_items():
        if isinstance(item, epub.EpubHtml):
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            current_subtitle = None
            paragraphs = soup.find_all(['h1', 'h2', 'h3', 'p'])  # headings + paragraphs
            para_counter = 0

            for element in paragraphs:
                if element.name in ['h1', 'h2', 'h3']:
                    current_subtitle = element.get_text().strip()
                    para_counter = 0
                elif element.name == 'p':
                    para_counter += 1
                    para_text = element.get_text()
                    repeated_in_para = find_repeated_words(para_text)

                    if repeated_in_para:
                        # split paragraph into sentences with spaCy
                        doc = nlp(para_text)
                        for word, start, end in repeated_in_para:
                            # find which sentence contains the repeated word
                            for sent in doc.sents:
                                if start >= sent.start_char and end <= sent.end_char:
                                    results.append(
                                        (item.get_id(), current_subtitle, para_counter, sent.text, word)
                                    )

    return results

