from src.main import Item
from src.database import Database


database = Database()
print(database.db.items.insert_one(Item('Test Item').__dict__).inserted_id)
