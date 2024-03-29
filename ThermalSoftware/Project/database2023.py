import sqlite3
import os
from fnmatch import fnmatch
from sqlite3 import IntegrityError
from Models.video import Video
from Models.frame_data import FrameData
from Models.testdata import TestData
from Models.testdataWithId import TestDataWithId
from thermalImageProcessing2023 import processVideo
from checkDuration import getFrameRate

"""
    database2023.py
    This is a application to call and process thermal videos and save to database using the correct models.
    
    Author: Group from 2021/2022 (Jonathan Mack)
    Edited by Hiu Sum Jaime Yue

"""

DATABASE = 'Project/cooking_thermal_2023.db' #New database in 2023

def generate_database():
    ''' Create a database based on the Test Data folder.
    Delete the database if it already exists.
    For each thermal video in the Test Data folder:
        1. Create an analysis table.
        2. Add records (FrameData) to the analysis table for each sampled frame.
        3. Add a record (Video) to the videos master table.
    
    Args:
        None
    
    Returns:
        None
    '''
    # Delete database if it already exists
    if os.path.exists(DATABASE):
        print('Removing existing database {}'.format(DATABASE))
        os.remove(DATABASE)

    # Get all filenames of thermal videos in Test Data folder
    TEST_DATA_FOLDER = 'Test Data'
    PATTERN = '*.mp4'
    filenames = []

    for path, subdirs, files in os.walk(TEST_DATA_FOLDER):
        for name in files:
            if fnmatch(name, PATTERN):
                filenames.append(os.path.join(path, name))

    # Iterate through each video
    for filename in filenames:
        add_video_from_filename(filename)



def create_videos_table():
    ''' Create the master videos table.
    The master videos table stores high-level information about thermal videos.
    This inlcudes the style of cooking (e.g., frying), the food being cooked (e.g., chicken), the
    filepath of the thermal video, the corresponding analysis table, and the registered stove ID.
    
    Args:
        None
    
    Returns:
        None
    '''
    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        # Check if the videos table already exists
        c.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='videos'")
        if c.fetchone()[0] == 0:
            c.execute('''CREATE TABLE videos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            type TEXT,
                            subtype TEXT,
                            filename TEXT,
                            analysis_table_name TEXT,
                            classification TEXT,
                            stoveId INTEGER
                        )''')
                        # Might delete classification and stoveId
        c.close()
    conn.close()



def insert_video(video):
    ''' Insert a video into the master videos table.
    
    Args:
        video (Video): The video to insert
    
    Returns:
        None
    '''
    # Create videos table if it does not already exist
    create_videos_table()

    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        try:
            c.execute('INSERT INTO videos VALUES (null, ?, ?, ?, ?, ?, ?)', video.get_as_record())
            print('Successfully inserted video {}'.format(video.filename))
        except AttributeError:
            print('Video to be inserted is not of type Video: {}'.format(type(video)))
        except:
            print('An unexpected error occurred when inserting a record into the videos table')
        finally:
            c.close()
    conn.close()



def get_all_videos():
    ''' Get all the videos from the master videos table.
    
    Args:
        None
    
    Returns:
        list: All videos in the master videos table
    '''
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM videos')
    videos = c.fetchall()
    c.close()
    conn.close()
    return videos



def get_video_by_id(id):
    ''' Get a video by its ID from the master videos table.
    
    Args:
        id (int): The ID to search for
    
    Returns:
        Video: The video with the ID provided
    '''
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM videos WHERE id=?', (id,))
    video = c.fetchone()
    c.close()
    conn.close()
    return video



def get_videos_by_type(type):
    ''' Get all the videos from the master videos table with the
    type provided (e.g., frying).
    
    Args:
        type (str): The type to search for
    
    Returns:
        list: All videos in the master videos table with the type
    '''
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM videos WHERE type=?', (type,))
    videos = c.fetchall()
    c.close()
    conn.close()
    return videos



def get_videos_by_subtype(subtype):
    ''' Get all the videos from the master videos table with the
    subtype provided (e.g., chicken).
    
    Args:
        subtype (str): The subtype to search for
    
    Returns:
        list: All videos in the master videos table with the subtype
    '''
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM videos WHERE subtype=?', (subtype,))
    videos = c.fetchall()
    c.close()
    conn.close()
    return videos



