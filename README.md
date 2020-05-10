# Horoscope

A simple full stack application using Python, MongoDB, and Angular that asks the user to input their sun sign and either today, yesterday, or tomorrow
and returns their horoscope for the chosen day. T
The python component is a REST service which interfaces with the http://sandipbgt.com/theastrologer-api/api.html REST APIs. 


### Prerequisites
Python  
PIP  
flask  
flask-restful  
requests

### Deployment
Using Terminal: FLASK_APP=HoroscopeRestService.py flask run  
Can run on  python based IDE as well.

### REST Service Endpoints
GET /today/{sign}  
GET /tomorrow/{sign}  
GET /yesterday{sign}  

## Authors
Julian Dsilva
