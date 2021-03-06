from custom_exceptions.bad_money_input import BadValueInput
from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.insufficient_funds_exception import InsufficientFunds
from data_access_layer.bank_account_data_access_object.bank_account_dao_implementation import BankAccountDAOImp
from entities_customers_bank_account_info.customer_class_information import BankAccount
from data_access_layer.bankacc_dao_int_new import BankAccountDAOInterface3
from data_access_layer.bank_account_data_access_object.ba_dao_imp3 import BankAccount3, BankAccountDaoImp3
from service_layer.bank_account_services.bank_account_service_imp import BankAccountServiceImp

bank_account_dao = BankAccountDaoImp3()
bank_account_service = BankAccountServiceImp(bank_account_dao)
test_bank_account_person = BankAccount3(1,1,100.00)

"""Create bank account test"""



def test_add_new_bank_account():
    test_bank_account = BankAccount3(1, 0, 100)
    result = bank_account_dao.create_bank_account(test_bank_account)
    assert result.ba_id_number != 0

"""Get bank account info"""


def test_get_bank_account_info_by_bank_account_id_success():
    result = bank_account_dao.get_bank_account_info(1)
    assert result.ba_id_number == 1


def test_get_bank_account_info_by_bank_account_id_nonexistent():
    try:
        bank_account_dao.get_bank_account_info(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"

def test_get_all_bank_account_info_by_cust_id_success():
    result = bank_account_dao.get_all_bank_accounts_by_cust_id(1)
    assert result.cust_id_number == 1

def test_get_all_bank_account_info_by_cust_id_nonexistent():
    try:
        bank_account_dao.get_all_bank_accounts_by_cust_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer account matches this ID number. Try again"

"""update"""
#FIX THESE COMPLETELY BROKEN

def test_deposit_funds_by_bank_account_id_success():
    result = bank_account_service.deposit_funds_by_id(1,1,50.00)
    assert result


def test_deposit_funds_by_bank_account_id_failure():
    try:
        bank_account_service.deposit_funds_by_id(1,3,50.00)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"

def test_deposit_funds_with_negative_amount():
    try:
        bank_account_service.deposit_funds_by_id(1, 1, -50.00)
        assert False
    except InsufficientFunds as e:
        assert str(e) == "This transaction could not be processed. Try again"

def test_withdraw_funds_with_string():
    try:
        bank_account_service.deposit_funds_by_id(1, 1, "string")
        assert False
    except BadValueInput as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_withdraw_funds_by_bank_account_id_success():
    result = bank_account_service.withdraw_funds_by_id(1, 1, 50.00)
    assert result


def test_withdraw_funds_by_bank_account_id_failure():
    try:
        bank_account_service.withdraw_funds_by_id(1,3,50.00)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"

def test_withdraw_funds_with_negative_amount():
    try:
        bank_account_service.withdraw_funds_by_id(1, 1, -50.00)
        assert False
    except InsufficientFunds as e:
        assert str(e) == "This transaction could not be processed. Try again"

def test_deposit_funds_with_string():
    try:
        bank_account_service.deposit_funds_by_id(1, 1, "string")
        assert False
    except BadValueInput as e:
        assert str(e) == "This transaction could not be processed. Try again"


def test_transfer_funds_success():
    result = bank_account_service.transfer_funds_by_ids(1,1,2,50.00)
    return result

def test_transfer_funds_with_bad_cust_id():
    try:
        bank_account_service.transfer_funds_by_ids(0, 1, 2, 50.0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"

def test_transfer_funds_with_bad_ba_id_1():
    try:
        bank_account_service.transfer_funds_by_ids(1, 90, 2, 50.0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"

def test_transfer_funds_with_bad_ba_id_2():
    try:
        bank_account_service.transfer_funds_by_ids(1, 1, 90, 50.0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"

def test_transfer_funds_with_negative():
    try:
        bank_account_service.transfer_funds_by_ids(1, 1, 2, -50.0)
        assert False
    except InsufficientFunds as e:
        assert str(e) == "This transaction could not be processed. Try again"

def test_transfer_funds_with_string():
    try:
        bank_account_service.transfer_funds_by_ids(1, 1, 90, "STRING")
        assert False
    except BadValueInput as e:
        assert str(e) == "This transaction could not be processed. Try again"








"""Delete"""


def test_delete_bank_account_by_id_success():
    result = bank_account_dao.delete_bank_account_by_id(1)
    assert result


def test_delete_bank_account_by_id_failure():
    try:
        bank_account_dao.delete_bank_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No bank account matches this ID number. Try again"