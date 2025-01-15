from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, create_tables

def create_session():
    engine = create_engine('postgresql://sai:sai@localhost:5433/bank_management_system')
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session