
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
    with pytest.raises(InsufficientFundsError, match= "^Insufficient funds$"):
        account.transfer(savings_account, 501)

def test_transfer_should_throw_error_when_transfering_zero(account: BankAccount, savings_account: SavingsAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
        account.transfer(savings_account, 0)

def test_transfer_should_throw_error_when_transfering_negative_amounts(account: BankAccount, savings_account: SavingsAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
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
    with pytest.raises(ValueError, match= "^Cannot withdraw more than €1000 from savings$"):
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


def test_should_return_string_representation_of_bank_account(savings_account: SavingsAccount):
    assert savings_account.__str__() == "Esther's account balance is 1000"


def test_should_return_same_amount_when_applied_interest_rate_zero(savings_account: SavingsAccount):
    savings_account.interest_rate = 0.0
    savings_account.apply_interest()
    assert savings_account.get_balance() == 1000

def test_withdraw_raises_error_for_zero_amount(savings_account: SavingsAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
        savings_account.withdraw(0)

def test_withdraw_raises_error_for_negative_amount(savings_account: SavingsAccount):
    with pytest.raises(ValueError, match= "^Withdrawal amount must be positive$"):
        savings_account.withdraw(-5)

def test_should_apply_interest_with_values_less_than_one_but_greater_than_zero(savings_account: SavingsAccount):
    savings_account.balance =1.0
    savings_account.apply_interest()
    assert savings_account.get_balance() == 1.05