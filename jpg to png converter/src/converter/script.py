# Importing Required Modules
from PIL import Image
# Define the Path Of Image where img is saved
img = Image.open(r'C:\Users\tanma\Desktop\panda.jpg')
img.save(r'C:\Users\tanma\Desktop\new_panda.png')

# Giving Message to the User 
if img.save(r'C:\Users\tanma\Desktop\new_panda.png') == img.save(r'C:\Users\tanma\Desktop\new_panda.png'):
    print('Image Converted Sucessfully')
# If Image Could Not Be Processed The Show the Message
else:
    print('Image Could not Be Coverted \n Try Again')