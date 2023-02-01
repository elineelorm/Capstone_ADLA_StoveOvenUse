from moviepy.editor import VideoFileClip

#To get frame rate of the 20 equally spaced frame 
def getFrameRate():
    #Need changes for it to pass in a path from dataClient.py
    filename = "C:/Users/jaime/Desktop/SYSC4907A/Code/Capstone_ADLA_StoveOvenUse/ThermalSoftware/Test Data/2023.01.09-19.27.32 [Boiling water 20Frames].mp4"
    print(filename)
    video = VideoFileClip(filename)

    print(str(video.duration/60) + " mins") #in mins
    print("Video length: " + str(video.duration))

    frameRate = video.duration//20 #round up
    print("Video frame rate: " + str(frameRate))

    return frameRate

# Example
if __name__ == '__main__':
    getFrameRate()

