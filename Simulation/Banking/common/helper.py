from uuid import uuid4


def generateUID() -> str:
    """generate unique id for user"""

    return str(uuid4())
