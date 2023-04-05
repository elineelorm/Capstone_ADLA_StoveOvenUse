"""
    frame_data.py
    This file includes the frame_data model.
    
    Author: Group from 2021/2022 (Jonathan Mack)
    Edited by Hiu Sum Jaime Yue and Eline Elorm Nuviadenu

"""

class FrameData:
    ''' An instance of FrameData represents a frame that is sampled from a thermal video.
    FrameData records are stored in an analysis table pertaining to the specific thermal video file.

    Each instance of FrameData contains the following fields:
        timeElapsed (INTEGER) - The elapsed time (in seconds) since the beginning of the time the frame was sampled (primary key)
        avg_pan_temp (REAL) - The average temperature of the pan (in Celsius)
        highest_pan_temp (REAL) - The highest temperature of the pan (in Celsius)
        lowest_pan_temp (REAL) - The lowest temperature of the pan (in Celsius)
        avg_food_temp(REAL) - The average temperature of the food (in Celsius)
        highest_food_temp (REAL) - The highest temperature of the food (in Celsius)
        lowest_food_temp (REAL) - The lowest temperature of the food (in Celsius)
    '''
    def __init__(self, time_elapsed, avg_pan_temp, highest_pan_temp ,lowest_pan_temp, avg_food_temp, highest_food_temp, lowest_food_temp):
        self._timeElapsed = time_elapsed
        self._avgPanTemp = avg_pan_temp
        self._higPanTemp = highest_pan_temp
        self._lowPanTemp = lowest_pan_temp
        self._avgFoodTemp = avg_food_temp
        self._higFoodTemp = highest_food_temp
        self._lowFoodTemp = lowest_food_temp

    @property
    def timeElapsed(self):
        return self._timeElapsed

    @property
    def avgPanTemp(self):
        return self._avgPanTemp

    @property
    def higPanTemp(self):
        return self._higPanTemp

    @property
    def lowPanTemp(self):
        return self._lowPanTemp

    @property
    def avgFoodTemp(self):
        return self._avgFoodTemp

    @property
    def higFoodTemp(self):
        return self._higFoodTemp

    @property
    def lowFoodTemp(self):
        return self._lowFoodTemp

    def get_as_record(self):
        return (self.timeElapsed, self.avgPanTemp, self.higPanTemp, self.lowPanTemp, self.avgFoodTemp, self.higFoodTemp, self.lowFoodTemp)
