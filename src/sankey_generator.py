import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

def generate_sankey(income, bank_account, credit_card, categories):
    """Generate a Sankey diagram showing the flow of funds."""
    sankey = Sankey(
        flows=[income, -bank_account, bank_account, -credit_card] + [-amount for amount in categories.values()],
        # Corrected: Added 'Credit Card' as the fourth label
        labels=['Income', 'Bank Account', 'Bank Account', 'Credit Card', *categories.keys()], # Note: Check the second 'Bank Account' label
        orientations=[0, 1, 0, 1] + [0]*len(categories)
    )
    
    sankey.finish()
    plt.title('Sankey Diagram of Income Flow')
    plt.show()

# Sample data for demonstration
if __name__ == "__main__":
    income = 1000
    bank_account = 600
    credit_card = 300
    categories = {'Rent': 400, 'Groceries': 200, 'Utilities': 100}

    generate_sankey(income, bank_account, credit_card, categories)