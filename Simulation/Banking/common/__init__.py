from pony.orm import Database

DB = Database()
DB.bind(provider="sqlite", filename="sqlite.db", create_db=True)