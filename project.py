from datetime import datetime
import uuid

def generate_invoice():
    # Auto-generated fields
    date_today = datetime.now().strftime("%Y-%m-%d")
    invoice_number = f"INV-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8]}"

    # User inputs
    print("Fill the following details to generate your invoice:")
    bank_account = input("1. Bank Account Number: ")
    ifsc_code = input("2. Bank IFSC Code: ")
    client_company = input("3. Client's Company Name: ")
    legal_name = input("4. Your Legal Name: ")
    
    items = []
    print("6. Enter items (type 'done' to finish):")
    while True:
        item = input(" - Item description: ")
        if item.lower() == 'done':
            break
        cost = input("   Cost of item: ")
        items.append((item, cost))
    
    # Calculating total if not manually entered
    total = sum(float(c[1]) for c in items)
    entered_total = input(f"7. Total (press Enter to auto-calculate as ₹{total:.2f}): ")
    total = float(entered_total) if entered_total.strip() else total

    notes = input("8. Any other important detail (optional): ")

    # Displaying invoice
    print("\n" + "="*40)
    print(f"Invoice Number: {invoice_number}")
    print(f"Date: {date_today}")
    print(f"Bill To: {client_company}")
    print(f"From: {legal_name}")
    print("-" * 40)
    print("Items:")
    for desc, amt in items:
        print(f" - {desc}: ₹{amt}")
    print("-" * 40)
    print(f"Total Amount: ₹{total:.2f}")
    print("-" * 40)
    print("Bank Details:")
    print(f"  Account No: {bank_account}")
    print(f"  IFSC Code: {ifsc_code}")
    if notes:
        print("-" * 40)
        print(f"Notes: {notes}")
    print("="*40)

# Run the invoice generator
generate_invoice()
