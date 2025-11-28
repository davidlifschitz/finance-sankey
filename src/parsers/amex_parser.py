import csv
import pandas as pd
from PyPDF2 import PdfReader

def parse_csv(file_path):
    """Parses a CSV file containing American Express transactions."""
    transactions = []
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions

def parse_pdf(file_path):
    """Parses a PDF file containing American Express transactions."""
    transactions = []
    reader = PdfReader(file_path)
    for page in reader.pages:
        text = page.extract_text()
        transactions.append(text)
    return transactions
