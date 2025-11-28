class TransactionCategorizer:
    def __init__(self):
        self.categories = {
            'Food': ['groceries', 'restaurants', 'coffee', 'snacks'],
            'Transportation': ['gas', 'public transport', 'taxi', 'ride share'],
            'Entertainment': ['movies', 'games', 'concerts', 'subscriptions'],
            'Utilities': ['electricity', 'water', 'internet', 'phone'],
            'Shopping': ['clothes', 'electronics', 'gifts'],
            'Healthcare': ['pharmacy', 'doctor', 'insurance']
        }

    def categorize(self, transaction_description):
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword in transaction_description.lower():
                    return category
        return 'Other'

# Example Usage
if __name__ == '__main__':
    categorizer = TransactionCategorizer()
    print(categorizer.categorize('I went to the grocery store'))  # Output: 'Food'