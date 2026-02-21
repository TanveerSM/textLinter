# Text Linter – Repeated Words Detector

While reading a book recently, I noticed a few repeated words that seemed like small mistakes but really shouldn’t have made it into a published work. I felt a little bad for the author—these are minor errors, but they affect readability.

This project is a personal experiment to see **how difficult it would be to catch repeated words automatically**. Using Python, EPUB parsing, and some text analysis, the tool highlights repeated words in paragraphs and organizes them by chapter and subtitle, making it easier to pinpoint where errors occur.

The goal isn’t to criticize authors, but to explore **practical text analysis** and **build something useful** for readers, editors, or anyone interested in automated proofreading.

## Features
- Reads EPUB files
- Detects repeated words in paragraphs
- Tracks chapters, subtitles, and paragraph numbers for context
- Shows the first few occurrences for quick review

## Usage
1. Place your EPUB file in the project eBook folder
3. Run the script:
   ```bash
   python main.py
   ```
4. Review the output in the eBook folder to see repeated words by chapter, subtitle, and paragraph.

## Example Output
Chapter 'chapter10', Subtitle 'PITCH PERFECT—OR HOW CONDUCTORS FOSTER ORIGINALITY', Paragraph 22:

  Repeated word: 'can' -> One study even showed that it can can also help ward off serious injuries.
