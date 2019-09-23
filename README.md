# Backend_code for python using flask assingment

<img src="https://www.fylehq.com/assets/images/logos/fylelogo.svg"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

## Objective:
1.use PostgreSQL as a backend database (you can get the data from [indian_banks](https://github.com/snarayanank2/indian_banks))
2.GET API to fetch a bank details, given branch IFSC code
3.GET API to fetch all details of branches, given bank name and a city 
4.each API should support limit & offset parameters
5.APIs should be authenticated using a JWT key, with validity = 5 days

## Prerequisite:
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
psycopg2==2.8.3
PyJWT==1.7.1
Werkzeug==0.16.0

### database.ini 
Contains informations for connecting postgresSQL i.e. host,database,user,password

### config.py 
To configure postgreSQL

### jwt_token.py
It contains two classes:
1.GenerateApiToken which generate a jwt token with a expires in 5 day.
2.ValidateApiToken which decode and verify the jwt token and send a response .

### service.py
fetch bank details from postgres, given branch IFSC code 
fetch all details of branches from postgreSQL, given bank name and a city

### app.py
API to fetch a bank details, given branch IFSC code
API to fetch all details of branches, given bank name and a city 




