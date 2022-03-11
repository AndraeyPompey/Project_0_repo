from custom_exceptions.id_not_found import IdNotFound


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

        #def __init__(self, cust_id_number: int, ba_id_number: int, money_amount: float):
            #self.ba_id_number = ba_id_number
            #self.cust_id_number = cust_id_number
            #self.money_amount = money_amount


# whats a customer?
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




class BankAccount2:

    def __init__(self, id_number):
        self.id_number = id_number
        self.balance = 0

    def deposit_funds(self, id_number):
        if self.id_number == id_number:
            amount=float
            self.balance += amount
            return self.balance
        else:
            raise IdNotFound("No bank account matches this ID number. Try again")

    def withdraw_funds(self, id_number):
        if self.id_number == id_number:
            amount=float
            self.balance += amount
            return self.balance
        else:
            raise IdNotFound("No bank account matches this ID number. Try again")

# try:
    #     cust_data: dict = request.get_json()
    #     customer = Customer_name(cust_data["firstName"], cust_data["lastName"], cust_data["custIdNumber"])
    #     result = cust_service.service_create_customer(customer)
    #     result_dictionary = result.convert_to_dictionary()
    #     result_json = jsonify(result_dictionary)
    #     return result_json, 201
    # except BadCustomerInfo as e:
    #     message = {
    #         "message":str(e)
    #     }
    #     return jsonify(message), 400
    # except IdNotFound as e:
    #     message = {
    #         "message":str(e)
    #     }
    #     return jsonify(message), 400