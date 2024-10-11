from common import database
from ....Package.myorm.type import Int, Text

class User(database.Model):
    id = Int(primaryKey=True, autoIncrement=True)
    name = Text()
    email = Text(unique=True)
    phone = Text()
    password = Text()