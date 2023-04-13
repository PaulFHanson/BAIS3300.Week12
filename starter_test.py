import pytest
from oop_loan_pmt import Loan, collectLoanDetails, main 


# Unit Tests
def test_loan_initialization():
    loan = Loan(100000, 30, 0.06)
    assert loan.loanAmount == 100000
    assert loan.annualRate == 0.06
    assert loan.numberOfPmts == 360
    assert loan.periodicIntRate == 0.005


def test_discount_factor_calculation():
    loan = Loan(100000, 30, 0.06)
    loan.calculateDiscountFactor()
    assert loan.discountFactor == pytest.approx(166.7916, rel=1e-4)


def test_loan_payment_calculation():
    loan = Loan(100000, 30, 0.06)
    loan.calculateLoanPmt()
    assert loan.loanPmt == pytest.approx(599.55, rel=1e-2)


 #Functional Test
def test_main_function(capsys, monkeypatch):
    input_values = [10000, 30, 0.06]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    print("\r")
    print(" -- collectUserDetails functional test")
    loan = collectLoanDetails()
    assert loan.loanAmount == 10000
    assert loan.numberOfPmts == 360
    assert loan.annualRate == 0.06
