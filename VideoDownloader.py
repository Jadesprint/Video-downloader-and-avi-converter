from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
videoLog = open("Log.txt", mode="a")

def toAvi(inputFile, newFileName):
    try:
        clip = VideoFileClip(inputFile)
        clip.write_videofile(newFileName, codec = 'rawvideo', audio_codec='pcm_s16le')
        print("Conversion success")

    except Exception as a:
        print("Error raised: ", str(a))


def downloadVideo():
    try:
        video = input('Link: \n')
        video = YouTube(video)
        m, s = divmod(int(video.length), 60)
        videoLog.writelines(f'Title: {video.title} | Duration: {m}:{s}\n')
        video.streams.filter(progressive=True, file_extension='').order_by('resolution').desc().first().download()
        toAvi(video.title+".mp4", video.title+'.avi')
        videoLog.writelines("Success\n")

    except Exception as e:
        print('Something went wrong\n ', str(e))



def main():
    downloadVideo()
    



if __name__ == "__main__":
    main()