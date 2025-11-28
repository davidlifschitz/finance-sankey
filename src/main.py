import os
import glob
from parsers.capone_parser import CapitalOneParser
from parsers.chase_parser import ChaseParser
# from parsers.amex_parser import AmexParser
from categorizer import TransactionCategorizer
from sankey_generator import generate_sankey

def main():
    # 1. Setup paths
    import_path = 'data/imports'
    all_transactions = []
    
    # 2. Iterate through files in imports
    files = glob.glob(os.path.join(import_path, '*'))
    
    print(f"Found {len(files)} files to process...")

    for file_path in files:
        parser = None
        print(f"Processing: {file_path}")
        
        # Simple logic to choose parser based on filename (You should rename your files appropriately)
        if 'capital' in file_path.lower() or 'capone' in file_path.lower():
            parser = CapitalOneParser(file_path)
        elif 'chase' in file_path.lower():
            parser = ChaseParser(file_path)
        # elif 'amex' in file_path.lower():
        #     parser = AmexParser(file_path)
            
        if parser:
            txns = parser.parse()
            if txns:
                all_transactions.extend(txns)
                print(f"  -> Extracted {len(txns)} transactions")
        else:
            print("  -> No matching parser found for this file.")

    # 3. Categorize
    categorizer = TransactionCategorizer()
    categories = {}
    
    total_income = 0
    bank_flow = 0
    credit_card_flow = 0

    print("Categorizing transactions...")
    for txn in all_transactions:
        cat = categorizer.categorize(txn['description'])
        amount = abs(float(txn['amount'])) # Absolute value for visualization
        
        # Simple logic: If description implies income (Paycheck, Deposit), add to income
        # Otherwise treat as expense
        if 'deposit' in txn['description'].lower() or 'payroll' in txn['description'].lower():
            total_income += amount
            bank_flow += amount
        else:
            # Aggregate category spending
            categories[cat] = categories.get(cat, 0) + amount
            credit_card_flow += amount

    # 4. Generate Diagram
    if all_transactions:
        print("Generating Sankey Diagram...")
        # Note: You might need to tweak the flow logic in sankey_generator.py 
        # to handle the specific numbers dynamically
        generate_sankey(total_income, bank_flow, credit_card_flow, categories)
    else:
        print("No transactions found. Please check your PDF filenames and formats.")

if __name__ == "__main__":
    main()