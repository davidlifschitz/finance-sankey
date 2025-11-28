import pandas as pd
from datetime import datetime

class ChaseParser:
    """Parser for Chase bank CSV export files."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = []
    
    def parse(self):
        """Parse Chase CSV file and standardize transaction format."""
        try:
            df = pd.read_csv(self.file_path)
            
            # Chase typically has columns: Transaction Date, Post Date, Description, Category, Type, Amount
            for index, row in df.iterrows():
                transaction = {
                    'date': pd.to_datetime(row.get('Transaction Date', row.get('Date'))),
                    'description': row.get('Description', ''),
                    'category': row.get('Category', 'Uncategorized'),
                    'amount': float(row.get('Amount', 0)),
                    'type': row.get('Type', 'Debit'),
                    'source': 'Chase'
                }
                self.transactions.append(transaction)
            
            return self.transactions
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None
        except Exception as e:
            print(f"Error parsing Chase CSV: {e}")
            return None
    
    def get_transactions_by_month(self, year, month):
        """Filter transactions by year and month."""
        return [t for t in self.transactions if t['date'].year == year and t['date'].month == month]