from custom_exceptions.bad_customer_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from entities_customers_bank_account_info.customer_class_information import Customer_name
from service_layer.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

#create

    def service_create_customer(self, customer_name:Customer_name) -> Customer_name:
        if type(customer_name.first_name) != str:
            raise BadCustomerInfo("Please pass in a valid first name")
        elif len(customer_name.first_name) >= 20:
            raise BadCustomerInfo("Please pass in a valid first name")
        elif type(customer_name.last_name) != str:
            raise BadCustomerInfo("Please pass in a valid last name")
        elif len(customer_name.last_name) >= 20:
            raise BadCustomerInfo("Please pass in a valid last name")
        return self.customer_dao.create_customer(customer_name)

    #read

    def service_get_cust_by_id(self, cust_id_number: int) -> Customer_name:
        try:
            return self.customer_dao.get_cust_information_by_id(int(cust_id_number)) #LOOK UP NOTES
        except ValueError:
            raise BadCustomerInfo("No Customer matches the id given: please try again")

        #if type(cust_id_number) == int:
            #return self.customer_dao.get_cust_information_by_id(int(cust_id_number)) #CHECK BACK ON NOTES
       # else:
            #raise IdNotFound("No Customer matches the id given: please try again")

    #update

    def service_update_cust_by_id(self, customer_name:Customer_name) -> Customer_name:
        if type(customer_name.first_name) != str:
            raise BadCustomerInfo("Please pass in a valid first name")
        elif type(customer_name.last_name) != str:
            raise BadCustomerInfo("Please pass in a valid last name")
        return self.customer_dao.update_cust_by_id(customer_name)


#delete

    def delete_cust_by_id(self, cust_id_number: int) -> bool:
        if type(cust_id_number) == int:
            return self.customer_dao.delete_cust_by_id(cust_id_number)
        else:
            raise IdNotFound("No Customer matches the id given: please try again")

