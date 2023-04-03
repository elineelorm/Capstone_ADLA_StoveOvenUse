"""
    classification.py
    This is the classification model of the system
    
    Author: Eline-Elorm Nuviadenu
"""

from database import Database
import pickle
import pandas as pd
import time


class Classification:
    def __init__(self):
        self.name = "Classification"
        self._db = Database()

    def load_model(self, filename):
        """
        Loads the machine learning model 

        Parmeters
        ---------
        filename : str 
            The path to the machine learning model 

        """
        return pickle.load(open(filename, 'rb'))

    def process_data(self, dataset):
        """
        Processes the dataset to enable smooth predictions

        Parameters
        ----------
        dataset : str
            The path to the csv file with data to be predicted 

        Returns
        -------
        tuple of lists
            - the data without unnecessary columns
            - the original dataset 
        """
        data = pd.read_csv(dataset, skiprows=1)
        dataset_list = list(data.columns.values)
        return(data[dataset_list[5:]], dataset_list)

    def label_predictions(self, data, dataset, model1, model2, model3):
        """
        Makes predictions and write to appropriate database 

        Parameters
        ----------
        data : Dataframe
            The data to be predicted 

        dataset : list
            A list of all the input data

        model1 : Machine Learning Model (ON/OFF)
            A model to predict if the stove was off(0) or on(1)

        model2 : Machine Learning Model (SAFE/UNSAFE)
            A model to predict if the stove was safe(0) or unsafe(1)

        model3 : Machine Learning Model (FRYING/BOILING)
            A model to predict if the cooking method was boiling(0) or frying(1)


        """
        for ix in data.index:
            stove_id = dataset[0][1]
            time.sleep(5)
            if (model1.predict([data.values[ix]]) == 1): #on
                print("Stove is on!")
                if(model2.predict([data.values[ix]]) == 0): #safe
                    print("Stove is safe!")
                    if (model3.predict([data.values[ix]]) == 0): #boil
                        print("An egg was boiled")
                        self._db.write_to_db(stove_id, "Safe", "On", "Boiling")
                    else:
                        print("An egg was fried")
                        self._db.write_to_db(stove_id, "Safe", "On", "Frying")
                else:  #unsafe
                    print("Stove is unsafe!")
                    self._db.write_to_db(stove_id, "Unsafe", "On", "None")
            else: #off
                print("Stove is off!")
                self._db.write_to_db(stove_id, "Safe", "Off", "None")


    
    
  
    
    
