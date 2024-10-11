from pony.orm import Database

DB = Database("sqlite", "database.sqlite", create_db=True)
