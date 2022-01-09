#Get YouTube Video Details Using Python
#Importing Required Modules
import pafy

#Taking The URL Of Video From User
url = input("Enter the URL Of your Video Here: ")

# Getting the Video
video = pafy.new(url)

# Getting Video Title 
print(video.title)

# Getting Video Rating
print(video.rating)

# Getting Video Views Count
print(video.viewcount)

# Getting Aurthor & Video Length
print(video.author,video.length)

# Getting Video Duration, Likes , Dislikes & Description
print(video.description,video.likes,video.dislikes,video.description)
