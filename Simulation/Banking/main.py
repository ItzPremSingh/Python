from fastapi import FastAPI

from bank.route import bank_route
from common import DB
from user.route import user_route

app = FastAPI()
app.include_router(bank_route)
app.include_router(user_route)

# sql_debug(True)
DB.generate_mapping(create_tables=True)


@app.get("/")
async def main():
    return {"message": "Hello World"}
