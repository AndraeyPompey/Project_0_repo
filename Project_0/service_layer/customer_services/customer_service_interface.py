from abc import ABC, abstractmethod
from entities_customers_bank_account_info.customer_class_information import Customer_name
from data_access_layer.customer_data_access_object.customer_dao_interface import CustomerDAOInterface

class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao


    #create
    @abstractmethod
    def service_create_customer(self, customer_name:Customer_name) -> Customer_name:
        pass

    #read
    @abstractmethod
    def service_get_cust_by_id(self, cust_id_number: int) -> Customer_name:
        pass

    #update
    @abstractmethod
    def service_update_cust_by_id(self, customer_name:Customer_name) -> Customer_name:
        pass

    #delete
    @abstractmethod
    def delete_cust_by_id(self, cust_id_number: int) -> bool:
        pass