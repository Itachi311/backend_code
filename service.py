import psycopg2
from config import config
import os
import logging

logging.basicConfig(filename='log/app.log', filemode='a',format='%(asctime)s- %(message)s',datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


def connect(data):
    """ Connect to the PostgreSQL database server """
    offset=int(data["offset"]) if "offset" in data.keys() else 0
    limit=int(data["limit"]) if "limit" in data.keys() else 1
    conn = None
    try:
        # read connection parameters
        params = config()
        
 
        # connect to the PostgreSQL server
        logger.info("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        # create a cursor
        cur = conn.cursor()

        logger.info(data)
        
        if "ifsc" in data.keys() and offset == 0 and limit == 1:
            #fetch a bank details, given branch IFSC code
            cur.execute('SELECT * FROM branches WHERE ifsc=%s LIMIT %s OFFSET %s',(data["ifsc"],limit,offset,))
            # display the required search one
            db_search = cur.fetchone()
            
            return db_search

        elif "bank_name" in data.keys() and "city" in data.keys():
            #fetch all details of branches, given bank name and a city
            cur.execute('SELECT * FROM bank_branches WHERE bank_name=%s  and city=%s LIMIT %s OFFSET %s',(data["bank_name"],data["city"],limit,offset,))
            # display the required search
            db_search = cur.fetchall()
            
            return  db_search
        else:
            logger.info("Invalid limit or offset or search parameters......")
            return "Invalid limit or offset or search parameters"
        
 
       
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        return (error)
    finally:
        if conn is not None:
            conn.close()
            logger.info('Database connection closed.....')
        
 
 
if __name__ == '__main__':
    connect()