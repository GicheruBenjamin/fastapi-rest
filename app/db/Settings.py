
'''
Settings for database
Get DATABASE_URL from .env file
create a connection to the database
And migrate the models in .Models into the database
'''

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .Models import Base

load_dotenv()

def InitDb():
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Db = sessionmaker(bind=engine)
    db = Db()
    return db
