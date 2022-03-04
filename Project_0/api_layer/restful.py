""" This module contains code for my api"""

"""
I am going to be making a RESTful web service. REST stands for Representational State Transfer, and is a popular
way of structuring web application. RESTful webservice inputs (think HTTP Requests) and outputs (think HTTP Response)
are in a machine friendly format (think JSON).

There are 6 different constraints to restful web services that help both guide your development process and that
help you maintain a true RESTful web service.

1. Client-Server architecture
    RESTful web services are not complete applications: they do not handle ANY client logic. Your RESTful web service
    should not handle the creating of the request to your service, but it can handle the response for the request
    that is made.
2. Stateless
    RESTful web services do not keep track of clients: any tracking is handled client-side.
    
3. Cacheable
    Information may be cached client-side to speed up operations.
    
4. Uniform Interface
    Resources handled by a restful web service should be easily identified by the Uniform Resoucre Identifier
    (URI) that is provided.
    Example uniform URI: GET /customer/1/account/5 should get the info from account 5 belonging to customer
    identified by number 1
    
5. Layered System
    RESTful web services should be able to call other RESTful web services
    
6. (optional) Code on Demand
    RESTful web servies may return executable code. This is not a common practice.
"""