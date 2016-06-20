Simple Flask contact api
-------------------------
Requirement

Need contact api with 
 - create, update, delete, edit
 - get a particular contact
 - search for a contact by email

# Mock the Database no real database required

Sample Record

{
	"contact": [{
		"name": "Some Name",
		"email": "someemail@domain.com",
		"address": {
			"type": "work",
			"line": "blah..",
			"city": "some city",
			"zip": "90510"
		},
		"phone": {
			"type": "mobile",
			"number": "5555555555",
			"country": "+1212"
		}
	}]
}
 
# Api exposed

1. Get all contacts

   curl -v "http://127.0.0.1:9002/api/v1/contact"
   
  open in browser
  
   https://flask-contact-api.herokuapp.com/api/v1/contact

2. Get specific contact

   curl -v "http://127.0.0.1:9002/api/v1/contact/someemail@domain.com"
   
  open in browser
  
   https://flask-contact-api.herokuapp.com/api/v1/contact/aurelia98@connelly-lehner.com

3. Update specific contact
   curl -X PUT -H "Content-Type: application/json" -d '{
       "address": {
         "city": "East Wynonaport", 
         "line": "250 Fisher Loop Apt. 784\nPort Patrick, AZ 00685-9561", 
         "type": "Geochemist", 
         "zip": "07638"
       }, 
       "email": "guna@gmail.com", 
       "name": "Hazen Dickinson", 
       "phone": {
         "country": "AE", 
         "number": "(422)828-8943x810", 
         "type": "MintCream"
       }
    }
   ' "http://localhost:9002/api/v1/contact/phammes@bernhard.org"

4. Create new contact
   curl -X POST -H "Content-Type: application/json" -d '{
    "address": {
      "city": "East Wynonaport", 
      "line": "250 Fisher Loop Apt. 784\nPort Patrick, AZ 00685-9561", 
      "type": "Geochemist", 
      "zip": "07638"
    }, 
    "email": "guna@gmail.com", 
    "name": "Hazen Dickinson", 
    "phone": {
      "country": "AE", 
      "number": "(422)828-8943x810", 
      "type": "MintCream"
    }
 }
' "http://localhost:9002/api/v1/contact"


5. Delete existing contact

   curl -X DELETE -v "http://localhost:9002/api/v1/contact/willaimlesch@gmail.com" 

Heroku app -- url

https://flask-contact-api.herokuapp.com/
