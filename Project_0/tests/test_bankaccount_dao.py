from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.zero_funds_exception import ZeroFunds
from data_access_layer.bank_account_data_access_object.bank_account_dao_implementation import BankAccountDAOImp
from entities_customers_bank_account_info.customer_class_information import BankAccount

bank_account_dao = BankAccountDAOImp()
test_bank_account_person = BankAccount(1,1,100)

"""Create bank account test"""


def test_create_bank_account_success(): #Figure out how to tie the BA with specific customers
    test_bank_account = BankAccount(1, 0, 200)
    result = bank_account_dao.create_bank_account(test_bank_account)
    assert result.ba_id_number != 0
    #assert result.money_amount != 0


def test_catch_non_unique_bank_account_id():
    test_bank_account = BankAccount(1, 1, 200)
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


"""update"""
#FIX THESE COMPLETELY BROKEN

def test_deposit_funds_by_bank_account_id_success():

    #deposit_amount: float = 50
    if deposit_amount >= 0:
        result = bank_account_dao.deposit_funds_by_id(test_bank_account_person)
        print(result)
        return result.money_amount == 15
    else:
        print("This request could not be processed. Please try again")



def test_deposit_funds_by_bank_account_id_failure():
    deposit_amount: float = -47
    if deposit_amount >= 0:
        return True
    else:
        print("This request could not be processed. Please try again")



def test_withdraw_funds_by_bank_account_id_success():
    old_money_amount = test_bank_account_person
    withdraw_amount = 20
    if old_money_amount.money_amount >= withdraw_amount:
        if withdraw_amount >= 0 and withdraw_amount == float:
            return True
    else:
        print("This request could not be processed. Please try again")




def test_withdraw_funds_by_bank_account_id_failure():
    old_money_amount = test_bank_account_person
    withdraw_amount = 200
    if old_money_amount.money_amount >= withdraw_amount and withdraw_amount == float:
        if withdraw_amount >= 0:
            return True
    else:
        print("This request could not be processed. Please try again")



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
