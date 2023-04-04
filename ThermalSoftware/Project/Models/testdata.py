#from msilib.schema import Class
class TestData:
    ''' 
    //Change this!
    An instance of TestData represents a frame that is sampled from a thermal video created in 2023.
    FrameData records are stored in an analysis table pertaining to the specific thermal video file.

    
    Each instance of FrameData contains the following fields:
        timeElapsed (INTEGER) - The elapsed time (in seconds) since the beginning of the time the frame was sampled (primary key)
        panTemp (REAL) - The average temperature of the pan (in Celsius)
        panArea (INTEGER) - The area of the pan (in pixels)
        numFood (INTEGER) - The number of food elements
        foodTemp (TEXT) - The string representation of an array containing temperatures (in Celsius) of each identified food
        foodArea (TEXT) - The string representation of an array containing the areas (in pixels) of each identified food
        classification (TEXT) - The classification of the frame specified by the classifier
    '''
    def __init__(self, state, type, safety, time_elapsed_1, avg_pan_temp_1, highest_pan_temp_1, lowest_pan_temp_1, avg_food_temp_1, highest_food_temp_1, lowest_food_temp_1, 
        time_elapsed_2, avg_pan_temp_2, highest_pan_temp_2, lowest_pan_temp_2, avg_food_temp_2, highest_food_temp_2, lowest_food_temp_2, 
        time_elapsed_3, avg_pan_temp_3, highest_pan_temp_3, lowest_pan_temp_3, avg_food_temp_3, highest_food_temp_3, lowest_food_temp_3, 
        time_elapsed_4, avg_pan_temp_4, highest_pan_temp_4, lowest_pan_temp_4, avg_food_temp_4, highest_food_temp_4, lowest_food_temp_4,
        time_elapsed_5, avg_pan_temp_5, highest_pan_temp_5, lowest_pan_temp_5, avg_food_temp_5, highest_food_temp_5, lowest_food_temp_5,
        time_elapsed_6, avg_pan_temp_6, highest_pan_temp_6, lowest_pan_temp_6, avg_food_temp_6, highest_food_temp_6, lowest_food_temp_6,
        time_elapsed_7, avg_pan_temp_7, highest_pan_temp_7, lowest_pan_temp_7, avg_food_temp_7, highest_food_temp_7, lowest_food_temp_7,
        time_elapsed_8, avg_pan_temp_8, highest_pan_temp_8, lowest_pan_temp_8, avg_food_temp_8, highest_food_temp_8, lowest_food_temp_8,
        time_elapsed_9, avg_pan_temp_9, highest_pan_temp_9, lowest_pan_temp_9, avg_food_temp_9, highest_food_temp_9, lowest_food_temp_9,
        time_elapsed_10, avg_pan_temp_10, highest_pan_temp_10, lowest_pan_temp_10, avg_food_temp_10, highest_food_temp_10, lowest_food_temp_10,      
        time_elapsed_11, avg_pan_temp_11, highest_pan_temp_11, lowest_pan_temp_11, avg_food_temp_11, highest_food_temp_11, lowest_food_temp_11,      
        time_elapsed_12, avg_pan_temp_12, highest_pan_temp_12, lowest_pan_temp_12, avg_food_temp_12, highest_food_temp_12, lowest_food_temp_12,      
        time_elapsed_13, avg_pan_temp_13, highest_pan_temp_13, lowest_pan_temp_13, avg_food_temp_13, highest_food_temp_13, lowest_food_temp_13,      
        time_elapsed_14, avg_pan_temp_14, highest_pan_temp_14, lowest_pan_temp_14, avg_food_temp_14, highest_food_temp_14, lowest_food_temp_14,      
        time_elapsed_15, avg_pan_temp_15, highest_pan_temp_15, lowest_pan_temp_15, avg_food_temp_15, highest_food_temp_15, lowest_food_temp_15,      
        time_elapsed_16, avg_pan_temp_16, highest_pan_temp_16, lowest_pan_temp_16, avg_food_temp_16, highest_food_temp_16, lowest_food_temp_16,      
        time_elapsed_17, avg_pan_temp_17, highest_pan_temp_17, lowest_pan_temp_17, avg_food_temp_17, highest_food_temp_17, lowest_food_temp_17,      
        time_elapsed_18, avg_pan_temp_18, highest_pan_temp_18, lowest_pan_temp_18, avg_food_temp_18, highest_food_temp_18, lowest_food_temp_18,      
        time_elapsed_19, avg_pan_temp_19, highest_pan_temp_19, lowest_pan_temp_19, avg_food_temp_19, highest_food_temp_19, lowest_food_temp_19,      
        time_elapsed_20, avg_pan_temp_20, highest_pan_temp_20, lowest_pan_temp_20, avg_food_temp_20, highest_food_temp_20, lowest_food_temp_20):
            self._state = state
            self._type = type
            self._safety = safety
            self._timeElapsed_1 = time_elapsed_1     
            self._avgPanTemp_1 = avg_pan_temp_1      
            self._higPanTemp_1 = highest_pan_temp_1  
            self._lowPanTemp_1 = lowest_pan_temp_1   
            self._avgFoodTemp_1 = avg_food_temp_1    
            self._higFoodTemp_1 = highest_food_temp_1
            self._lowFoodTemp_1 = lowest_food_temp_1 

            self._timeElapsed_2 = time_elapsed_2     
            self._avgPanTemp_2 = avg_pan_temp_2      
            self._higPanTemp_2 = highest_pan_temp_2  
            self._lowPanTemp_2 = lowest_pan_temp_2   
            self._avgFoodTemp_2 = avg_food_temp_2    
            self._higFoodTemp_2 = highest_food_temp_2
            self._lowFoodTemp_2 = lowest_food_temp_2

            self._timeElapsed_3 = time_elapsed_3
            self._avgPanTemp_3 = avg_pan_temp_3
            self._higPanTemp_3 = highest_pan_temp_3
            self._lowPanTemp_3 = lowest_pan_temp_3
            self._avgFoodTemp_3 = avg_food_temp_3
            self._higFoodTemp_3 = highest_food_temp_3
            self._lowFoodTemp_3 = lowest_food_temp_3

            self._timeElapsed_4 = time_elapsed_4
            self._avgPanTemp_4 = avg_pan_temp_4
            self._higPanTemp_4 = highest_pan_temp_4
            self._lowPanTemp_4 = lowest_pan_temp_4
            self._avgFoodTemp_4 = avg_food_temp_4
            self._higFoodTemp_4 = highest_food_temp_4
            self._lowFoodTemp_4 = lowest_food_temp_4

            self._timeElapsed_5 = time_elapsed_5
            self._avgPanTemp_5 = avg_pan_temp_5
            self._higPanTemp_5 = highest_pan_temp_5
            self._lowPanTemp_5 = lowest_pan_temp_5
            self._avgFoodTemp_5 = avg_food_temp_5
            self._higFoodTemp_5 = highest_food_temp_5
            self._lowFoodTemp_5 = lowest_food_temp_5

            self._timeElapsed_6 = time_elapsed_6
            self._avgPanTemp_6 = avg_pan_temp_6
            self._higPanTemp_6 = highest_pan_temp_6
            self._lowPanTemp_6 = lowest_pan_temp_6
            self._avgFoodTemp_6 = avg_food_temp_6
            self._higFoodTemp_6 = highest_food_temp_6
            self._lowFoodTemp_6 = lowest_food_temp_6

            self._timeElapsed_7 = time_elapsed_7
            self._avgPanTemp_7 = avg_pan_temp_7
            self._higPanTemp_7 = highest_pan_temp_7
            self._lowPanTemp_7 = lowest_pan_temp_7
            self._avgFoodTemp_7 = avg_food_temp_7
            self._higFoodTemp_7 = highest_food_temp_7
            self._lowFoodTemp_7 = lowest_food_temp_7

            self._timeElapsed_8 = time_elapsed_8
            self._avgPanTemp_8 = avg_pan_temp_8
            self._higPanTemp_8 = highest_pan_temp_8
            self._lowPanTemp_8 = lowest_pan_temp_8
            self._avgFoodTemp_8 = avg_food_temp_8
            self._higFoodTemp_8 = highest_food_temp_8
            self._lowFoodTemp_8 = lowest_food_temp_8

            self._timeElapsed_9 = time_elapsed_9
            self._avgPanTemp_9 = avg_pan_temp_9
            self._higPanTemp_9 = highest_pan_temp_9
            self._lowPanTemp_9 = lowest_pan_temp_9
            self._avgFoodTemp_9 = avg_food_temp_9
            self._higFoodTemp_9 = highest_food_temp_9
            self._lowFoodTemp_9 = lowest_food_temp_9

            self._timeElapsed_10 = time_elapsed_10
            self._avgPanTemp_10 = avg_pan_temp_10
            self._higPanTemp_10 = highest_pan_temp_10
            self._lowPanTemp_10 = lowest_pan_temp_10
            self._avgFoodTemp_10 = avg_food_temp_10
            self._higFoodTemp_10 = highest_food_temp_10
            self._lowFoodTemp_10 = lowest_food_temp_10

            self._timeElapsed_11 = time_elapsed_11
            self._avgPanTemp_11 = avg_pan_temp_11
            self._higPanTemp_11 = highest_pan_temp_11
            self._lowPanTemp_11 = lowest_pan_temp_11
            self._avgFoodTemp_11 = avg_food_temp_11
            self._higFoodTemp_11 = highest_food_temp_11
            self._lowFoodTemp_11 = lowest_food_temp_11

            self._timeElapsed_12 = time_elapsed_12
            self._avgPanTemp_12 = avg_pan_temp_12
            self._higPanTemp_12 = highest_pan_temp_12
            self._lowPanTemp_12 = lowest_pan_temp_12
            self._avgFoodTemp_12 = avg_food_temp_12
            self._higFoodTemp_12 = highest_food_temp_12
            self._lowFoodTemp_12 = lowest_food_temp_12

            self._timeElapsed_13 = time_elapsed_13
            self._avgPanTemp_13 = avg_pan_temp_13
            self._higPanTemp_13 = highest_pan_temp_13
            self._lowPanTemp_13 = lowest_pan_temp_13
            self._avgFoodTemp_13 = avg_food_temp_13
            self._higFoodTemp_13 = highest_food_temp_13
            self._lowFoodTemp_13 = lowest_food_temp_13

            self._timeElapsed_14 = time_elapsed_14
            self._avgPanTemp_14 = avg_pan_temp_14
            self._higPanTemp_14 = highest_pan_temp_14
            self._lowPanTemp_14 = lowest_pan_temp_14
            self._avgFoodTemp_14 = avg_food_temp_14
            self._higFoodTemp_14 = highest_food_temp_14
            self._lowFoodTemp_14 = lowest_food_temp_14

            self._timeElapsed_15 = time_elapsed_15
            self._avgPanTemp_15 = avg_pan_temp_15
            self._higPanTemp_15 = highest_pan_temp_15
            self._lowPanTemp_15 = lowest_pan_temp_15
            self._avgFoodTemp_15 = avg_food_temp_15
            self._higFoodTemp_15 = highest_food_temp_15
            self._lowFoodTemp_15 = lowest_food_temp_15

            self._timeElapsed_16 = time_elapsed_16
            self._avgPanTemp_16 = avg_pan_temp_16
            self._higPanTemp_16 = highest_pan_temp_16
            self._lowPanTemp_16 = lowest_pan_temp_16
            self._avgFoodTemp_16 = avg_food_temp_16
            self._higFoodTemp_16 = highest_food_temp_16
            self._lowFoodTemp_16 = lowest_food_temp_16

            self._timeElapsed_17 = time_elapsed_17
            self._avgPanTemp_17 = avg_pan_temp_17
            self._higPanTemp_17 = highest_pan_temp_17
            self._lowPanTemp_17 = lowest_pan_temp_17
            self._avgFoodTemp_17 = avg_food_temp_17
            self._higFoodTemp_17 = highest_food_temp_17
            self._lowFoodTemp_17 = lowest_food_temp_17

            self._timeElapsed_18 = time_elapsed_18
            self._avgPanTemp_18 = avg_pan_temp_18
            self._higPanTemp_18 = highest_pan_temp_18
            self._lowPanTemp_18 = lowest_pan_temp_18
            self._avgFoodTemp_18 = avg_food_temp_18
            self._higFoodTemp_18 = highest_food_temp_18
            self._lowFoodTemp_18 = lowest_food_temp_18

            self._timeElapsed_19 = time_elapsed_19
            self._avgPanTemp_19 = avg_pan_temp_19
            self._higPanTemp_19 = highest_pan_temp_19
            self._lowPanTemp_19 = lowest_pan_temp_19
            self._avgFoodTemp_19 = avg_food_temp_19
            self._higFoodTemp_19 = highest_food_temp_19
            self._lowFoodTemp_19 = lowest_food_temp_19

            self._timeElapsed_20 = time_elapsed_20
            self._avgPanTemp_20 = avg_pan_temp_20
            self._higPanTemp_20 = highest_pan_temp_20
            self._lowPanTemp_20 = lowest_pan_temp_20
            self._avgFoodTemp_20 = avg_food_temp_20
            self._higFoodTemp_20 = highest_food_temp_20
            self._lowFoodTemp_20 = lowest_food_temp_20
            
    @property
    def state(self):
        return self._state

    @property
    def type(self):
        return self._type

    @property
    def safety(self):
        return self._safety

    @property
    def timeElapsed_1(self):
        return self._timeElapsed_1
    @property
    def avgPanTemp_1(self):
        return self._avgPanTemp_1
    @property
    def higPanTemp_1(self):
        return self._higPanTemp_1
    @property
    def lowPanTemp_1(self):
        return self._lowPanTemp_1
    @property
    def avgFoodTemp_1(self):
        return self._avgFoodTemp_1
    @property
    def higFoodTemp_1(self):
        return self._higFoodTemp_1
    @property
    def lowFoodTemp_1(self):
        return self._lowFoodTemp_1
    @property
    def timeElapsed_2(self):
        return self._timeElapsed_2
    @property
    def avgPanTemp_2(self):
        return self._avgPanTemp_2
    @property
    def higPanTemp_2(self):
        return self._higPanTemp_2
    @property
    def lowPanTemp_2(self):
        return self._lowPanTemp_2
    @property
    def avgFoodTemp_2(self):
        return self._avgFoodTemp_2
    @property
    def higFoodTemp_2(self):
        return self._higFoodTemp_2
    @property
    def lowFoodTemp_2(self):
        return self._lowFoodTemp_2
    @property
    def timeElapsed_3(self):
        return self._timeElapsed_3
    @property
    def avgPanTemp_3(self):
        return self._avgPanTemp_3
    @property
    def higPanTemp_3(self):
        return self._higPanTemp_3
    @property
    def lowPanTemp_3(self):
        return self._lowPanTemp_3
    @property
    def avgFoodTemp_3(self):
        return self._avgFoodTemp_3
    @property
    def higFoodTemp_3(self):
        return self._higFoodTemp_3
    @property
    def lowFoodTemp_3(self):
        return self._lowFoodTemp_3
    @property
    def timeElapsed_4(self):
        return self._timeElapsed_4
    @property
    def avgPanTemp_4(self):
        return self._avgPanTemp_4
    @property
    def higPanTemp_4(self):
        return self._higPanTemp_4
    @property
    def lowPanTemp_4(self):
        return self._lowPanTemp_4
    @property
    def avgFoodTemp_4(self):
        return self._avgFoodTemp_4
    @property
    def higFoodTemp_4(self):
        return self._higFoodTemp_4
    @property
    def lowFoodTemp_4(self):
        return self._lowFoodTemp_4
    @property
    def timeElapsed_5(self):
        return self._timeElapsed_5
    @property
    def avgPanTemp_5(self):
        return self._avgPanTemp_5
    @property
    def higPanTemp_5(self):
        return self._higPanTemp_5
    @property
    def lowPanTemp_5(self):
        return self._lowPanTemp_5
    @property
    def avgFoodTemp_5(self):
        return self._avgFoodTemp_5
    @property
    def higFoodTemp_5(self):
        return self._higFoodTemp_5
    @property
    def lowFoodTemp_5(self):
        return self._lowFoodTemp_5
    @property
    def timeElapsed_6(self):
        return self._timeElapsed_6
    @property
    def avgPanTemp_6(self):
        return self._avgPanTemp_6
    @property
    def higPanTemp_6(self):
        return self._higPanTemp_6
    @property
    def lowPanTemp_6(self):
        return self._lowPanTemp_6
    @property
    def avgFoodTemp_6(self):
        return self._avgFoodTemp_6
    @property
    def higFoodTemp_6(self):
        return self._higFoodTemp_6
    @property
    def lowFoodTemp_6(self):
        return self._lowFoodTemp_6
    @property
    def timeElapsed_7(self):
        return self._timeElapsed_7
    @property
    def avgPanTemp_7(self):
        return self._avgPanTemp_7
    @property
    def higPanTemp_7(self):
        return self._higPanTemp_7
    @property
    def lowPanTemp_7(self):
        return self._lowPanTemp_7
    @property
    def avgFoodTemp_7(self):
        return self._avgFoodTemp_7
    @property
    def higFoodTemp_7(self):
        return self._higFoodTemp_7
    @property
    def lowFoodTemp_7(self):
        return self._lowFoodTemp_7
    @property
    def timeElapsed_8(self):
        return self._timeElapsed_8
    @property
    def avgPanTemp_8(self):
        return self._avgPanTemp_8
    @property
    def higPanTemp_8(self):
        return self._higPanTemp_8
    @property
    def lowPanTemp_8(self):
        return self._lowPanTemp_8
    @property
    def avgFoodTemp_8(self):
        return self._avgFoodTemp_8
    @property
    def higFoodTemp_8(self):
        return self._higFoodTemp_8
    @property
    def lowFoodTemp_8(self):
        return self._lowFoodTemp_8
    @property
    def timeElapsed_9(self):
        return self._timeElapsed_9
    @property
    def avgPanTemp_9(self):
        return self._avgPanTemp_9
    @property
    def higPanTemp_9(self):
        return self._higPanTemp_9
    @property
    def lowPanTemp_9(self):
        return self._lowPanTemp_9
    @property
    def avgFoodTemp_9(self):
        return self._avgFoodTemp_9
    @property
    def higFoodTemp_9(self):
        return self._higFoodTemp_9
    @property
    def lowFoodTemp_9(self):
        return self._lowFoodTemp_9
    @property
    def timeElapsed_10(self):
        return self._timeElapsed_10
    @property
    def avgPanTemp_10(self):
        return self._avgPanTemp_10
    @property
    def higPanTemp_10(self):
        return self._higPanTemp_10
    @property
    def lowPanTemp_10(self):
        return self._lowPanTemp_10
    @property
    def avgFoodTemp_10(self):
        return self._avgFoodTemp_10
    @property
    def higFoodTemp_10(self):
        return self._higFoodTemp_10
    @property
    def lowFoodTemp_10(self):
        return self._lowFoodTemp_10
    @property
    def timeElapsed_11(self):
        return self._timeElapsed_11
    @property
    def avgPanTemp_11(self):
        return self._avgPanTemp_11
    @property
    def higPanTemp_11(self):
        return self._higPanTemp_11
    @property
    def lowPanTemp_11(self):
        return self._lowPanTemp_11
    @property
    def avgFoodTemp_11(self):
        return self._avgFoodTemp_11
    @property
    def higFoodTemp_11(self):
        return self._higFoodTemp_11
    @property
    def lowFoodTemp_11(self):
        return self._lowFoodTemp_11
    @property
    def timeElapsed_12(self):
        return self._timeElapsed_12
    @property
    def avgPanTemp_12(self):
        return self._avgPanTemp_12
    @property
    def higPanTemp_12(self):
        return self._higPanTemp_12
    @property
    def lowPanTemp_12(self):
        return self._lowPanTemp_12
    @property
    def avgFoodTemp_12(self):
        return self._avgFoodTemp_12
    @property
    def higFoodTemp_12(self):
        return self._higFoodTemp_12
    @property
    def lowFoodTemp_12(self):
        return self._lowFoodTemp_12
    @property
    def timeElapsed_13(self):
        return self._timeElapsed_13
    @property
    def avgPanTemp_13(self):
        return self._avgPanTemp_13
    @property
    def higPanTemp_13(self):
        return self._higPanTemp_13
    @property
    def lowPanTemp_13(self):
        return self._lowPanTemp_13
    @property
    def avgFoodTemp_13(self):
        return self._avgFoodTemp_13
    @property
    def higFoodTemp_13(self):
        return self._higFoodTemp_13
    @property
    def lowFoodTemp_13(self):
        return self._lowFoodTemp_13
    @property
    def timeElapsed_14(self):
        return self._timeElapsed_14
    @property
    def avgPanTemp_14(self):
        return self._avgPanTemp_14
    @property
    def higPanTemp_14(self):
        return self._higPanTemp_14
    @property
    def lowPanTemp_14(self):
        return self._lowPanTemp_14
    @property
    def avgFoodTemp_14(self):
        return self._avgFoodTemp_14
    @property
    def higFoodTemp_14(self):
        return self._higFoodTemp_14
    @property
    def lowFoodTemp_14(self):
        return self._lowFoodTemp_14
    @property
    def timeElapsed_15(self):
        return self._timeElapsed_15
    @property
    def avgPanTemp_15(self):
        return self._avgPanTemp_15
    @property
    def higPanTemp_15(self):
        return self._higPanTemp_15
    @property
    def lowPanTemp_15(self):
        return self._lowPanTemp_15
    @property
    def avgFoodTemp_15(self):
        return self._avgFoodTemp_15
    @property
    def higFoodTemp_15(self):
        return self._higFoodTemp_15
    @property
    def lowFoodTemp_15(self):
        return self._lowFoodTemp_15
    @property
    def timeElapsed_16(self):
        return self._timeElapsed_16
    @property
    def avgPanTemp_16(self):
        return self._avgPanTemp_16
    @property
    def higPanTemp_16(self):
        return self._higPanTemp_16
    @property
    def lowPanTemp_16(self):
        return self._lowPanTemp_16
    @property
    def avgFoodTemp_16(self):
        return self._avgFoodTemp_16
    @property
    def higFoodTemp_16(self):
        return self._higFoodTemp_16
    @property
    def lowFoodTemp_16(self):
        return self._lowFoodTemp_16
    @property
    def timeElapsed_17(self):
        return self._timeElapsed_17
    @property
    def avgPanTemp_17(self):
        return self._avgPanTemp_17
    @property
    def higPanTemp_17(self):
        return self._higPanTemp_17
    @property
    def lowPanTemp_17(self):
        return self._lowPanTemp_17
    @property
    def avgFoodTemp_17(self):
        return self._avgFoodTemp_17
    @property
    def higFoodTemp_17(self):
        return self._higFoodTemp_17
    @property
    def lowFoodTemp_17(self):
        return self._lowFoodTemp_17
    @property
    def timeElapsed_18(self):
        return self._timeElapsed_18
    @property
    def avgPanTemp_18(self):
        return self._avgPanTemp_18
    @property
    def higPanTemp_18(self):
        return self._higPanTemp_18
    @property
    def lowPanTemp_18(self):
        return self._lowPanTemp_18
    @property
    def avgFoodTemp_18(self):
        return self._avgFoodTemp_18
    @property
    def higFoodTemp_18(self):
        return self._higFoodTemp_18
    @property
    def lowFoodTemp_18(self):
        return self._lowFoodTemp_18
    @property
    def timeElapsed_19(self):
        return self._timeElapsed_19
    @property
    def avgPanTemp_19(self):
        return self._avgPanTemp_19
    @property
    def higPanTemp_19(self):
        return self._higPanTemp_19
    @property
    def lowPanTemp_19(self):
        return self._lowPanTemp_19
    @property
    def avgFoodTemp_19(self):
        return self._avgFoodTemp_19
    @property
    def higFoodTemp_19(self):
        return self._higFoodTemp_19
    @property
    def lowFoodTemp_19(self):
        return self._lowFoodTemp_19
    @property
    def timeElapsed_20(self):
        return self._timeElapsed_20
    @property
    def avgPanTemp_20(self):
        return self._avgPanTemp_20
    @property
    def higPanTemp_20(self):
        return self._higPanTemp_20
    @property
    def lowPanTemp_20(self):
        return self._lowPanTemp_20
    @property
    def avgFoodTemp_20(self):
        return self._avgFoodTemp_20
    @property
    def higFoodTemp_20(self):
        return self._higFoodTemp_20
    @property
    def lowFoodTemp_20(self):
        return self._lowFoodTemp_20


    def get_as_record(self):
        return (self.state, self.type, self.safety, 
            self.timeElapsed_1, self.avgPanTemp_1, self.higPanTemp_1, self.lowPanTemp_1, self.avgFoodTemp_1, self.higFoodTemp_1, self.lowFoodTemp_1,
            self.timeElapsed_2, self.avgPanTemp_2, self.higPanTemp_2, self.lowPanTemp_2, self.avgFoodTemp_2, self.higFoodTemp_2, self.lowFoodTemp_2,   
            self.timeElapsed_3, self.avgPanTemp_3, self.higPanTemp_3, self.lowPanTemp_3, self.avgFoodTemp_3, self.higFoodTemp_3, self.lowFoodTemp_3,   
            self.timeElapsed_4, self.avgPanTemp_4, self.higPanTemp_4, self.lowPanTemp_4, self.avgFoodTemp_4, self.higFoodTemp_4, self.lowFoodTemp_4,   
            self.timeElapsed_5, self.avgPanTemp_5, self.higPanTemp_5, self.lowPanTemp_5, self.avgFoodTemp_5, self.higFoodTemp_5, self.lowFoodTemp_5,   
            self.timeElapsed_6, self.avgPanTemp_6, self.higPanTemp_6, self.lowPanTemp_6, self.avgFoodTemp_6, self.higFoodTemp_6, self.lowFoodTemp_6,   
            self.timeElapsed_7, self.avgPanTemp_7, self.higPanTemp_7, self.lowPanTemp_7, self.avgFoodTemp_7, self.higFoodTemp_7, self.lowFoodTemp_7,   
            self.timeElapsed_8, self.avgPanTemp_8, self.higPanTemp_8, self.lowPanTemp_8, self.avgFoodTemp_8, self.higFoodTemp_8, self.lowFoodTemp_8,   
            self.timeElapsed_9, self.avgPanTemp_9, self.higPanTemp_9, self.lowPanTemp_9, self.avgFoodTemp_9, self.higFoodTemp_9, self.lowFoodTemp_9,   
            self.timeElapsed_10, self.avgPanTemp_10, self.higPanTemp_10, self.lowPanTemp_10, self.avgFoodTemp_10, self.higFoodTemp_10, self.lowFoodTemp_10,
            self.timeElapsed_11, self.avgPanTemp_11, self.higPanTemp_11, self.lowPanTemp_11, self.avgFoodTemp_11, self.higFoodTemp_11, self.lowFoodTemp_11,
            self.timeElapsed_12, self.avgPanTemp_12, self.higPanTemp_12, self.lowPanTemp_12, self.avgFoodTemp_12, self.higFoodTemp_12, self.lowFoodTemp_12,
            self.timeElapsed_13, self.avgPanTemp_13, self.higPanTemp_13, self.lowPanTemp_13, self.avgFoodTemp_13, self.higFoodTemp_13, self.lowFoodTemp_13,
            self.timeElapsed_14, self.avgPanTemp_14, self.higPanTemp_14, self.lowPanTemp_14, self.avgFoodTemp_14, self.higFoodTemp_14, self.lowFoodTemp_14,
            self.timeElapsed_15, self.avgPanTemp_15, self.higPanTemp_15, self.lowPanTemp_15, self.avgFoodTemp_15, self.higFoodTemp_15, self.lowFoodTemp_15,
            self.timeElapsed_16, self.avgPanTemp_16, self.higPanTemp_16, self.lowPanTemp_16, self.avgFoodTemp_16, self.higFoodTemp_16, self.lowFoodTemp_16,
            self.timeElapsed_17, self.avgPanTemp_17, self.higPanTemp_17, self.lowPanTemp_17, self.avgFoodTemp_17, self.higFoodTemp_17, self.lowFoodTemp_17,
            self.timeElapsed_18, self.avgPanTemp_18, self.higPanTemp_18, self.lowPanTemp_18, self.avgFoodTemp_18, self.higFoodTemp_18, self.lowFoodTemp_18,
            self.timeElapsed_19, self.avgPanTemp_19, self.higPanTemp_19, self.lowPanTemp_19, self.avgFoodTemp_19, self.higFoodTemp_19, self.lowFoodTemp_19,
            self.timeElapsed_20, self.avgPanTemp_20, self.higPanTemp_20, self.lowPanTemp_20, self.avgFoodTemp_20, self.higFoodTemp_20, self.lowFoodTemp_20)
