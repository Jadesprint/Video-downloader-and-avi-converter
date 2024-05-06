# Video-downloader-and-avi-converter
Python script for video downloading from youtube and mp4 to avi converter

# Modules used:
- Pytube
- Moviepy

Moviepy is used for te mp4-avi conversion using moviepy.editor and VideoFileClip class
Pytube as the name suggest downloads the video you input in the console (link), it is noteworthy that you can't download literal Youtube clips from the Clips 
official feature, since this just creates a private enviroment in your channel for people to watch a determined length from a video that is not yours so
it simply won't work, must be a public video that is posted in Youtube, wether is a normal video or a Youtube Short.

# Usage
- Make sure to pip-install the modules above
For this just open a terminal (win+r, then write cmd in the text box), then write pip install [module name]
- Preferably create a folder which you will use for saving your videos
- Run this script in the folder, it'll ask you for a link and that's it
- Additional feature:
I added a txt file as a log for you to check which videos you've downloaded at the moment, it shows you title, duration and a "success" message when download is, well, successful.
- Both Mp4 and Avi video will be saved in the folder
