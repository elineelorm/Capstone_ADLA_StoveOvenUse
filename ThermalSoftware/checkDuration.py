from moviepy.editor import VideoFileClip
filename = "C:/Users/jaime/Desktop/SYSC4907A/Code/Capstone_ADLA_StoveOvenUse/ThermalSoftware/Test Data/2023.01.09-19.27.32 [Boiling water].mp4"
print(filename)
video = VideoFileClip(filename)

print(video.duration/60)