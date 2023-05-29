# BibTeX Filter Script

This script filters BibTeX entries based on specified keywords and generates a new BibTeX file containing the filtered entries.

## Description

The BibTeX Filter Script is a Python script that allows you to filter BibTeX entries from a given input BibTeX file based on specified keywords. It provides a command-line interface for easy usage and requires the following Python libraries: `argparse`, `re`, `bibtexparser`.

The script performs the following operations:
- Reads the input BibTeX file.
- Filters the BibTeX entries based on the specified keywords.
- Removes entries with empty "keywords" fields.
- Writes the filtered BibTeX entries to the output BibTeX file.

## Prerequisites

- Python 3.x
- `argparse` library
- `re` library
- `bibtexparser` library

## Usage

1. Clone the repository or download the script file to your local machine.
2. Install the required Python libraries (`argparse`, `re`, `bibtexparser`) if not already installed.
3. Prepare your input BibTeX file and keywords file.
4. Open a terminal or command prompt.
5. Run the script using the following command:

```shell
python bibtex_filter_script.py -ib input_bibtex_file.bib -ob output_bibtex_file.bib -k keywords_file.txt

```
Replace the following placeholders with your actual file names:
- `input_bibtex_file.bib`: Path to the input BibTeX file.
- `output_bibtex_file.bib`: Path to the output BibTeX file.
- `keywords_file.txt`: Path to the file containing the keywords (each keyword on a separate line).

6. After executing the command, the script will filter the BibTeX entries based on the specified keywords and generate the output BibTeX file.
