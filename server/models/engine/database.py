from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
from os import getenv

# load_dotenv()
#from models.base_model import BaseModel

MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PWD = getenv("MYSQL_PWD")
MYSQL_DB = getenv("MYSQL_DB")

engine = create_engine(
    "mysql+mysqldb://Nat:NATSEIKWA510@localhost/akwaaba_db",
    echo=True
)
# connection = engine.connect()

Base=declarative_base()

Session = sessionmaker(bind=engine)
session = Session()