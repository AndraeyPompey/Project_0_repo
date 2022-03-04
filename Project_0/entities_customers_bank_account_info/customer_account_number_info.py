#from entities_customers_bank_account_info.customer_class_information import cust_id_number



class account:
    def __init__(self, acc_number: int, cust_id_number: int, checking_acc_number: int, saving_acc_number: int):
        self.acc_number = acc_number
        self.cust_id_number = cust_id_number
        self.checking_acc_number = checking_acc_number
        self.saving_acc_number = saving_acc_number






class BankAccount:
    def __init__(self, ba_id_number: int,cust_id_number: int, money_amount: int):
        self.ba_id_number = ba_id_number
        self.cust_id_number = cust_id_number
        self.money_amount = money_amount


"""
accounts have unique numbers
accounts have two types: checkings and savings
accounts have a positive(or 0 balance) amount
"""