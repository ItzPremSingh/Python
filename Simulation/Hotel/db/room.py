from common import database
from ....Package.myorm.type import int, Text, Float, Date


class Room(database.Model):
    number = Int(primaryKey=True, autoIncrement=True)
    type = Text()
    capacity = Int()
    price = Float()
    isAvailable = Int(default=1)
    checkInDateTime = Date()
