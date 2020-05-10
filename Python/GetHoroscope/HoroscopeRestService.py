from flask import  Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)


class Horoscope(Resource):
    base = "http://sandipbgt.com/theastrologer/api/horoscope/" 

    def get(self, day, sign):
        r=callHoroscopeAPI(sign, day)
        if r.status_code == 200: 
            data=r.json() 
            return data["horoscope"], 200
        elif r.status_code == 404:
            return "Not valid sign", 400
        else:
            return "Service Not Available", 404

api.add_resource(Horoscope, '/<day>/<sign>') 




def callHoroscopeAPI(sign, day):
        URL = Horoscope.base + sign + "/" + day
        r = requests.get(url=URL) 
        return r


if __name__ == '__main__':
    app.run(port='5002') 