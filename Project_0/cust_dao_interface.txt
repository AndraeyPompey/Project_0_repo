from abc import ABC, abstractmethod

from entities_customers_bank_account_info.customer_class_information import Customer_name


class CustomerDAOInterface(ABC):

    #create
    @abstractmethod
    def create_customer(self, customer_name:Customer_name)->Customer_name:
        pass

    # read
    @abstractmethod
    def get_cust_information_by_id(self, cust_id_number: int)-> Customer_name:
        pass

    #update
    @abstractmethod
    def update_cust_by_id(self, customer_name:Customer_name)-> Customer_name:
        pass

    #delete
    @abstractmethod
    def delete_cust_by_id(self, cust_id_number: int)-> bool:
        pass