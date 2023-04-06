"""
    database.py
    This class represents the database module of the system.
    
    Author: Eline-Elorm Nuviadenu
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 


class Database:
    def __init__(self):
        self.name = "Classification Database Module"
        self._init_config()
        self._firebase = firebase_admin.initialize_app(self._cred, self._config)
        self._db_log = db.reference('/Log')     #   Database for Backlog 
        self._db = db.reference('/Users/1/StoveManagement')     #Database for Current State of Stove


    def _init_config(self):
        """
            Initializes the config attribute of the database.
            This needs to be modified if the database to be used is changed
        """
        self._cred = credentials.Certificate('secret_key.json')
        self._config = {
            "databaseURL": "https://the-og-27e6f-default-rtdb.firebaseio.com"
        }

    def write_to_db(self, stove_id, safety, state, type):
        """
            Writes data to database,.
            Creates one to be stored permanently in the backlog,
            and one to update the application

            Parameters
            ----------
            stove_id : int 
                The id of the stove currently in use 
            safety : str 
                The safety of the stove - safe/unsafe
            state : str
                The state of the stove - on/off
            type : str 
                The type of cooking method being used - frying/boiling
        """
        
        print("Adding to Log...")
        self._db_log.push({
            'Safety': safety,
            'State': state,
            'Type': type,
            'stoveId': int(stove_id)
        })
        print("Updating data to be shown on app...")
        self._db.set({
            'Safety': safety,
            'State': state,
            'Type': type,
            'stoveId': int(stove_id)
        })
    