from database import create_session
from views import create_customer, create_account, deposit

if __name__ == "__main__":
    session = create_session()

    new_customer = create_customer(session, "Poe Poe", "123 Main St", "+959761200121")
    new_account = create_account(session, new_customer.id, "Savings")
    deposit_success = deposit(session, new_account.id, 1000.0,)

    session.close()