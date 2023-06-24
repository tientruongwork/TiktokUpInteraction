from capture import capture
from print_format import print_format
import cv2


def execute_check(path, isVideo):
    # Load the two images
    image1 = cv2.imread("screenshot.png")
    image2 = cv2.imread(path)

    # Convert image1 to grayscale
    # Perform template matching
    result = cv2.matchTemplate(image2, image1, cv2.TM_CCOEFF_NORMED)

    # Get the best match location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    match_percent = str(round(max_val * 100)) + "%"

    print_format("Image match rate = " + match_percent)

    # Check if the best match is above a certain threshold
    thresh_hold = 0.8
    if isVideo == True:
        thresh_hold = 0.7

    if max_val >= thresh_hold:
        return True
    else:
        return False


def check_is_video():
    print_format("Checking is video")
    capture()
    return execute_check("heart.jpg", True)


def check_is_home():
    print_format("Checking is home page")
    capture()
    return execute_check("home.jpg", False)
