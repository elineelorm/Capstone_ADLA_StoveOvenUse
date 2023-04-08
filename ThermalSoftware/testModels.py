import unittest
from Project.Models.testdata import TestData
from Project.Models.testdataWithId import TestDataWithId
from Project.thermalImageProcessing2023 import processVideo
from Project.checkDuration import getFrameRate

"""
    testModels.py
    This file includes all the unit testing for the TestData model and TestDataWithId model.
    
    Author: Hiu Sum Jaime Yue

"""

# Can not directly test the fuction that used in database2023.py as it is linked to database
# Here is an edited version of add_video_from_filename that return an array of object that we want 
def add_video_from_filename_v2(filename):
    ''' 
    Author: Group from 2021/2022 (Jonathan Mack)
    Edited by Hiu Sum Jaime Yue

    Analyzes a video given its filename and stores its analytical data
    (FrameData records) into the database.

    The provided filename must contain the 'Test Data' folder as part of its path.

    Args:
        filename (str): The filename of the video to analyze and store

    Returns:
        None
    '''
    rate = getFrameRate(filename)
    

    # Replace '\\' with '/' to handle incoming filenames
    filename = filename.replace('\\', '/')

    # Trim leading path up until the Test Data folder
    filename = filename[filename.find('Test Data'):]

    # Get the type of the video (e.g., Frying)
    type = filename.split('/')[1]

    # Get the subtype of the video (e.g., Chicken)
    subtype = filename[filename.find('[')+1:filename.find(']')]

    # Set stove ID to 1 since we only have one stove
    stoveId = 1

    print("Frame rate in database: " + str(rate))
    # Get frame data from video(new change in 2023)=> sampleRate from 10 to 40 to (Dynamic)60 to 40 to attempt at equally spaced 20 frames
    frameData = processVideo(filename, rate)

    setData = []

    for (timeElapsed, avgPanTemp, highPanTemp, lowPanTemp, avgFoodTemp, highFoodTemp, lowFoodTemp) in frameData:
        # frameByFrameClassification = frameByFrameClassifications[timeElapsed]
        setData.append(timeElapsed)
        setData.append(avgPanTemp)
        setData.append(highPanTemp)
        setData.append(lowPanTemp)
        setData.append(avgFoodTemp)
        setData.append(highFoodTemp)
        setData.append(lowFoodTemp)

    #For testdata table, set state, type and safety to 0 and change it when we generate the csv
    testdataArray = [0,0,0] + setData

    #For testdataWithId table, set stoveId to 1 and change it when we generate the csv
    testdataWithIdArray = [1,0,0,0] + setData

    result = []
    result.append(testdataArray)
    result.append(testdataWithIdArray)

    return result

class TestModels(unittest.TestCase):
    """
    This is a class to test all new models.
    """
    # setUpClass method will only run once for all test functions
    @classmethod
    def setUpClass(cls):
        cls.result = add_video_from_filename_v2("C:/Users/jaime/Desktop/SYSC4907A/Code/Capstone_ADLA_StoveOvenUse/ThermalSoftware/Test Data/2023.03.28-15.34.35 [Fry egg].mp4")
        cls.TestDataArr = cls.result[0]
        cls.TestDataWithIdArr = cls.result[1]
    def test_arr_for_TestDataObj_len(self):
        """
        Test that check the number of elements in test arr before put into testDataObj
        """
        TestDataArrLen = len(self.TestDataArr)
        self.assertEqual(TestDataArrLen, 143)
    def test_arr_for_TestDataWithIdObj_len(self):
        """
        Test that check the number of elements in test arr before put into testDataWithIdObj
        """
        TestDataWithIdArrLen = len(self.TestDataWithIdArr)
        self.assertEqual(TestDataWithIdArrLen, 144)
    def test_TestDataObj_numOfVar(self):
        """
        Test that check the number of variables in TestDataObj
        """
        TestDataObj = TestData(*self.TestDataArr)

        resultLen = len(vars(TestDataObj))
        self.assertEqual(resultLen, 143)

    def test_TestDataWithIdObj_numOfVar(self):
        """
        Test that check the number of variables in TestDataWithIdObj
        """
        TestDataWithIdObj = TestDataWithId(*self.TestDataWithIdArr)
        resultLen = len(vars(TestDataWithIdObj))
        self.assertEqual(resultLen, 144) # Should be 145 but becuase of auto increment id => check 145 - 1 = 144

if __name__ == '__main__':
    unittest.main()