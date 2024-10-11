from fastapi import APIRouter

from account.model import Account

from .model import House

houseRouter = APIRouter(prefix="/house/v1")


@houseRouter.post("/create/house/")
async def createHouse(
    floor: int, room: int, address: str, description: str, roomPrice: int
):
    House.create(
        Account.get(name="admin"),
        floor,
        room,
        address,
        description,
        roomPrice,
    )
    return {"message": "house created"}


@houseRouter.get("/search/room/")
async def searchRoom():
    return {"message": "Search room"}


@houseRouter.get("/search/house/")
async def searchHouse():
    return {"message": "Search house"}


@houseRouter.get("/book/room/")
async def bookRoom():
    return {"message": "Book room"}


@houseRouter.get("/add/room/")
async def addRoom():
    return {"message": "Add room"}


@houseRouter.get("/add/bathroom/")
async def addBathroom():
    return {"message": "Add bathroom"}


@houseRouter.get("/add/kichen/")
async def addKichen():
    return {"message": "Add kichen"}
