from fastapi import FastAPI

from account.route import accountRouter
from house.route import houseRouter

from common.db import DB

app = FastAPI()
app.include_router(houseRouter)
app.include_router(accountRouter)

DB.generate_mapping(create_tables=True)


@app.get("/")
async def main():
    return {"message": "Hello, World!"}
