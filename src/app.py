#! /usr/bin/python
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from fake_input_generator import FakeContact
import os

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('contact', type=str, help='contact to create user')

# Memory to save contact_data
contact_data = []

# Contact Model or base Calls to create Contact data.


class Contact(object):

    def __init__(self, email, name=None, addresscity=None, addressline=None,
                 addresstype=None, addresszip=None, phonecountry=None, phonenumber=None, phonetype=None):
        self.email = email
        self.name = name
        self.addresscity = addresscity
        self.addressline = addressline
        self.addresstype = addresstype
        self.addresszip = addresszip
        self.phonecountry = phonecountry
        self.phonenumber = phonenumber
        self.phonetype = phonetype

    def json(self):
        return {"email": self.email,
                "name": self.name,
                "address": {
                    "city": self.addresscity,
                    "line": self.addressline,
                    "type": self.addresstype,
                    "zip": self.addresszip
                },
                "phone": {
                    "country": self.phonecountry,
                    "number": self.phonenumber,
                    "type": self.phonetype
                },
                }

    def to_str(self):
        return json.dumps(self.json())


def check_if_contact_exist(email_id):
    result = [item for item in contact_data if item['email'] == email_id]
    if result:
        return result
    else:
        abort(404, message="User Contact {} doesn't exist".format(email_id))


# Basic idea of API workes on Resource.
# So creating Contact resource.
class ContactResource(Resource):

    def get(self, email_id):
        result = check_if_contact_exist(email_id)
        return jsonify(result)

    def delete(self, email_id):
        result = check_if_contact_exist(email_id)
        contact_data.remove(result[0])
        return '', 204

    def put(self, email_id):
        global contact_data
        json_data = request.get_json(force=True)
        update_contact = check_if_contact_exist(email_id)
        for k, v in json_data.items():
            if k in update_contact[0]:
                update_contact[0][k] = v
        return update_contact, 201


class ContactResourceList(Resource):

    def get(self):
        return jsonify(contact_data)

    def post(self):
        global contact_data
        json_data = request.get_json(force=True)
        email_id = json_data['email']
        result = [item for item in contact_data if item['email'] == email_id]
        if result:
            abort(404, message="User Contact {} already exist".format(email_id))
        new_contact = Contact(email_id)
        for k, v in json_data.items():
           if type(v) == dict:
               for k1, v1 in v.items():
                   setattr(new_contact, k+k1, v1)
           else:
               setattr(new_contact, k, v)
        contact_data = contact_data + [new_contact.json()]
        return new_contact.json(), 201


api.add_resource(ContactResourceList, '/api/v1/contact')
api.add_resource(ContactResource, '/api/v1/contact/<string:email_id>')


# this call to generate random data for contact
@app.route('/api/v1/contact/generate/<int:count>', methods=['GET'])
def generate_contacts(count):
    global contact_data
    fake_data = FakeContact()
    result = fake_data.generate_data(count)
    contact_data = contact_data + result
    return jsonify({'contacts': contact_data})


@app.route('/')
def index():
    return "Hello, World! This is Sample Contact API"

if __name__ == '__main__':
    fake_data = FakeContact()
    contact_data = fake_data.generate_data(1)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

