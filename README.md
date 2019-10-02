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

``` pip install -r requirements.txt```

### config.py 
configuration for postgresql

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
3. Sending sensitive information like database credentials and JWT secret key from environment variables
4. Search and pagination parameters are sent as query parameters
# usage
1. Install [postresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
2. ``` pip install -r requirements.txt```
3. ``` python app.py```

# curl request:

1. GET API to fetch a bank details, given branch IFSC code:
```
 curl -X GET \
  'https://limitless-crag-08495.herokuapp.com/bank_details?ifsc=ALLA0210032&offset=0&limit=1' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: c1b8f4be-8bec-4ed2-b5eb-cbe54e06ada3' \
  -H 'cache-control: no-cache' \
  -d '{
   "Access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik5BUlVUTyIsInNlY3JldCI6IjEyMzRAIiwiZXhwIjoxNTcwNDc2MzAzfQ.32jXnBK6d8M_q9WU8ZbBqfKOfMSgWMCiiHuuW3G1W_Y",
   "success":"True"
 
}'
``` 
2. GET API to fetch all details of branches, given bank name and a city :
``` 
curl -X GET \
  'https://limitless-crag-08495.herokuapp.com/branches_details?bank_name=ALLAHABAD%20BANK&city=KOLKATA&offset=0&limit=10' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 1cda54f8-c483-46a3-89bf-adffa90b5063' \
  -H 'cache-control: no-cache' \
  -d '{
   "Access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik5BUlVUTyIsInNlY3JldCI6IjEyMzRAIiwiZXhwIjoxNTcwNDc2MzAzfQ.32jXnBK6d8M_q9WU8ZbBqfKOfMSgWMCiiHuuW3G1W_Y",
   "success":"True"
 
}'
```

