from moviepy.editor import VideoFileClip

#To get frame rate of the 20 equally spaced frame 
def getFrameRate(filename):
    #Pass in a path from dataClient.py
    print("Enter getFrameRate()")
    print(filename)

    video = VideoFileClip(filename)

    print(str(video.duration/60) + " mins") #in mins
    print("Video length: " + str(video.duration) + " s")

    frameRate = video.duration//19 #round up Change from 20 to 19 (19 splits 20 equally space)
    print("Video frame rate: " + str(frameRate) + " seconds/frame in SQL")

    return frameRate

# Example
if __name__ == '__main__':
    getFrameRate()

