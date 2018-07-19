import cv2
import os

image_folder = "images"
video_name = "demo.avi"

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

frame = cv2.imread(os.path.join(image_folder, images[0]))
cv2.imshow('video', frame)
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
video = cv2.VideoWriter(video_name, fourcc, 20.0, (width, height))

for image in images:
    frame = cv2.imread(os.path.join(image_folder, image))
    video.write(frame)
    
video.release()
cv2.destroyAllWindows()

print("The video is made.")
