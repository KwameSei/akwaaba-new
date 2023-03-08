from models.engine.database import Base, engine
from models.event import All_Event
# from models.models import All_Event
from models.user import User
from models.image import Images
#from models.engine.db_storage import engine, Base

print("Creating database....")

Base.metadata.create_all(engine)
