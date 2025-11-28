# src/utils.py

from datetime import datetime

def validate_transaction(data):
    """Validate transaction data."""
    required_fields = ['amount', 'date', 'description']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')
    if not isinstance(data['amount'], (int, float)):
        raise ValueError('Amount must be a number')
    return True

def format_date(date_string):
    """Format the date from string to YYYY-MM-DD."""
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError('Invalid date format, should be YYYY-MM-DD')

def normalize_transaction_amount(amount, currency_factor):
    """Normalize transaction amount based on currency factor."""
    return amount / currency_factor
