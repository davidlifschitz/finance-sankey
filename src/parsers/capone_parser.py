import csv
import re
from PyPDF2 import PdfReader

class CapitalOneParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        if self.file_path.lower().endswith('.pdf'):
            return self._parse_pdf()
        else:
            return self._parse_csv()

    def _parse_csv(self):
        transactions = []
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Adjust column names based on actual CSV headers
                    transaction = {
                        'date': row.get('Transaction Date', row.get('Date')),
                        'description': row.get('Description', ''),
                        'category': row.get('Category', 'Uncategorized'),
                        'amount': float(row.get('Amount', row.get('Debit', 0)) or 0) * -1 if row.get('Debit') else float(row.get('Amount', 0)),
                        'source': 'Capital One'
                    }
                    transactions.append(transaction)
        except Exception as e:
            print(f"Error parsing CSV {self.file_path}: {e}")
        return transactions

    def _parse_pdf(self):
        transactions = []
        try:
            reader = PdfReader(self.file_path)
            # Regex to find dates like Jan 01 or 01/01/2024
            # This is a generic pattern; Capital One formats vary by account type
            date_pattern = re.compile(r'(\w{3}\s\d{2}|\d{2}/\d{2}/\d{2,4})')
            
            for page in reader.pages:
                text = page.extract_text()
                lines = text.split('\n')
                for line in lines:
                    # Simple heuristic: Lines with dates and dollar signs are likely transactions
                    if date_pattern.search(line) and '$' in line:
                        parts = line.split()
                        # This logic is brittle and depends heavily on specific PDF layout
                        transactions.append({
                            'date': parts[0], 
                            'description': " ".join(parts[1:-1]),
                            'amount': float(parts[-1].replace('$', '').replace(',', '')),
                            'category': 'Uncategorized', # PDFs rarely contain category data
                            'source': 'Capital One'
                        })
        except Exception as e:
            print(f"Error parsing PDF {self.file_path}: {e}")
        return transactions