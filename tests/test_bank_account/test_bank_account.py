import pytest
from source.bank_account.bank_account import BankAccount, InsufficientFundsError


@pytest.fixture
def bank_account():
    return BankAccount("Esther", 500)

@pytest.fixture
def bank_account2():
    return BankAccount("Timo", 500)

def test_deposit_increases_balance(bank_account: BankAccount):
    bank_account.deposit(200)
    assert bank_account.get_balance() == 700
    

def test_deposit_raises_error_for_negative_amount(bank_account: BankAccount):
    with pytest.raises(ValueError, match= "^Deposit amount must be positive$"):
        bank_account.deposit(-100)

def test_deposit_raises_error_for_barely_negative_amount(bank_account: BankAccount):
    with pytest.raises(ValueError, match= "^Deposit amount must be positive$"):
        bank_account.deposit(-1)
        
        
def test_deposit_raises_error_for_zero_amount(bank_account: BankAccount):
    with pytest.raises(ValueError, match= "^Deposit amount must be positive$"):
        bank_account.deposit(0)


def test_withdraw_decreases_balance(bank_account: BankAccount):
    bank_account.withdraw(200)
    assert bank_account.get_balance() == 300
    
def test_withdraws_all_the_money(bank_account: BankAccount):
    bank_account.withdraw(500)
    assert bank_account.get_balance() == 0


def test_withdraw_raises_error_for_insufficient_funds(bank_account: BankAccount):
    with pytest.raises(InsufficientFundsError, match= "^Insufficient funds$"):
        bank_account.withdraw(600)
        
        
def test_withdraw_does_not_raise_error_for_insufficient_funds_if_balance_zero_after_withdraw(bank_account: BankAccount):
    bank_account.withdraw(500)
    assert bank_account.get_balance() == 0


def test_withdraw_raises_error_for_negative_amount(bank_account: BankAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
        bank_account.withdraw(-100)
        
def test_withdraw_raises_error_for_zero_amount(bank_account: BankAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
        bank_account.withdraw(0)
        
def test_transfer_should_raise_error_when_transfering_more_money_than_current_balance(bank_account: BankAccount, bank_account2: BankAccount):
    with pytest.raises(InsufficientFundsError, match= "^Insufficient funds$"):
        bank_account.transfer(bank_account2, 600)
        
def test_transfer_should_raise_error_when_transfering_amount_of_zero(bank_account: BankAccount, bank_account2: BankAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
        bank_account.transfer(bank_account2, 0)
        
def test_transfer_should_raise_error_when_transfering_amount_is_negative(bank_account: BankAccount, bank_account2: BankAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
        bank_account.transfer(bank_account2, -600)

def test_should_return_string_representation_of_bank_account(bank_account: BankAccount):
    assert bank_account.__str__() == "Esther's account balance is 500"


def test_transfer_with_insufficient_funds_by_one(bank_account: BankAccount, bank_account2: BankAccount):
    with pytest.raises(InsufficientFundsError, match= "^Insufficient funds$"):
        bank_account.transfer(bank_account2, 501)