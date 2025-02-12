import os
from sqlalchemy import create_engine

# Get environment variables
user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')

# Create engine and test connection
try:
    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}')
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")
