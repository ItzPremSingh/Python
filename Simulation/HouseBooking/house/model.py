from secrets import randbelow

from pony.orm import PrimaryKey, Required, Set, db_session

from account.model import Account
from common import DB


class House(DB.Entity):
    id = PrimaryKey(int)
    owner = Set("Account", reverse="houses")
    floor = Required(int)
    room = Required(int)
    address = Required(str)
    description = Required(str)
    roomPrice = Required(int)

    def __str__(self):
        return self.owner

    @classmethod
    def create(
        cls,
        owner: Account,
        floor: int,
        room: int,
        address: str,
        description: str,
        roomPrice: int,
    ):
        with db_session:
            return cls(
                id=randbelow(1000),
                owner=owner,
                floor=floor,
                room=room,
                address=address,
                description=description,
                roomPrice=roomPrice,
            )
