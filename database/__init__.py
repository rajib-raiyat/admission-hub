from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a PostgreSQL database engine
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/admission_hub_db')

# Create a Session class to handle database interactions
Session = sessionmaker(bind=engine)

# Use the Session class to create a session object
session = Session()


if __name__ == '__main__':
    print(session)
