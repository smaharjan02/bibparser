#BibTeX Filter Script
This script filters BibTeX entries based on specified keywords and generates a new BibTeX file containing the filtered entries.

Description
The BibTeX Filter Script is a Python script that allows you to filter BibTeX entries from a given input BibTeX file based on specified keywords. It provides a command-line interface for easy usage and requires the following Python libraries: argparse, re, bibtexparser.

The script performs the following operations:

Reads the input BibTeX file.
Filters the BibTeX entries based on the specified keywords.
Removes entries with empty "keywords" fields.
Writes the filtered BibTeX entries to the output BibTeX file.
