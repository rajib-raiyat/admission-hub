from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a PostgreSQL database engine
engine = create_engine('postgresql+psycopg2://hello_flask:hello_flask@localhost:5432/hello_flask_dev')

# Create a Session class to handle database interactions
Session = sessionmaker(bind=engine)

# Use the Session class to create a session object
session = Session()
