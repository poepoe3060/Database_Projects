from models import Customer, Account, Transaction

def create_customer(session, name, address, phone):
    existing_customer = session.query(Customer).filter_by(name=name, phone=phone).first()
    if existing_customer:
        return existing_customer
    new_customer = Customer(name=name, address=address, phone=phone)
    session.add(new_customer)
    session.commit()
    return new_customer


def create_account(session, customer_id, account_type):
    existing_account = session.query(Account).filter_by(customer_id=customer_id, account_type=account_type).first()
    if existing_account:
        return existing_account
    new_account = Account(customer_id=customer_id, account_type=account_type)
    session.add(new_account)
    session.commit()
    return new_account


def deposit(session, account_id, amount):
    existing_transaction = session.query(Transaction).filter_by(account_id=account_id, amount=amount, transaction_type='Deposit').first()
    if existing_transaction:
        return False
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        account.balance += amount
        new_transaction = Transaction(account_id=account_id, amount=amount, transaction_type='Deposit')
        session.add(new_transaction)
        session.commit()
        return True
    else:
        return False

def create_loan(session, account_id, amount):
    existing_loan = session.query(Transaction).filter_by(account_id=account_id, amount=amount, transaction_type='Loan').first()
    if existing_loan:
        return False
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        account.balance += amount
        new_transaction = Transaction(account_id=account_id, amount=amount, transaction_type='Loan')
        session.add(new_transaction)
        session.commit()
        return True
    else:
        return False
