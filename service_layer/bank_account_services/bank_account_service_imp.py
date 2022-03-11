#from abc import ABC
from abc import ABC

from custom_exceptions.bad_money_input import BadValueInput
from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.insufficient_funds_exception import InsufficientFunds
from data_access_layer.bank_account_data_access_object.ba_dao_imp3 import BankAccountDaoImp3
#from data_access_layer.bankacc_dao_int_new import BankAccountDAOInterface3
from data_access_layer.customer_data_access_object.customer_dao_implementation import CustomerDaoImplementation

from entities_customers_bank_account_info.new_bank_acc import BankAccount3
#from entities_customers_bank_account_info.customer_class_information import Customer_name
from service_layer.bank_account_services.bank_account_service_int import BankAccountServiceInterface3


class BankAccountServiceImp(BankAccountServiceInterface3, ABC):
    bank_account_needed_for_id_catch = BankAccount3(1, 1, 500)
    bank_account_needed_for_id_catch2 = BankAccount3(1, 2, 500)
    bank_account_needed_for_id_catch3 = BankAccount3(2, 1, 500)
    bank_account_needed_for_id_catch4 = BankAccount3(2, 2, 500)
    bank_account_list = []
    bank_account_list.append(bank_account_needed_for_id_catch)
    bank_account_list.append(bank_account_needed_for_id_catch2)
    bank_account_list.append(bank_account_needed_for_id_catch3)
    bank_account_list.append(bank_account_needed_for_id_catch4)
    id_generator = 2
    ba_dao_imp = BankAccountDaoImp3
    cust_dao_imp = CustomerDaoImplementation

    def __init__(self, bank_dao):
        self.bank_dao: BankAccountDaoImp3 = bank_dao


    def add_new_bank_account(self, bank_account: BankAccount3) -> BankAccount3:  # Tie into Customer ID somehow
        return self.bank_dao.create_bank_account(bank_account)






    def get_bank_account_info(self, ba_id_number: int) -> BankAccount3:  # Tie into Customer ID somehow
        return self.bank_dao.get_bank_account_info(ba_id_number)

    def get_all_bank_accounts_by_cust_id(self, cust_id_number: int) -> BankAccount3:
        return self.bank_dao.get_all_bank_accounts_by_cust_id(cust_id_number)

    def update_bank_account(self, bank_account: BankAccount3) -> BankAccount3:
        return self.bank_dao.update_bank_account(bank_account)

    def withdraw_funds_by_id(self, cust_id_number: int, ba_id_number: int, withdraw_amount: float):
        account = self.bank_dao.get_bank_account_info(ba_id_number)
        if account.cust_id_number != cust_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        if account.ba_id_number != ba_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        elif type(withdraw_amount) != float:
            raise BadValueInput("This transaction could not be processed. Try again")
        # elif account.balance - withdraw_amount < 0:
        #     raise InsufficientFunds("This transaction could not be processed. Try again")
        elif withdraw_amount < 0:
            raise InsufficientFunds("This transaction could not be processed. Try again")
        else:
            account.balance = account.balance - withdraw_amount
            return self.bank_dao.update_bank_account(account) #CREATE AN UPDATE

    def deposit_funds_by_id(self, cust_id_number: int, ba_id_number: int, deposit_amount: float):
        account = self.bank_dao.get_bank_account_info(ba_id_number)
        if account.cust_id_number != cust_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        if account.ba_id_number != ba_id_number:
            raise IdNotFound("No bank account matches this ID number. Try again")
        if type(deposit_amount) != float:
            raise BadValueInput("This transaction could not be processed. Try again")
        if deposit_amount < 0:
            raise InsufficientFunds("This transaction could not be processed. Try again")
        if account.balance + deposit_amount < 0:
            raise InsufficientFunds("This transaction could not be processed. Try again")
        else:
            account.balance = account.balance + deposit_amount
            return self.bank_dao.update_bank_account(account)  # CREATE AN UPDATE

    def transfer_funds_by_ids(self, cust_id_number: int, ba_id_number1: int, ba_id_number2: int, transfer_amount: float):
        self.withdraw_funds_by_id(cust_id_number,ba_id_number1, transfer_amount)
        self.deposit_funds_by_id(cust_id_number,ba_id_number2,transfer_amount)
        return "Transfer complete"

    def delete_bank_account_by_id(self, ba_id_number: int) -> bool:  # Tie into Customer ID somehow
        for bank_account in self.bank_account_list:
            if bank_account.ba_id_number == ba_id_number:
                self.bank_account_list.remove(bank_account)
                return True
        raise IdNotFound("No bank account matches this ID number. Try again")

    print(bank_account_list)
