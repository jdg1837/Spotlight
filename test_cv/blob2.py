import cv2
import numpy as np;

# Read image
im = cv2.imread("car8.jpg", cv2.IMREAD_GRAYSCALE)
# Set up the detector with default parameters.

params = cv2.SimpleBlobDetector_Params()
# Change thresholds
params.minThreshold = 0    # the graylevel of images
params.maxThreshold = 255

params.filterByColor = True
params.blobColor = 0

# Filter by Area
params.filterByArea = True
params.minArea = 1000

detector = cv2.SimpleBlobDetector(params)

# Detect blobs.
keypoints = detector.detect(im)

print keypoints
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
