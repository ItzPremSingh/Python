from datetime import datetime

from pony.orm import PrimaryKey, Required, Set, db_session

from common import DB
from common.helper import generateUID
from user.models import User


class Transaction(DB.Entity):
    id = PrimaryKey(str)
    amount = Required(float)
    type = Required(str)
    associated = Required(int)
    timestamp = Required(datetime, default=lambda: datetime.now())

    def __str__(self):
        return self.id