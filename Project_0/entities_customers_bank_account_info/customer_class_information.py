class Customer_name:
    def __init__(self, first_name: str, last_name: str, cust_id_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.cust_id_number = cust_id_number

    def convert_to_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "custIdNumber": self.cust_id_number
        }


        #class BankAccount:
           # def __init__(self, Customer_name, ba_id_number: int, money_amount: int):
               # self.Customer_name = Customer_name

        # I need a first name and a last name


#whats a customer?
"""
Customers have first names.
Customers have last names.
Customers have id numbers.
Customers have bank accounts.

the account information will be separate, so I need to focus on the name and id number
"""


class BankAccount:

    def __init__(self, cust_id_number: int, ba_id_number: int, money_amount: float):
        self.ba_id_number = ba_id_number
        self.cust_id_number = cust_id_number
        self.money_amount = money_amount





