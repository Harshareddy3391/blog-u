from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Database_url="mysql+pymysql://root:Harsha%40345@localhost/blogdb"


engine=create_engine(Database_url)


Sessionlocal=sessionmaker(bind=engine)

try:
    connections=engine.connect()
    print("database connected successfully")

except:
    print("Database connection fail...")