


class BankAccount3:

    def __init__(self, cust_id_number: int, ba_id_number: int, balance: float):
        self.balance = balance
        self.cust_id_number = cust_id_number
        self.ba_id_number = ba_id_number

    def convert_to_dictionary2(self):
        return {
            "custIdNumber": self.cust_id_number,
            "baIdNumber": self.ba_id_number,
            "balance": self.balance
            }



