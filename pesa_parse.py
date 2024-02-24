#!/usr/bin/python3
'''
Your program's comments and imports here
'''

import re
import sqlite3

def parse_message(message):
    # Regular expressions to extract information
    transaction_code = re.search(r'^([A-Z]{2}\w{8})', message).group(1)

    transaction_type = determine_transaction_type(message)

    amount = re.search(r'Ksh([\d,]+\.\d{2})', message).group(1).replace(",", "")

    sender_name = "YOU"  # You mentioned that for sent transactions, the sender is always "YOU."

    sender_phone = "N/A"  # Set sender phone to "N/A" for all sent transactions and such payments.

    receiver_name = ""
    receiver_account = ""
    receiver_phone = "UNKNOWN"  # Set receiver phone to "UNKNOWN" for this specific type of transaction.

    # Check for airtime purchases and set the receiver name to "SAFARICOM"
    if "You bought Ksh" in message:
        receiver_name = "SAFARICOM"

    # Check if the transaction is "received" with YOU as the receiver
    received_match = re.search(r'You have received Ksh([\d,]+\.\d{2}) from (.+) (\d{10})', message)
    if received_match:
        amount = received_match.group(1).replace(",", "")
        sender_name = received_match.group(2).strip()
        sender_phone = received_match.group(3)

    # Check if the transaction is "sent" with YOU as the sender
    sent_match = re.search(r'sent to (.+) (\d{10})', message)
    if sent_match:
        receiver_name = sent_match.group(1).strip()
        receiver_phone = sent_match.group(2)

    # Check for merchant payments and extract the receiver name and account
    merchant_match = re.search(r'sent to (.+) for account (\w+)', message)
    if merchant_match:
        receiver_name = merchant_match.group(1).strip()
        receiver_account = merchant_match.group(2).strip()
        receiver_phone = "N/A"

    # Check for bill payments and extract the receiver name
    bill_payment_match = re.search(r'paid to (.+) on \d{1,2}/\d{1,2}/\d{2}', message)
    if bill_payment_match:
        receiver_name = bill_payment_match.group(1).strip()

    date_match = re.search(r'on (\d{1,2}/\d{1,2}/\d{2}) at (\d{1,2}:\d{2} [AP]M)', message)
    date = date_match.group(1) if date_match else "UNKNOWN"
    time = date_match.group(2) if date_match else "UNKNOWN"

    balance_match = re.search(r'New M-PESA balance is Ksh([\d,]+\.\d{2})', message)
    balance = balance_match.group(1).replace(",", "") if balance_match else "UNKNOWN"

    transaction_cost_match = re.search(r'Transaction cost, Ksh([\d,]+\.\d{2})', message)
    transaction_cost = transaction_cost_match.group(1).replace(",", "") if transaction_cost_match else "UNKNOWN"

    # Store the extracted information in a dictionary
    parsed_data = {
        "Transaction Code": transaction_code,
        "Transaction Type": transaction_type,
        "Amount": amount,
        "Sender Name": sender_name,
        "Sender Phone": sender_phone,
        "Receiver Name": receiver_name,
        "Receiver Phone": receiver_phone,
        "Receiver Account": receiver_account,
        "Date": date,
        "Time": time,
        "Balance": balance,
        "Transaction Cost": transaction_cost
    }

    return parsed_data

def determine_transaction_type(message):
    if re.search(r'sent to\s+.*\s+for account \w+', message):
        return "merchant_payment"
    elif "received" in message:
        return "received"
    elif re.search(r'You bought Ksh', message):
        return "airtime_purchase"
    elif re.search(r'pay your outstanding Fuliza M-PESA', message):
        return "fuliza_payment"
    elif re.search(r'sent to', message):
        return "sent"
    elif re.search(r'paid to\s+.*\s+on', message):
        return "bill_payment"
    else:
        return "unknown"

def insert_into_database(data):
    # Establish a connection to the database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    try:
        # Define the SQL statement
        sql = "INSERT INTO your_table (transaction_code, transaction_type, amount, sender_name, sender_phone, receiver_name, receiver_phone, receiver_account, date, balance, transaction_cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        # Execute the SQL statement with the extracted data
        cursor.execute(sql, (
            data['Transaction Code'],
            data['Transaction Type'],
            data['Amount'],
            data['Sender Name'],
            data['Sender Phone'],
            data['Receiver Name'],
            data['Receiver Phone'],
            data['Receiver Account'],
            data['Date'],
            data['Balance'],
            data['Transaction Cost']
        ))

        # Commit the changes to the database
        conn.commit()

        print("Data inserted successfully!")
    except Exception as e:
        print("Error:", str(e))
    finally:
        # Close the database connection
        cursor.close()
        conn.close()

# Example usage with the new message
message = input("Enter the M-PESA message here: ")
parsed_data = parse_message(message)
for key, value in parsed_data.items():
    print(key + ":", value)

# Database insertion (if desired)
insert_into_database(parsed_data)

