import sqlite3

# preparation for local saving of previously interacted with media
class InstaPy2DB:
    def __init__(self, database: str = None):
        print('[INFO]: Initialized InstaPy2DB')
        self.database = database
    
    def connect(self):
        self.connect = sqlite3.connect(database=self.database)