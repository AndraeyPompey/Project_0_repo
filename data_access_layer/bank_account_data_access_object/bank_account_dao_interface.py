from abc import ABC, abstractmethod

from entities_customers_bank_account_info.new_bank_acc import BankAccount3


class BankAccountDAOInterface(ABC):

    @abstractmethod
    def create_bank_account(self, bank_account:BankAccount3)->BankAccount3:
        pass

    @abstractmethod
    def get_bank_account_info(self, ba_id_number: int)->BankAccount3:
        pass

    @abstractmethod
    def get_all_bank_accounts_by_cust_id(self, cust_id_number: int)->BankAccount3:
        pass

    @abstractmethod
    def update_bank_account(self, ba_id_number: int)-> BankAccount3:
        pass


    # @abstractmethod
    # def withdraw_funds_by_id(self, cust_id_number: int, ba_id_number: int, withdraw_amount: float)->BankAccount:
    #     pass
    #
    # @abstractmethod
    # def deposit_funds_by_id(self, cust_id_number: int, ba_id_number: int, deposit_amount: float)->BankAccount:
    #     pass

    @abstractmethod
    def delete_bank_account_by_id(self, ba_id_number: int)->bool:
        pass