def get_videos_by_stoveId(stoveId):
    ''' Get all the videos from the master videos table with the
    registered stove ID.
    
    Args:
        stoveId (str): The stove ID to search for
    
    Returns:
        list: All videos in the master videos table with the stove ID
    '''
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM videos WHERE stoveId=?', (stoveId,))
    videos = c.fetchall()
    c.close()
    conn.close()
    return videos


# 2023: Updated variable names in SQL command
def create_analysis_table(name):
    ''' Return the modified name of the analysis table created for a given name.
    Appends a unique, incrementing index to the end of the analysis table name.

    Example:
        chicken => Chicken_Analysis_Table_1
        Chicken => Chicken_Analysis_Table_2
        ground beef => Ground_Beef_Analysis_Table_1

    Arg:
        name (str): The original name of the analysis table
    
    Returns:
        string: The modified name of the analysis table
    '''
    # Replace spaces with underscores
    name = name.title().replace(' ', '_')

    # Index of the analysis table
    tableIndex = 1
    baseName = '{}_Analysis_Table'.format(name)

    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        while True:
            # Format the analysis table name to include an index
            name = '{}_{}'.format(baseName, tableIndex)
            # Check if the analysis table already exists
            c.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name=?", (name,))
            if c.fetchone()[0] == 0:
                break
            # Increment the analysis table index until the table name is unique
            tableIndex += 1
        # Must use string formatting since sqlite3 doesn't support variable table names(updated names)
        c.execute('''CREATE TABLE {} (
                        time_elapsed INTEGER PRIMARY KEY,
                        avg_pan_temp REAL,
                        highest_pan_temp REAL,
                        lowest_pan_temp REAL,
                        avg_food_temp REAL,
                        highest_food_temp REAL,
                        lowest_food_temp REAL
                    )'''.format(name))
        c.close()
    conn.close()
    print('{} created'.format(name))
    return name



def insert_one_frame_data(frameData, analysisTableName):
    ''' Insert a FrameData record into an analysis table.
    
    Args:
        frameData (FrameData): The FrameData to insert
        analysisTableName (str): The name of the analysis table to insert to
    
    Returns:
        None
    '''
    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        try:
            # Must use string formatting since sqlite3 doesn't support variable table names
            c.execute('INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?)'.format(analysisTableName),
                       frameData.get_as_record())
        except AttributeError:
            print('Frame data to be inserted is not of type FrameData: {}'.format(type(frameData)))
        except IntegrityError:
            print('A record with a Time Elapsed of {} already exists in analysis table {}'.format(
                frameData.timeElapsed, analysisTableName))
        finally:
            c.close()
    conn.close()



def insert_many_frame_data(frameDataList, analysisTableName):
    ''' Insert multiple FrameData records into an analysis table.
    
    Args:
        frameData (FrameData): The FrameData to insert
        analysisTableName (str): The name of the analysis table to insert to
    
    Returns:
        None
    '''
    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        try:
            # Must use string formatting since sqlite3 doesn't support variable table names
            c.executemany('INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?)'.format(analysisTableName),
                       [frameData.get_as_record() for frameData in frameDataList])
        except AttributeError:
            print('Frame data to be inserted is not a list of FrameData: {}'.format(type(frameDataList)))
        except IntegrityError:
            print('A record in the frame data set contains a time_elapsed that already '\
                  'exists in analysis table {}'.format(analysisTableName))
        finally:
            c.close()
    conn.close()



def get_all_frame_data(analysisTableName):
    ''' Get all FrameData records from an analysis table.
    
    Args:
        analysisTableName (str): The analysis table containing the FrameData
    
    Returns:
        list: All FrameData in an analysis table
    '''
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM {}'.format(analysisTableName))
    frameData = c.fetchall()
    c.close()
    conn.close()
    return frameData

# 2023: Method for getting thermal data in an array
def get_frame_data_array(analysisTableName):
    ''' Get all FrameData records from an analysis table.
    
    Args:
        analysisTableName (str): The analysis table containing the FrameData
    
    Returns:
        list: All FrameData in an analysis table
    '''
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM {}'.format(analysisTableName))
    frameData = c.fetchone()
    c.close()
    conn.close()
    return frameData

