
import os
 
def config():
    db={}
    # get database host name from environment variable
    db["host"]=os.environ.get('HOST')
    # get database name from environment variable
    db["database"]=os.environ.get('DATABASE')
    # get database user name from environment variable
    db["user"]=os.environ.get('DB_USER')
    # get database password  from environment variable
    db["password"]=os.environ.get('DB_PASSWORD')
    print(db)

    return db