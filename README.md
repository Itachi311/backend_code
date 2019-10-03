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

#### NOTES TO BE FOLLOWED

1. Sensitive information like database credentials and JWT secret key should be acquire from environment variables.
2. Search and pagination parameters should be sent as query parameters.
3. JWT tokens should be acquire from the headers of the request.

# usage

1. Install [postresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
2. ``` pip install -r requirements.txt```
3. ``` python app.py```

# curl request:

1. GET API to fetch a bank details, given branch IFSC code:
```
curl -X GET \
  'https://limitless-crag-08495.herokuapp.com/bank_details?ifsc=ALLA0210032&offset=0&limit=1' \
  -H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik5BUlVUTyIsInNlY3JldCI6IjEyMzRAIiwiZXhwIjoxNTcwNDc2MzAzfQ.32jXnBK6d8M_q9WU8ZbBqfKOfMSgWMCiiHuuW3G1W_Y' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 723fa8c7-cbcb-4f8b-9517-d7b1ed0d47ee' \
  -H 'cache-control: no-cache'
``` 
2. GET API to fetch all details of branches, given bank name and a city :
``` 
curl -X GET \
  'https://limitless-crag-08495.herokuapp.com/branches_details?bank_name=ALLAHABAD%20BANK&city=KOLKATA&offset=2&limit=2' \
  -H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik5BUlVUTyIsInNlY3JldCI6IjEyMzRAIiwiZXhwIjoxNTcwNDc2MzAzfQ.32jXnBK6d8M_q9WU8ZbBqfKOfMSgWMCiiHuuW3G1W_Y' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 9d4ed23f-b789-4bfb-86b0-1cac139517d1' \
  -H 'cache-control: no-cache'
```

