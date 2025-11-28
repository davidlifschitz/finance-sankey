import csv

class CapitalOneParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        transactions = []
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = {
                    'date': row['date'],
                    'merchant': row['merchant'],
                    'category': row['category'],
                    'amount': float(row['amount']),
                }
                transactions.append(transaction)
        return transactions
