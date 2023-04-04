"""
    names.py
    This is a file for repetitive printing as a helper file for Models/testdata.py
    
    Author: Hiu Sum Jaime Yue
"""
x = range(1, 21)

for n in x:
    # print("time_elapsed_{}, avg_pan_temp_{},highest_pan_temp_{}, lowest_pan_temp_{}, avg_food_temp_{}, highest_food_temp_{}, lowest_food_temp_{},"
    # .format(n,n,n,n,n,n,n))
    # print("self._timeElapsed_{} = time_elapsed_{}\nself._avgPanTemp_{} = avg_pan_temp_{}\nself._higPanTemp_{} = highest_pan_temp_{}\nself._lowPanTemp_{} = lowest_pan_temp_{}\nself._avgFoodTemp_{} = avg_food_temp_{}\nself._higFoodTemp_{} = highest_food_temp_{}\nself._lowFoodTemp_{} = lowest_food_temp_{}\n"
    # .format(n,n,n,n,n,n,n,n,n,n,n,n,n,n))

    # print("@property\ndef timeElapsed_{}(self):\nreturn self._timeElapsed_{}\n@property\ndef avgPanTemp_{}(self):\nreturn self._avgPanTemp_{}\n@property\ndef higPanTemp_{}(self):\nreturn self._higPanTemp_{}\n@property\ndef lowPanTemp_{}(self):\nreturn self._lowPanTemp_{}\n@property\ndef avgFoodTemp_{}(self):\nreturn self._avgFoodTemp_{}\n@property\ndef higFoodTemp_{}(self):\nreturn self._higFoodTemp_{}\n@property\ndef lowFoodTemp_{}(self):\nreturn self._lowFoodTemp_{}"
    # .format(n,n,n,n,n,n,n,n,n,n,n,n,n,n))

    
    print("self.timeElapsed_{}, self.avgPanTemp_{}, self.higPanTemp_{}, self.lowPanTemp_{}, self.avgFoodTemp_{}, self.higFoodTemp_{}, self.lowFoodTemp_{},\n"
    .format(n,n,n,n,n,n,n))