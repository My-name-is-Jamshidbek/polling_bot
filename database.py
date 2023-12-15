"""
data base
"""

import time
import datetime

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# from cryptography.fernet import Fernet

from config import *

import sqlite3
from sqlite3 import Connection

if not os.path.exists("users.db"):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    # Create the vooters table
    c.execute("CREATE TABLE vooters (id INTEGER PRIMARY KEY, name TEXT, votes INTEGER)")

    # Create the users table with a foreign key reference to vooters
    c.execute("""
        CREATE TABLE users (
            telegram_id INTEGER PRIMARY KEY,
            vooter_id INTEGER,
            FOREIGN KEY (vooter_id) REFERENCES vooters(id)
        )
    """)
    c.execute(
        "CREATE TABLE channels (id INTEGER PRIMARY KEY, name TEXT, link INTEGER)")

    conn.commit()
    conn.close()

