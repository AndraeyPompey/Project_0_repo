from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_data_access_object.customer_dao_interface import CustomerDAOInterface
from entities_customers_bank_account_info.customer_class_information import Customer_name


class CustomerDaoImplementation(CustomerDAOInterface):

    customer_list = []
    #id_generator = 2


    def __init__(self):
        cust_needed_for_id_catch = Customer_name("Bill", "Johnson", 1)

        self.customer_list = []
        self.id_generator = 2
        self.customer_list.append(cust_needed_for_id_catch)




    def create_customer(self, customer_name: Customer_name)->Customer_name:
        #cust needs to be given an Id, and added to the list
        customer_name.cust_id_number = self.id_generator
        self.id_generator += 1
        self.customer_list.append(customer_name)
        return customer_name



    def get_cust_information_by_id(self, cust_id_number: int)->Customer_name:
        for customer_name in self.customer_list:
            if customer_name.cust_id_number == cust_id_number:
                return customer_name
        raise IdNotFound("No Customer matches the id given: please try again")


    def update_cust_by_id(self, customer_name: Customer_name)->Customer_name:
        for old_customer in self.customer_list:
            if customer_name.cust_id_number == old_customer.cust_id_number:
                old_customer = customer_name
                return old_customer
        raise IdNotFound("No Customer matches the id given: please try again")

    def delete_cust_by_id(self, cust_id_number: int)-> bool:
        for customer_name in self.customer_list:
            if customer_name.cust_id_number == cust_id_number:
                self.customer_list.remove(customer_name)
                return True
        raise IdNotFound("No Customer matches the id given: please try again")




