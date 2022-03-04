"""This module is for when the code goes live. Contains the API for my application"""
from flask import Flask, request, jsonify

from custom_exceptions.bad_customer_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.zero_funds_exception import ZeroFunds
from data_access_layer.customer_data_access_object.customer_dao_implementation import CustomerDaoImplementation
from entities_customers_bank_account_info.customer_class_information import Customer_name
from tests.test_customer_service import customer_service

app: Flask = Flask(__name__) #Passing name as an argument lets the object know it should look for its information

my_list = ["I love my dog", "I ate pizza for lunch", "I am very sleepy"]



@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world"


@app.route("/personal/<name>", methods=["GET"])
def personal_greeting(name: str): #ANYTHING that comes as a path parameter will be passed into your function as strings
    return f"Hello {name}!"


@app.route("/add/<num_one>/<num_two>", methods=["GET"])
def addition_function(num_one, num_two):
    result = int(num_one) + int(num_two)
    return str(result)
    #return int(num_one) + int(num_two) won't work


@app.route("/list/<index>", methods=["GET"])
def get_phrase_from_list(index: str):
    global my_list
    return my_list[int(index)]


@app.route("/list", methods=["GET"])
def get_all_phrases_from_list():
    global my_list
    my_json_list = jsonify(my_list)
    return my_json_list, 202

@app.route("/json", methods=["GET"])
def return_a_json():
    customer_id = 1
    first_name = "Ted"
    last_name = "Teddington"
    """Because JSONs follow JavaScript naming conventions, we should make the dictionary keys follow them too"""
    customer_as_dictionary = {
        "customerId": customer_id,
        "firstName": first_name,
        "lastName": last_name
    }

    customer_as_json = jsonify(customer_as_dictionary)
    return customer_as_json, 200

@app.route("/query", methods=["GET"])
def get_filtered_phrases():
    min_index = request.args["min"]
    max_index = request.args["max"]
    global my_list
    return_list = []
    for index in range(0,len(my_list)-1, 1):
        if index >= int(min_index) and index <= int(max_index):
            return_list.append(my_list[index])
    return_list_as_json = jsonify(return_list)
    return return_list_as_json, 200



#@app.route("/list", methods=["POST"])
#def add_phrase_to_list():
    #request_content = request.get_json() #this method turns our JSON into a python dictionary
    #global my_list
    #my_list.append(request_content["key"])
    #return "Phrase added successfully"




app.run()


"""HTTP is the Hyper text transfer protocol. One of the most common ways of transferring information across the web.
What this system of info transfer does is it takes data in a machine friendly data format and transfers it across 
the web. There are 2 main parts to HTTP: the request, and the response. Part of the popularity of HTTP is the
guaranteed response to your requests.
"""

###HTTP Request
"""
All HTTP requests have 5 parts to them:
1. HTTP Version
2. URL
    - the url is an important part of the HTTP Request, and each part of the URL plays a role.
    - http://www.localhost:5000/greeting?hostile=false
        - http: this part of the url indicates what kind of request i am making.
        - www.localhost: this here is the ***domain*** name: this is where content we want to interact with is located.
        - 5000: this is the ***port*** where the request is going to be sent: the computer thats hosting the web server 
        that receives the http request is going to be "listening" on that particular port for our requests.
        - /greeting: this is the **path** of my request. these can contain one or more words, separated by / and
        they can also contain what is called **path parameters**
        - ?hostile=false: these are the ***query*** parameters, which are normally used when you want to filter data
3. Verb
    - the Verb of your HTTP request provides context about what you are trying to accomplish with your HTTP request.
    There are few common Verbs that you will be working with
        - GET
        - PUT
        - POST
        - PATCH
        - DELETE
4. Headers
    - headers provide meta data about your HTTP request, and they can sometimes be useful when parsing info from
    your request
5. Body
    - the body of a request holds all the info for the request. This can be user input data, it can be dates, whatever
    info you need to pass from the user to your web application is stored in the body of your request.
    - GET requests may not have a body
"""

### HTTP Response
"""
1. HTTP Version
2. Headers
3. Body
    - This is where any pertinent info for the user is stored
4. Status Code
    - this is a quick indication of how the request was handled
    -100 this is usually just meta data/general info
    -200 this is the success level
    -300 this is the reroute level
    -400 this is the failure level
        - this code is used when the requester makes a bad request. This could mean they made an HTTP request to the
        wrong location, etc.
    -500 this is the failure level for the web server
        - this is not a failure of the requester, but a failure of the developer. 

### JSON
Javascript Object Notation is the most common FORMAT that data is transferred across the web. Essentially,
JSONSs are formatted strings that work in key:value pairs. JSONs support three different data types:
    -Strings
    -Numbers
    -Booleans
The reason JSONs are so popular is because they are easy to just about every programming language to parse.

ex JSON
{
    "name":"Andraey Pompey"
    "profession":"Student"
    "Fun Fact":"I was in a band"
}

"""

app: Flask = Flask(__name__)
customer_dao = CustomerDaoImplementation


"""
If i want to do something with customer data, i need to use the 'customers' route for all request. I can use different
verbs to determine WHAT i am doing with the customer data, and that is how Flask will know what particular service
method needs to be called
"""


@app.route("/customers", method=["POST"])
def create_customer():
    try:
        customer_data: dict = request.get_json() #locating in the post request body, turning my customer dao into a dictionary
        customer_name = Customer_name(customer_data["firstName"], customer_data["lastName"], customer_data["custIdNumber"])
        result = customer_service.service_create_customer(customer_name)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadCustomerInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except ZeroFunds as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/customers/<id>", methods=["GET"])
def get_customer_by_id(id:str):
    try:
        result: Customer_name = customer_service.service_get_cust_by_id(int(id))
        # found an issue that could break code. need to do TDD to add code to my service layer to handle int(id)
        result_dictionary = result.convert_to_dictionary()
        return jsonify(result_dictionary), 200
    except BadCustomerInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except ZeroFunds as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400

app.run()