from fastapi import APIRouter, Depends
from pony.orm import db_session

from user import authenticate
from bank.models import Transaction, User

account_route = APIRouter()


@account_route.get("/account/{number}")
async def account(number: int, current_user: str = Depends(authenticate)):
    with db_session:
        user = User.get(account=number)
        if user:
            return {"users": user.username}
        return {"message": "account does not exist"}


@account_route.get("/balance/{number}")
async def balance(number: int, current_user: str = Depends(authenticate)):
    with db_session:
        user = User.get(account=number)
        if user:
            return {"balance": user.balance}
        return {"message": "account does not exist"}


@account_route.get("/transactions/{number}")
async def transactions(number: int, current_user: str = Depends(authenticate)):
    with db_session:
        user = User.get(account=number)
        if user:
            transList = []
            transactions = user.transactions
            if transactions:
                for transaction in transactions:
                    transList.append(
                        (
                            transaction.amount,
                            transaction.type,
                            transaction.associated,
                            transaction.timestamp,
                        )
                    )

            return {"transactions": transList}
        return {"message": "account does not exist"}


@account_route.post("/deposit")
async def deposit(
    number: int, amount: float, current_user: str = Depends(authenticate)
):
    with db_session:
        user = User.get(account=number)
        if user:
            user.balance += amount
            Transaction.create(
                user=user, amount=amount, type="deposit", associated=number
            )
            return {"message": "deposit successful"}
        return {"message": "account does not exist"}


@account_route.post("/withdraw")
async def withdraw(
    number: int, amount: float, current_user: str = Depends(authenticate)
):
    with db_session:
        user = User.get(account=number)
        if user:
            if user.balance < amount:
                return {"message": "insufficient balance"}
            user.balance -= amount
            Transaction.create(
                user=user, amount=amount, type="withdraw", associated=number
            )
            return {"message": "withdraw successful"}
        return {"message": "account does not exist"}


@account_route.post("/transfer")
async def transfer(
    from_number: int,
    to_number: int,
    amount: float,
    current_user: str = Depends(authenticate),
):
    with db_session:
        from_user = User.get(account=from_number)
        to_user = User.get(account=to_number)
        if from_user and to_user:
            if from_user.balance < amount:
                return {"message": "insufficient balance"}
            from_user.balance -= amount
            to_user.balance += amount
            Transaction.create(
                user=from_user, amount=amount, type="transfer", associated=from_number
            )
            Transaction.create(
                user=to_user, amount=amount, type="receive", associated=to_number
            )
            return {"message": "transfer successful"}
        return {"message": "account does not exist"}


@account_route.post("/details")
async def details(number: int, current_user: str = Depends(authenticate)):
    with db_session:
        user = User.get(account=number)
        if user:
            return {
                "username": user.username,
                "balance": user.balance,
            }
        return {"message": "account does not exist"}


@account_route.post("/all_accounts")
async def all_accounts(current_user: str = Depends(authenticate)):
    print(type(current_user))
    with db_session:
        users = User.select()
        return {"users": [(user.account, user.username) for user in users]}
