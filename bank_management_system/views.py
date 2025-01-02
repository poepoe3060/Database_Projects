from models import Customer, Account, Transaction

def create_customer(session, name, address, phone):
    new_customer = Customer(name=name, address=address, phone=phone)
    session.add(new_customer)
    session.commit()
    return new_customer

def create_account(session, customer_id, account_type):
    new_account = Account(customer_id=customer_id, account_type=account_type)
    session.add(new_account)
    session.commit()
    return new_account

def deposit(session, account_id, amount):
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        account.balance += amount
        new_transaction = Transaction(account_id=account_id, amount=amount, transaction_type='Deposit')
        session.add(new_transaction)
        session.commit()
        return True
    else:
        return False