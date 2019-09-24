# Backend_code for python using flask assingment

<img src="https://www.fylehq.com/assets/images/logos/fylelogo.svg"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

## Objective:
1. use PostgreSQL as a backend database (you can get the data from [indian_banks](https://github.com/snarayanank2/indian_banks))
2. GET API to fetch a bank details, given branch IFSC code
3. GET API to fetch all details of branches, given bank name and a city 
4. each API should support limit & offset parameters
5. APIs should be authenticated using a JWT key, with validity = 5 days

## Prerequisite:
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
psycopg2==2.8.3
PyJWT==1.7.1
Werkzeug==0.16.0
``` pip install -r requirements.txt```
### database.ini 
Contains informations for connecting postgresSQL i.e. host,database,user,password

### config.py 
To configure postgreSQL

### jwt_token.py
It contains two classes:
1. GenerateApiToken which generate a jwt token with a expires in 5 day.
2. ValidateApiToken which decode and verify the jwt token and send a response .

### service.py
1. fetch bank details from postgres, given branch IFSC code 
2. fetch all details of branches from postgreSQL, given bank name and a city

### app.py
1. API to fetch a bank details, given branch IFSC code
2. API to fetch all details of branches, given bank name and a city 

# usage
1. Install [postresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
``` pip install -r requirements.txt```
``` python app.py```

# curl request:

1. GET API to fetch a bank details, given branch IFSC code:
``` curl -X GET \
  https://limitless-crag-08495.herokuapp.com/bank_details \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 54d466e4-6699-4fbf-aed7-1cd342e0fed8' \
  -H 'cache-control: no-cache' \
  -d '
{
   "Access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik5hcnV0byIsInNlY3JldCI6IkRlZmF1bHQxIiwiZXhwIjoxNTY5NTcyNjAwfQ.FrFU6nJ-QkppIY1bZMHUIhyoElwgLHYxDq8H0OEJeco",
   "success":"True",
  "ifsc":"ABHY0065005","offset":0,"limit":1
}'
``` 
2. GET API to fetch all details of branches, given bank name and a city 
```curl -X GET \
  https://limitless-crag-08495.herokuapp.com/branches_details \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 97933c9c-6b96-446e-8bfa-5cafb9ae9d1d' \
  -H 'cache-control: no-cache' \
  -d '{
   "Access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik5hcnV0byIsInNlY3JldCI6IkRlZmF1bHQxIiwiZXhwIjoxNTY5NTcyNjAwfQ.FrFU6nJ-QkppIY1bZMHUIhyoElwgLHYxDq8H0OEJeco",
   "success":"True",
   "bank_name":"ALLAHABAD BANK",
   "city":"KOLKATA",
   "offset":"10",
   "limit":"10"
}' 
```

