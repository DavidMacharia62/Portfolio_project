# Portfolio_project
A portfolio project delivered as part of the requirements for my Software Engineering course.

---

# M-PESA Message Parsing Tool

## Overview

The M-PESA Message Parsing Tool is a Python-based utility designed to parse and extract relevant information from M-PESA transaction messages. M-PESA is a mobile phone-based money transfer service widely used in Kenya and other countries. This tool aims to facilitate the extraction of essential transaction details, such as transaction type, amount, sender, receiver, date, and time, from raw M-PESA messages.

## Features

- **Message Parsing**: Extracts transaction details from raw M-PESA messages.
- **Transaction Type Detection**: Automatically determines the type of transaction (e.g., sent, received, bill payment, merchant payment).
- **Sender and Receiver Identification**: Identifies the sender and receiver of the transaction.
- **Handling of Various Message Formats**: Accommodates different message formats commonly used in M-PESA transactions.
- **Database Storage**: Stores parsed transaction data in a SQLite database for easy retrieval and analysis.
- **Command-Line Interface (CLI)**: Provides a user-friendly interface for parsing M-PESA messages.
- **Bash Scripting Support**: Allows automation of message parsing tasks using bash scripts.

## Technologies Used

- **Python**: Core programming language for developing the parsing logic and CLI.
- **Regular Expressions (Regex)**: Used for pattern matching and extracting relevant information from messages.
- **SQLite**: Lightweight relational database management system for storing parsed transaction data.
- **Command-Line Interface (CLI)**: Enables interaction with the tool via the command line.
- **Bash Scripting**: Supports automation of parsing tasks across multiple messages.

## Usage

1. **Installation**: Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your_username/mpesa-message-parser.git
   ```

2. **Dependencies**: Install the required Python dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. **Execution**: Run the parsing tool by providing M-PESA messages as input.

   ```bash
   python parse_mpesa_message.py
   ```

4. **Batch Processing**: Utilize bash scripts to automate parsing tasks for multiple messages.

   ```bash
   ./parse_messages.sh messages_directory
   ```

## Example

Consider the following M-PESA message:

```
RGG6NT5CAW Confirmed. Ksh130.00 paid to NEWTON WANYAMA NGUTUKU. on 16/7/23 at 11:50 AM.New M-PESA balance is Ksh1,266.16. Transaction cost, Ksh0.00.
```

After parsing, the tool will output:

```
Transaction Code: RGG6NT5CAW
Transaction Type: bill_payment
Amount: 130.00
Sender Name: YOU
Sender Phone: N/A
Receiver Name: NEWTON WANYAMA NGUTUKU.
Receiver Phone: UNKNOWN
Receiver Account: UNKNOWN
Date: 16/7/23
Time: 11:50 AM
Balance: 1266.16
Transaction Cost: 0.00
```

## Contributors

- [Your Name](https://github.com/your_username)
- [Contributor 1](https://github.com/contributor1)
- [Contributor 2](https://github.com/contributor2)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
