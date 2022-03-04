"""This module contains customer dao unit tests"""
from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_data_access_object.customer_dao_implementation import CustomerDaoImplementation
from entities_customers_bank_account_info.customer_class_information import Customer_name
"""
create customer tests
"""

customer_dao = CustomerDaoImplementation()

def test_create_customer_success():
    test_customer = Customer_name("Andraey", "Pompey", 0)
    result = customer_dao.create_customer(test_customer)
    assert result.cust_id_number != 0

def test_catch_non_unique_id():
    test_customer = Customer_name("Jimmy", "Williams", 1)
    result = customer_dao.create_customer(test_customer)
    assert result.cust_id_number != 1

"""Get Customer Info Section"""

def test_get_customer_info_by_id_success():
    result = customer_dao.get_cust_information_by_id(1)
    assert result.cust_id_number == 1

def test_get_customer_using_nonexistent_id():
    try:
        customer_dao.get_cust_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"

    """update team test"""

def test_update_cust_by_id_success():
    new_cust_name = Customer_name("Charlie", "Williams", 2)
    result = customer_dao.update_cust_by_id(new_cust_name)
    assert result.first_name == "Charlie"

def test_update2_cust_by_id_success():
    new_cust_name = Customer_name("Jimmy", "Walters", 2)
    result = customer_dao.update_cust_by_id(new_cust_name)
    assert result.last_name == "Walters"

def test_update_cust_using_nonexistent_id():
    try:
        new_cust_name = Customer_name("Charlie", "Williams", 0)
        customer_dao.update_cust_by_id(new_cust_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"

"""delete customer tests"""

def test_delete_cust_by_id_success():
    result = customer_dao.delete_cust_by_id(1)
    assert result

def test_delete_cust_with_nonexistent_id():
    try:
        customer_dao.delete_cust_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"