# 2023: Method that create a new table for saving frame data to be transferred to csv using testdata model
def create_testdata_table():
    ''' Create the master testdata table.
    The master testdata table stores high-level information about thermal videos.
    This inlcudes everything that goes into the csv for machine learning purpose.
    
    Args:
        None
    
    Returns:
        None
    '''
    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        # Check if the testdata table already exists
        c.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='testdata'")
        if c.fetchone()[0] == 0:
            c.execute('''CREATE TABLE testdata (
                            state INTEGER,
                            type INTEGER,
                            safety INTEGER,
                            time_elapsed_1 INTEGER,
                            avg_pan_temp_1 REAL,
                            highest_pan_temp_1 REAL,
                            lowest_pan_temp_1 REAL,
                            avg_food_temp_1 REAL,
                            highest_food_temp_1 REAL,
                            lowest_food_temp_1 REAL,
                            time_elapsed_2 INTEGER,
                            avg_pan_temp_2 REAL,
                            highest_pan_temp_2 REAL,
                            lowest_pan_temp_2 REAL,
                            avg_food_temp_2 REAL,
                            highest_food_temp_2 REAL,
                            lowest_food_temp_2 REAL,
                            time_elapsed_3 INTEGER,
                            avg_pan_temp_3 REAL,
                            highest_pan_temp_3 REAL,
                            lowest_pan_temp_3 REAL,
                            avg_food_temp_3 REAL,
                            highest_food_temp_3 REAL,
                            lowest_food_temp_3 REAL,
                            time_elapsed_4 INTEGER,
                            avg_pan_temp_4 REAL,
                            highest_pan_temp_4 REAL,
                            lowest_pan_temp_4 REAL,
                            avg_food_temp_4 REAL,
                            highest_food_temp_4 REAL,
                            lowest_food_temp_4 REAL,
                            time_elapsed_5 INTEGER,
                            avg_pan_temp_5 REAL,
                            highest_pan_temp_5 REAL,
                            lowest_pan_temp_5 REAL,
                            avg_food_temp_5 REAL,
                            highest_food_temp_5 REAL,
                            lowest_food_temp_5 REAL,
                            time_elapsed_6 INTEGER,
                            avg_pan_temp_6 REAL,
                            highest_pan_temp_6 REAL,
                            lowest_pan_temp_6 REAL,
                            avg_food_temp_6 REAL,
                            highest_food_temp_6 REAL,
                            lowest_food_temp_6 REAL,
                            time_elapsed_7 INTEGER,
                            avg_pan_temp_7 REAL,
                            highest_pan_temp_7 REAL,
                            lowest_pan_temp_7 REAL,
                            avg_food_temp_7 REAL,
                            highest_food_temp_7 REAL,
                            lowest_food_temp_7 REAL,
                            time_elapsed_8 INTEGER,
                            avg_pan_temp_8 REAL,
                            highest_pan_temp_8 REAL,
                            lowest_pan_temp_8 REAL,
                            avg_food_temp_8 REAL,
                            highest_food_temp_8 REAL,
                            lowest_food_temp_8 REAL,
                            time_elapsed_9 INTEGER,
                            avg_pan_temp_9 REAL,
                            highest_pan_temp_9 REAL,
                            lowest_pan_temp_9 REAL,
                            avg_food_temp_9 REAL,
                            highest_food_temp_9 REAL,
                            lowest_food_temp_9 REAL,
                            time_elapsed_10 INTEGER,
                            avg_pan_temp_10 REAL,
                            highest_pan_temp_10 REAL,
                            lowest_pan_temp_10 REAL,
                            avg_food_temp_10 REAL,
                            highest_food_temp_10 REAL,
                            lowest_food_temp_10 REAL,
                            time_elapsed_11 INTEGER,
                            avg_pan_temp_11 REAL,
                            highest_pan_temp_11 REAL,
                            lowest_pan_temp_11 REAL,
                            avg_food_temp_11 REAL,
                            highest_food_temp_11 REAL,
                            lowest_food_temp_11 REAL,
                            time_elapsed_12 INTEGER,
                            avg_pan_temp_12 REAL,
                            highest_pan_temp_12 REAL,
                            lowest_pan_temp_12 REAL,
                            avg_food_temp_12 REAL,
                            highest_food_temp_12 REAL,
                            lowest_food_temp_12 REAL,
                            time_elapsed_13 INTEGER,
                            avg_pan_temp_13 REAL,
                            highest_pan_temp_13 REAL,
                            lowest_pan_temp_13 REAL,
                            avg_food_temp_13 REAL,
                            highest_food_temp_13 REAL,
                            lowest_food_temp_13 REAL,
                            time_elapsed_14 INTEGER,
                            avg_pan_temp_14 REAL,
                            highest_pan_temp_14 REAL,
                            lowest_pan_temp_14 REAL,
                            avg_food_temp_14 REAL,
                            highest_food_temp_14 REAL,
                            lowest_food_temp_14 REAL,
                            time_elapsed_15 INTEGER,
                            avg_pan_temp_15 REAL,
                            highest_pan_temp_15 REAL,
                            lowest_pan_temp_15 REAL,
                            avg_food_temp_15 REAL,
                            highest_food_temp_15 REAL,
                            lowest_food_temp_15 REAL,
                            time_elapsed_16 INTEGER,
                            avg_pan_temp_16 REAL,
                            highest_pan_temp_16 REAL,
                            lowest_pan_temp_16 REAL,
                            avg_food_temp_16 REAL,
                            highest_food_temp_16 REAL,
                            lowest_food_temp_16 REAL,
                            time_elapsed_17 INTEGER,
                            avg_pan_temp_17 REAL,
                            highest_pan_temp_17 REAL,
                            lowest_pan_temp_17 REAL,
                            avg_food_temp_17 REAL,
                            highest_food_temp_17 REAL,
                            lowest_food_temp_17 REAL,
                            time_elapsed_18 INTEGER,
                            avg_pan_temp_18 REAL,
                            highest_pan_temp_18 REAL,
                            lowest_pan_temp_18 REAL,
                            avg_food_temp_18 REAL,
                            highest_food_temp_18 REAL,
                            lowest_food_temp_18 REAL,
                            time_elapsed_19 INTEGER,
                            avg_pan_temp_19 REAL,
                            highest_pan_temp_19 REAL,
                            lowest_pan_temp_19 REAL,
                            avg_food_temp_19 REAL,
                            highest_food_temp_19 REAL,
                            lowest_food_temp_19 REAL,
                            time_elapsed_20 INTEGER,
                            avg_pan_temp_20 REAL,
                            highest_pan_temp_20 REAL,
                            lowest_pan_temp_20 REAL,
                            avg_food_temp_20 REAL,
                            highest_food_temp_20 REAL,
                            lowest_food_temp_20 REAL                    
                        )''')
        c.close()
    conn.close()


