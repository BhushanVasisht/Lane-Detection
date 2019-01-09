import cv2
import numpy as np

def mask_region(image):
    triangle = np.array([[[500, 740],[600, 280],[1400,740]]])
    mask = np.zeros_like(image)

    mask = cv2.fillPoly(mask, triangle, (255,255,255))

    mask_region = np.bitwise_and(image, mask)

    return mask_region


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('road.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  if ret == True:

      lane_reg = mask_region(frame)

      # Display the resulting frame
      cv2.imshow('Frame',lane_reg)

      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
