'''Testing openCV line detection'''
# Found on https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv

import cv2
import numpy as np


def detect_lines(filename):

    # Get gray image
    imgInput = filename
    imgOutput = '../images/' + filename.replace('.png', '') + '_lines.png'
    img = cv2.imread(imgInput)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Process gray image with GaussianBlur
    kernal_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernal_size, kernal_size), 0)

    # Process edge detection using Canny
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    # Get lines with HoughLinesP
    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 50  # minimum number of pixels making up a line
    max_line_gap = 150  # maximum gap in pixels between connectable line segments
    line_image = np.copy(img)   # creating a blank to draw lines on
    line_overlay = np.copy(img)

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)

    # Draw the lines on the  image
    lines_edges = cv2.addWeighted(img, 0.8, line_overlay, 1, 0)

    cv2.imwrite(imgOutput, line_image)

    return imgOutput