# 2023: Method that saving frame data in testdata table to be transferred to csv using testdata model
def insert_testdata(testdata):
    ''' Insert a testdata into the testdata table.
    
    Args:
        testdata(testdata): The testdata to insert
    
    Returns:
        None
    '''
    # Create testdata table if it does not already exist
    create_testdata_table()

    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        try:
            # we have 143 values in the testdata model
            c.execute('INSERT INTO testdata VALUES (?,?,?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?)',
             testdata.get_as_record())
            print('Successfully inserted testdata')
        except AttributeError:
            print('Testdata to be inserted is not of type TestData: {}'.format(type(TestData)))
        except:
            print('An unexpected error occurred when inserting a record into the testdata table')
        finally:
            c.close()
    conn.close()

# 2023: Method that create a new table for saving frame data to be transferred to csv using testdataWithId model
def create_testdataWithId_table():
    ''' Create the master testdataWithId table. 
    The master testdataWithId table stores high-level information about thermal videos.
    This inlcudes everything that goes into the csv for machine learning purpose.
    
    Args:
        None
    
    Returns:
        None
    '''
    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        # Check if the testdataWithId table already exists
        c.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='testdataWithId'")
        if c.fetchone()[0] == 0:
            c.execute('''CREATE TABLE testdataWithId (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            stoveId INETEGER,
                            state INTEGER,
                            type INTEGER,
                            safety INTEGER,
                            time_elapsed_1 INTEGER,
                            avg_pan_temp_1 REAL,
                            highest_pan_temp_1 REAL,
                            lowest_pan_temp_1 REAL,
                            avg_food_temp_1 REAL,
                            highest_food_temp_1 REAL,
                            lowest_food_temp_1 REAL,
                            time_elapsed_2 INTEGER,
                            avg_pan_temp_2 REAL,
                            highest_pan_temp_2 REAL,
                            lowest_pan_temp_2 REAL,
                            avg_food_temp_2 REAL,
                            highest_food_temp_2 REAL,
                            lowest_food_temp_2 REAL,
                            time_elapsed_3 INTEGER,
                            avg_pan_temp_3 REAL,
                            highest_pan_temp_3 REAL,
                            lowest_pan_temp_3 REAL,
                            avg_food_temp_3 REAL,
                            highest_food_temp_3 REAL,
                            lowest_food_temp_3 REAL,
                            time_elapsed_4 INTEGER,
                            avg_pan_temp_4 REAL,
                            highest_pan_temp_4 REAL,
                            lowest_pan_temp_4 REAL,
                            avg_food_temp_4 REAL,
                            highest_food_temp_4 REAL,
                            lowest_food_temp_4 REAL,
                            time_elapsed_5 INTEGER,
                            avg_pan_temp_5 REAL,
                            highest_pan_temp_5 REAL,
                            lowest_pan_temp_5 REAL,
                            avg_food_temp_5 REAL,
                            highest_food_temp_5 REAL,
                            lowest_food_temp_5 REAL,
                            time_elapsed_6 INTEGER,
                            avg_pan_temp_6 REAL,
                            highest_pan_temp_6 REAL,
                            lowest_pan_temp_6 REAL,
                            avg_food_temp_6 REAL,
                            highest_food_temp_6 REAL,
                            lowest_food_temp_6 REAL,
                            time_elapsed_7 INTEGER,
                            avg_pan_temp_7 REAL,
                            highest_pan_temp_7 REAL,
                            lowest_pan_temp_7 REAL,
                            avg_food_temp_7 REAL,
                            highest_food_temp_7 REAL,
                            lowest_food_temp_7 REAL,
                            time_elapsed_8 INTEGER,
                            avg_pan_temp_8 REAL,
                            highest_pan_temp_8 REAL,
                            lowest_pan_temp_8 REAL,
                            avg_food_temp_8 REAL,
                            highest_food_temp_8 REAL,
                            lowest_food_temp_8 REAL,
                            time_elapsed_9 INTEGER,
                            avg_pan_temp_9 REAL,
                            highest_pan_temp_9 REAL,
                            lowest_pan_temp_9 REAL,
                            avg_food_temp_9 REAL,
                            highest_food_temp_9 REAL,
                            lowest_food_temp_9 REAL,
                            time_elapsed_10 INTEGER,
                            avg_pan_temp_10 REAL,
                            highest_pan_temp_10 REAL,
                            lowest_pan_temp_10 REAL,
                            avg_food_temp_10 REAL,
                            highest_food_temp_10 REAL,
                            lowest_food_temp_10 REAL,
                            time_elapsed_11 INTEGER,
                            avg_pan_temp_11 REAL,
                            highest_pan_temp_11 REAL,
                            lowest_pan_temp_11 REAL,
                            avg_food_temp_11 REAL,
                            highest_food_temp_11 REAL,
                            lowest_food_temp_11 REAL,
                            time_elapsed_12 INTEGER,
                            avg_pan_temp_12 REAL,
                            highest_pan_temp_12 REAL,
                            lowest_pan_temp_12 REAL,
                            avg_food_temp_12 REAL,
                            highest_food_temp_12 REAL,
                            lowest_food_temp_12 REAL,
                            time_elapsed_13 INTEGER,
                            avg_pan_temp_13 REAL,
                            highest_pan_temp_13 REAL,
                            lowest_pan_temp_13 REAL,
                            avg_food_temp_13 REAL,
                            highest_food_temp_13 REAL,
                            lowest_food_temp_13 REAL,
                            time_elapsed_14 INTEGER,
                            avg_pan_temp_14 REAL,
                            highest_pan_temp_14 REAL,
                            lowest_pan_temp_14 REAL,
                            avg_food_temp_14 REAL,
                            highest_food_temp_14 REAL,
                            lowest_food_temp_14 REAL,
                            time_elapsed_15 INTEGER,
                            avg_pan_temp_15 REAL,
                            highest_pan_temp_15 REAL,
                            lowest_pan_temp_15 REAL,
                            avg_food_temp_15 REAL,
                            highest_food_temp_15 REAL,
                            lowest_food_temp_15 REAL,
                            time_elapsed_16 INTEGER,
                            avg_pan_temp_16 REAL,
                            highest_pan_temp_16 REAL,
                            lowest_pan_temp_16 REAL,
                            avg_food_temp_16 REAL,
                            highest_food_temp_16 REAL,
                            lowest_food_temp_16 REAL,
                            time_elapsed_17 INTEGER,
                            avg_pan_temp_17 REAL,
                            highest_pan_temp_17 REAL,
                            lowest_pan_temp_17 REAL,
                            avg_food_temp_17 REAL,
                            highest_food_temp_17 REAL,
                            lowest_food_temp_17 REAL,
                            time_elapsed_18 INTEGER,
                            avg_pan_temp_18 REAL,
                            highest_pan_temp_18 REAL,
                            lowest_pan_temp_18 REAL,
                            avg_food_temp_18 REAL,
                            highest_food_temp_18 REAL,
                            lowest_food_temp_18 REAL,
                            time_elapsed_19 INTEGER,
                            avg_pan_temp_19 REAL,
                            highest_pan_temp_19 REAL,
                            lowest_pan_temp_19 REAL,
                            avg_food_temp_19 REAL,
                            highest_food_temp_19 REAL,
                            lowest_food_temp_19 REAL,
                            time_elapsed_20 INTEGER,
                            avg_pan_temp_20 REAL,
                            highest_pan_temp_20 REAL,
                            lowest_pan_temp_20 REAL,
                            avg_food_temp_20 REAL,
                            highest_food_temp_20 REAL,
                            lowest_food_temp_20 REAL                    
                        )''')
        c.close()
    conn.close()


