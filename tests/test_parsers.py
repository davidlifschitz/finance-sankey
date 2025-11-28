import unittest
from parsers.chase import ChaseParser
from parsers.capital_one import CapitalOneParser
from parsers.amex import AmexParser

class TestParsers(unittest.TestCase):

    def setUp(self):
        self.chase_parser = ChaseParser()
        self.capital_one_parser = CapitalOneParser()
        self.amex_parser = AmexParser()

    def test_chase_csv_parsing(self):
        transactions = self.chase_parser.parse_csv('path/to/chase.csv')
        self.assertIsInstance(transactions, list)
        self.assertGreater(len(transactions), 0)

    def test_chase_transaction_extraction(self):
        transactions = self.chase_parser.parse_csv('path/to/chase.csv')
        extracted = self.chase_parser.extract_transactions(transactions)
        self.assertGreater(len(extracted), 0)

    def test_chase_month_filtering(self):
        transactions = self.chase_parser.parse_csv('path/to/chase.csv')
        filtered = self.chase_parser.filter_by_month(transactions, '2025-11')
        for transaction in filtered:
            self.assertEqual(transaction.date.month, 11)

    def test_capital_one_csv_parsing(self):
        transactions = self.capital_one_parser.parse_csv('path/to/capital_one.csv')
        self.assertIsInstance(transactions, list)
        self.assertGreater(len(transactions), 0)

    def test_capital_one_transaction_extraction(self):
        transactions = self.capital_one_parser.parse_csv('path/to/capital_one.csv')
        extracted = self.capital_one_parser.extract_transactions(transactions)
        self.assertGreater(len(extracted), 0)

    def test_capital_one_month_filtering(self):
        transactions = self.capital_one_parser.parse_csv('path/to/capital_one.csv')
        filtered = self.capital_one_parser.filter_by_month(transactions, '2025-11')
        for transaction in filtered:
            self.assertEqual(transaction.date.month, 11)

    def test_amex_csv_parsing(self):
        transactions = self.amex_parser.parse_csv('path/to/amex.csv')
        self.assertIsInstance(transactions, list)
        self.assertGreater(len(transactions), 0)

    def test_amex_transaction_extraction(self):
        transactions = self.amex_parser.parse_csv('path/to/amex.csv')
        extracted = self.amex_parser.extract_transactions(transactions)
        self.assertGreater(len(extracted), 0)

    def test_amex_month_filtering(self):
        transactions = self.amex_parser.parse_csv('path/to/amex.csv')
        filtered = self.amex_parser.filter_by_month(transactions, '2025-11')
        for transaction in filtered:
            self.assertEqual(transaction.date.month, 11)

if __name__ == '__main__':
    unittest.main()