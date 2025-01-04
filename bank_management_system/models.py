from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    account_type = Column(String)
    balance = Column(Float, default=0.0)

class Loan(Base):
    __tablename__ = 'loan'
    id = Column(Integer, primary_key=True)
    loan_id = Column(Integer, ForeignKey('customers.id'))
    loan_type = Column(String)
    loan_amount = Column(Float)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Float)
    transaction_type = Column(String)

class Branch(Base):
    __tablename__ = 'branch'
    id = Column(Integer, primary_key=True)
    branch_name = Column(String)
    branch_address = Column(String)

def create_tables(engine):
    Base.metadata.create_all(engine)