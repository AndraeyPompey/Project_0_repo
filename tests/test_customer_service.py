from custom_exceptions.bad_customer_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_data_access_object.customer_dao_implementation import CustomerDaoImplementation
from entities_customers_bank_account_info.customer_class_information import Customer_name
from service_layer.customer_services.customer_service_implementation import CustomerServiceImp

customer_dao = CustomerDaoImplementation()
customer_service = CustomerServiceImp(customer_dao)
non_string_first_name = Customer_name(10, "Johnson", 3)
non_string_last_name = Customer_name("Jimbo", 98, 3)
first_name_too_long = Customer_name("JimboTronomus the ThirtyThird II", "Johnson", 3)
last_name_too_long = Customer_name("Jimbo", "JohnsonTronomus the ThirtyThird II", 3)


#Create tests
def test_check_no_duplicate_id_numbers():
    test_customer = Customer_name("Jimmy", "Williams", 1)
    result = customer_dao.create_customer(test_customer)
    assert result.cust_id_number != 1

def test_check_non_string_first_name_create_customer():
    try:
        customer_service.service_create_customer(non_string_first_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid first name"

def test_check_non_string_last_name_create_customer():
    try:
        customer_service.service_create_customer(non_string_last_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid last name"

def test_check_first_name_length_too_long():
    try:
        customer_service.service_create_customer(first_name_too_long)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid first name"

def test_check_last_name_length_too_long():
    try:
        customer_service.service_create_customer(last_name_too_long)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid last name"


#Select customer tests

def test_cant_typecast_to_int():
    try:
        customer_service.service_get_cust_by_id("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "No Customer matches the id given: please try again"

def test_get_customer_successfully_typecast_string():
    result = customer_service.service_get_cust_by_id("1")
    assert result.cust_id_number == 1





#def test_check_nonnumeric_id(): #because of the new features, I need to change this test
    #try:
       # customer_service.service_get_cust_by_id("one")
       #assert False
    #except BadCustomerInfo as e:
        #assert str(e) == "No Customer matches the id given: please try again"

#Update tests
def test_catch_non_string_first_name_update():
    try:
        customer_service.service_update_cust_by_id(non_string_first_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid first name"

def test_catch_non_string_last_name_update():
    try:
        customer_service.service_update_cust_by_id(non_string_last_name)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please pass in a valid last name"


#delete tests

def test_catch_non_numeric_id_delete_customer():
    try:
        customer_service.delete_cust_by_id("one")
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"


def test_delete_cust_with_nonexistent_id():
    try:
        customer_dao.delete_cust_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No Customer matches the id given: please try again"