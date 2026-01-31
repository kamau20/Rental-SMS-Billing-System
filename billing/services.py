PAYBILL_NUMBER = "123456"
ACCOUNT_NAME = "RENT"

def generate_bill_sms(bill):
    return (
        f"Dear {bill.tenant.name} (House {bill.tenant.house_number}),\n"
        f"Rent: KES {bill.tenant.monthly_rent}\n"
        f"Garbage: KES {bill.garbage_fee}\n"
        f"Water: KES {bill.water_bill}\n"
        f"Total: KES {bill.total}\n"
        f"Paid: KES {bill.amount_paid}\n"
        f"Balance: KES {bill.balance}\n"
        f"Pay via Paybill {PAYBILL_NUMBER}, Acc {ACCOUNT_NAME}.\n"
        f"Thank you."
    )
