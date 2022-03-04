from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.zero_funds_exception import ZeroFunds
from data_access_layer.bank_account_data_access_object.bank_account_dao_interface import BankAccountDAOInterface
from entities_customers_bank_account_info.customer_class_information import BankAccount


class BankAccountDAOImp(BankAccountDAOInterface):

    def __init__(self):
        bank_account_needed_for_id_catch = BankAccount(1, 1, 100)

        self.bank_account_list = []
        self.id_generator = 2
        self.bank_account_list.append(bank_account_needed_for_id_catch)
        self.new_money_amount = new_money_amount







    def create_bank_account(self, bank_account: BankAccount) -> BankAccount:  #Tie into Customer ID somehow
        bank_account.ba_id_number = self.id_generator
        self.id_generator += 1
        self.bank_account_list.append(bank_account)
        return bank_account

    def get_bank_account_info(self, ba_id_number: int) -> BankAccount: #Tie into Customer ID somehow
        for bank_account in self.bank_account_list:
            if bank_account.ba_id_number == ba_id_number:
                return bank_account
        raise IdNotFound("No bank account matches this ID number. Try again")

    def withdraw_funds_by_id(self, bank_account: BankAccount) -> BankAccount: #Tie into Customer ID somehow
        for new_money_amount in self.bank_account_list:
            if bank_account.ba_id_number == new_money_amount.ba_id_number:
                withdraw_amount = float(input()) #Make this flexible
                new_money_amount.money_amount = bank_account.money_amount - withdraw_amount
                return new_money_amount #is this replacing the value in the list
        raise IdNotFound("No bank account matches this ID number. Try again")


    def deposit_funds_by_id(self, bank_account: BankAccount) -> BankAccount: #Tie into Customer ID somehow
        for new_money_amount in self.bank_account_list:
            if bank_account.ba_id_number == new_money_amount.ba_id_number:
                deposit_amount = float(input())
                new_money_amount.money_amount = bank_account.money_amount + deposit_amount
                return new_money_amount  # is this replacing the value in the list
        raise IdNotFound("No bank account matches this ID number. Try again")

    def delete_bank_account_by_id(self, ba_id_number: int) -> bool: #Tie into Customer ID somehow
        for bank_account in self.bank_account_list:
            if bank_account.ba_id_number == ba_id_number:
                self.bank_account_list.remove(bank_account)
                return True
        raise IdNotFound("No bank account matches this ID number. Try again")