# 2023: Method that saving testdataWithId in testdataWithId table for to be transferred to csv 
# using testdataWithId model
def insert_testdataWithId(testdataWithId):
    ''' Insert a testdataWithId into the master testdataWithId table.
    
    Args:
        testdataWithId(testdataWithId): The testdataWithId to insert
    
    Returns:
        None
    '''
    # Create testdataWithId table if it does not already exist
    create_testdataWithId_table()

    conn = sqlite3.connect(DATABASE)
    with conn:
        c = conn.cursor()
        try:
            # we have 145 values
            c.execute('INSERT INTO testdataWithId VALUES (null,?,?,?,?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?)',
             testdataWithId.get_as_record())
            print('Successfully inserted testdataWithId')
        except AttributeError:
            print('testdataWithId to be inserted is not of type testdataWithId: {}'.format(type(TestDataWithId)))
        except:
            print('An unexpected error occurred when inserting a record into the testdataWithId table')
        finally:
            c.close()
    conn.close()

# 2023: Edited Method to fit with the testdataWithId model
def add_video_from_filename(filename):
    ''' Analyzes a video given its filename and stores its analytical data
    (FrameData records) into the database.

    The provided filename must contain the 'Test Data' folder as part of its path.

    Args:
        filename (str): The filename of the video to analyze and store

    Returns:
        None
    '''
    # new to check duration
    # print(filename)
    # print("Enter database.py")
    rate = getFrameRate(filename)
    

    # Replace '\\' with '/' to handle incoming filenames
    filename = filename.replace('\\', '/')

    # Trim leading path up until the Test Data folder
    filename = filename[filename.find('Test Data'):]

    # Get the type of the video (e.g., Frying)
    type = filename.split('/')[1]

    # Get the subtype of the video (e.g., Chicken)
    subtype = filename[filename.find('[')+1:filename.find(']')]

    # Create an analysis table whose name is based on the subtype
    analysisTableName = create_analysis_table(subtype)

    # Set stove ID to 1 since we only have one stove
    stoveId = 1

    
    print("Frame rate in database: " + str(rate))
    # Get frame data from video(new change in 2023)=> sampleRate from 10 to 40 to (Dynamic)60 to 40 to attempt at equally spaced 20 frames
    frameData = processVideo(filename, rate)

    # Add frame data to the analysis table
    frameDataObjs = []
    #Add all frame data in an array for testdata table
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

        newFrameData = FrameData(timeElapsed, avgPanTemp, highPanTemp, lowPanTemp, avgFoodTemp, highFoodTemp, lowFoodTemp)
        frameDataObjs.append(newFrameData)

    #For testdata table, set state, type and safety to 0 and change it when we generate the csv
    testdataArray = [0,0,0] + setData

    #For testdataWithId table, set stoveId to 1 and change it when we generate the csv
    testdataWithIdArray = [1,0,0,0] + setData

    insert_many_frame_data(frameDataObjs, analysisTableName)

    # Add a record to the videos master table 
    # Set to "Trial 2023" as not hard coding the classification,manual data labelling after image processing
    overallClassification = "Trial 2023"
    video = Video(type, subtype, filename, analysisTableName, overallClassification, stoveId)
    insert_video(video)

    #2023 For testdata table, * to unpack elements in testdataArray
    testdata = TestData(*testdataArray)
    insert_testdata(testdata)

    #2023 testdataWithId
    testdataWithId = TestDataWithId(*testdataWithIdArray)
    insert_testdataWithId(testdataWithId)


# Example
if __name__ == '__main__':
    frameData = get_all_frame_data('Three_Mushrooms_Analysis_Table_1')
    print(frameData)
    getFrameRate()