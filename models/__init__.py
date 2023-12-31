#!/usr/bin/python3
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv

# Define storage outside the conditional blocks to ensure it's always available
storage = None

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()  # Ensure the storage is reloaded after initialization
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()  # Ensure the storage is reloaded after initialization

# Now that the storage is initialized, importing State should work
from models.state import State

