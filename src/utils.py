import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import pymysql
# import mysql.connector

load_dotenv(find_dotenv())

host=os.environ.get("host")
user=os.environ.get("user")
password=os.environ.get("password")
db=os.environ.get('db')



def read_sql_data():
    
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
            # port = 3306
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df



    except Exception as e:
        raise CustomException(e,sys)

if __name__=="__main__":
    obj = read_sql_data()