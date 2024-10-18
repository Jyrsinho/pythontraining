import pytest
from source.bank_account.bank_account import BankAccount, InsufficientFundsError
from source.bank_account.savings_account import SavingsAccount

# import account fixture
from tests.test_bank_account.test_bank_account import bank_account as account  # type: ignore


@pytest.fixture
def savings_account():
    return SavingsAccount("Esther", 1000, interest_rate=0.05)


def test_transfer_reduces_source_and_increases_target_balance(account: BankAccount, savings_account: SavingsAccount):
    account.transfer(savings_account, 300)
    assert account.get_balance() == 200
    assert savings_account.get_balance() == 1300
    
def test_transfer_should_transfer_all_money(account: BankAccount, savings_account: SavingsAccount):
    account.transfer(savings_account, 500)
    assert account.get_balance() == 0
    assert savings_account.get_balance() == 1500
    
def test_transfer_should_throw_error_when_transfering_more_than_balance(account: BankAccount, savings_account: SavingsAccount):
    with pytest.raises(InsufficientFundsError):
        account.transfer(savings_account, 501)
    
def test_transfer_should_throw_error_when_transfering_zero(account: BankAccount, savings_account: SavingsAccount):
    with pytest.raises(ValueError):
        account.transfer(savings_account, 0)
        
def test_transfer_should_throw_error_when_transfering_negative_amounts(account: BankAccount, savings_account: SavingsAccount):
    with pytest.raises(ValueError):
        account.transfer(savings_account, -1)
    

def test_apply_interest_increases_savings_balance(savings_account: SavingsAccount):
    savings_account.apply_interest()
    assert savings_account.get_balance() == 1050


def test_should_not_apply_interest_to_savings_account_if_savings_account_balance_equal_to_zero(savings_account: SavingsAccount):
    savings_account.withdraw(1000)
    savings_account.apply_interest()
    assert savings_account.get_balance() == 0
    

def test_withdraw_reduces_savings_balance(savings_account: SavingsAccount):
    savings_account.withdraw(500)
    assert savings_account.get_balance() == 500


def test_withdraw_raises_error_when_amount_exceeds_balance(savings_account: SavingsAccount):
    with pytest.raises(ValueError):
        savings_account.withdraw(1500)
        
def test_withdraw_does_not_raise_error_when_amount_is_balance(savings_account: SavingsAccount):
    savings_account.withdraw(1000)
    assert savings_account.get_balance() == 0

def test_should_not_apply_interest_for_negative_balance(savings_account: SavingsAccount):
    savings_account.balance = -1000
    savings_account.apply_interest()
    assert savings_account.get_balance() == -1000  

def test_should_not_apply_interest_for_zero_balance(savings_account: SavingsAccount):
    savings_account.balance = 0
    savings_account.apply_interest()
    assert savings_account.get_balance() == 0
    


