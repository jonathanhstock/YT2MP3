from pytube import YouTube
import os

# URL input from user
yt = YouTube(str(input("Enter the URL you want to download: \n >> ")))
video = yt.streams.filter(only_audio=True).first()
# destination input from user
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or "."

# download the YouTube video
out_file = video.download(output_path=destination)

# save the video as an mp3 file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# print download has been completed
print(yt.title + " has been successfully downloaded.")
