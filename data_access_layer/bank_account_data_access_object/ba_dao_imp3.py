from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.insufficient_funds_exception import InsufficientFunds
from data_access_layer.bank_account_data_access_object.bank_account_dao_interface import BankAccountDAOInterface
from data_access_layer.bankacc_dao_int_new import BankAccountDAOInterface3
from data_access_layer.customer_data_access_object.customer_dao_implementation import CustomerDaoImplementation
from entities_customers_bank_account_info.new_bank_acc import BankAccount3
from entities_customers_bank_account_info.customer_class_information import Customer_name


class BankAccountDaoImp3(BankAccountDAOInterface):
    bank_account_needed_for_id_catch = BankAccount3(1, 1, 500.00)
    bank_account_needed_for_id_catch2 = BankAccount3(1, 2, 400.00)
    bank_account_needed_for_id_catch3 = BankAccount3(2, 1, 400.00)
    bank_account_needed_for_id_catch4 = BankAccount3(2, 2, 400.00)
    bank_account_list = []
    bank_account_list.append(bank_account_needed_for_id_catch)
    bank_account_list.append(bank_account_needed_for_id_catch2)
    bank_account_list.append(bank_account_needed_for_id_catch3)
    bank_account_list.append(bank_account_needed_for_id_catch4)



    def __init__(self):
        # bank_account_needed_for_id_catch = BankAccount(1, 1, 100)

        #self.bank_account_list = []
        self.id_generator = 2

        # self.bank_account_list.append(bank_account_needed_for_id_catch)
        # self.new_money_amount = new_money_amount

    def create_bank_account(self, bank_account: BankAccount3) -> BankAccount3:# Tie into Customer ID somehow
        # for bank_account in CustomerDaoImplementation.customer_list:
        #     if bank_account.cust_id_number == cust_id_number:
        bank_account.ba_id_number = self.id_generator
        self.id_generator += 1
        self.bank_account_list.append(bank_account)
        return bank_account


    def get_bank_account_info(self, ba_id_number: int) -> BankAccount3:  # Tie into Customer ID somehow
        for bank_account in self.bank_account_list:
            if bank_account.ba_id_number == ba_id_number:
                return bank_account
        raise IdNotFound("No bank account matches this ID number. Try again")

    def get_all_bank_accounts_by_cust_id(self, cust_id_number):
        for bank_account in self.bank_account_list:
            if bank_account.cust_id_number == cust_id_number:
                return BankAccountDaoImp3.bank_account_list[cust_id_number]
            else:
                raise IdNotFound("No customer account matches this ID number. Try again")


    def update_bank_account(self, bank_account: BankAccount3) -> BankAccount3:
        for old_info in self.bank_account_list:
            if bank_account.cust_id_number != old_info.cust_id_number:
                raise IdNotFound("No Customer matches the id given: please try again")
            # if bank_account.ba_id_number != old_info.ba_id_number:
            #     raise IdNotFound("No Bank Account matches the id given: please try again")
            else:
                old_info = bank_account
                return old_info
        # raise IdNotFound("No Customer matches the id given: please try again")


        # bank_account = BankAccountDaoImp3.bank_account_list[bank_account.ba_id_number]
        # return bank_account



    def delete_bank_account_by_id(self, ba_id_number: int) -> bool:  # Tie into Customer ID somehow
        for bank_account in self.bank_account_list:
            if bank_account.ba_id_number == ba_id_number:
                self.bank_account_list.remove(bank_account)
                return True
        raise IdNotFound("No bank account matches this ID number. Try again")

    print(bank_account_list[0])

