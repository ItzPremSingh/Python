from argparse import ArgumentParser

from functions import connect, insertRecord, lastBalance, listRecord

connection = connect(".database.db")
cursor = connection.cursor()


parser = ArgumentParser(description="Money Tracker")
subparsers = parser.add_subparsers(dest="command", help="Commands")


parserAdd = subparsers.add_parser("add", help="Add a new transaction")
parserAdd.add_argument("amount", type=int, help="Transaction amount")
parserAdd.add_argument("description", type=str, help="Transaction description")
parserAdd.add_argument("type", choices=["credit", "debit"], help="Transaction type")

parserHistory = subparsers.add_parser("history", help="Show the history")
parserHistory.add_argument(
    "-r", "--range", type=int, default=10, help="Show history in range"
)

subparsers.add_parser("balance", help="Get the balance")

args = parser.parse_args()

if args.command == "add":
    amount = args.amount
    balance = lastBalance(cursor)

    if args.type == "debit":
        balance -= amount

    else:
        balance += amount

    insertRecord(cursor, amount, args.description, args.type, balance)

elif args.command == "balance":
    if balance := lastBalance(cursor):
        print(f"Balance: {balance}")

    else:
        print("No transaction done")

elif args.command == "history":
    listRecord(cursor, args.range)

else:
    parser.print_help()


connection.commit()
connection.close()
