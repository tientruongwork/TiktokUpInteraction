import time
from pytesseract import Output, pytesseract
import win32gui, win32ui
from init_app import parent_app, app_rect
from PIL import Image
from ctypes import windll


def capture_handler():
    hwndDC = win32gui.GetWindowDC(parent_app)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    # Create a bitmap object
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, app_rect[2], app_rect[3])

    # Select the bitmap object into the device context
    saveDC.SelectObject(saveBitMap)

    # Copy the window's pixels into the device context
    result = windll.user32.PrintWindow(parent_app, saveDC.GetSafeHdc(), 0)

    # Convert the device context to a PIL image
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        "RGB", (bmpinfo["bmWidth"], bmpinfo["bmHeight"]), bmpstr, "raw", "BGRX", 0, 1
    )

    # Save the image to a file
    im.save("screenshot.png")


def capture():
    for i in range(2):
        capture_handler()
        time.sleep(0.2)

    return pytesseract.image_to_data("screenshot.png", output_type=Output.DICT)

capture()