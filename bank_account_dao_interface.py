from abc import ABC, abstractmethod

from entities_customers_bank_account_info.customer_class_information import BankAccount


class BankAccountDAOInterface(ABC):

    @abstractmethod
    def create_bank_account(self, bank_account:BankAccount)->BankAccount:
        pass

    @abstractmethod
    def get_bank_account_info(self, ba_id_number: int)->BankAccount:
        pass

    @abstractmethod
    def withdraw_funds_by_id(self, bank_account:BankAccount)->BankAccount:
        pass

    @abstractmethod
    def deposit_funds_by_id(self, bank_account: BankAccount)->BankAccount:
        pass

    @abstractmethod
    def delete_bank_account_by_id(self, ba_id_number: int)->bool:
        pass


