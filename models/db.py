#!/usr/bin/python3
"""
Create sqlalchemy and engine 
"""

from sqlalchemy import create_engine

# Replace these variables with your actual values
db_user = 'hbnb_dev'
db_password = 'hbnb_dev_pwd'
db_host = 'localhost'
db_name = 'hbnb_dev_db'

# Create the engine
db_url = f"mysql+mysqldb://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(db_url, pool_pre_ping=True)

