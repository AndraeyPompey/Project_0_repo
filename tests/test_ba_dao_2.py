from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.insufficient_funds_exception import InsufficientFunds
from data_access_layer.bank_account_data_access_object.bank_account_dao_implementation import BankAccountDAOImp
from entities_customers_bank_account_info.customer_class_information import BankAccount
from data_access_layer.bankacc_dao_int_new import BankAccountDAOInterface3
from data_access_layer.bank_account_data_access_object.ba_dao_imp3 import BankAccount3, BankAccountDaoImp3

bank_account_dao: BankAccountDaoImp3 = BankAccountDaoImp3()
test_bank_account_person = BankAccount3(1,1,100.00)

"""Create bank account test"""


def test_create_bank_account_success(): #Figure out how to tie the BA with specific customers
    test_bank_account = BankAccount3(1, 0, 100.00)
    result = bank_account_dao.create_bank_account(test_bank_account)
    assert result.ba_id_number != 0



def test_catch_non_unique_bank_account_id():
    test_bank_account = BankAccount3(1, 1, 200.00)
    result = bank_account_dao.create_bank_account(test_bank_account)
    assert result.ba_id_number != 1


#def test_Zero_money_inside_bank_account():
    #test_bank_account = BankAccount(1, 0, 0)
    #result = bank_account_dao.create_bank_account(test_bank_account)
    #try:
        #bank_account_dao.create_bank_account(test_bank_account)
        #assert False
    #except ZeroFunds as e:
        #assert str(e) == "Please place money inside of your account"






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
    return result

def test_get_all_bank_account_info_by_cust_id_nonexistent():
    try:
        bank_account_dao.get_all_bank_accounts_by_cust_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer account matches this ID number. Try again"



"""update"""

def test_update_account_success():
    new_bank_info = BankAccount3(1,1,300.00)
    result = bank_account_dao.update_bank_account(new_bank_info)
    assert result.balance == 300.00


def test_update_account_cust_id_failure():
    new_bank_info = BankAccount3(0, 1, 300.00)
    try:
        bank_account_dao.update_bank_account(new_bank_info)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"

# def test_update_account_ba_id_failure():
#     new_bank_info = BankAccount3(1, 0, 300.00)
#     try:
#         bank_account_dao.update_bank_account(new_bank_info)
#         assert False
#     except IdNotFound as e:
#         assert str(e) == "No Bank Account matches the id given: please try again"


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
