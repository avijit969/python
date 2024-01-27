from pytube import YouTube

# Replace 'your_video_url' with the URL of the YouTube video you want to download
video_url = 'https://youtu.be/BRvzLVvjNdo?si=sR-F8MehQTC-_IW-'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
video_stream = yt.streams.get_lowest_resolution()

# Download the video
video_stream.download('D:\download')
