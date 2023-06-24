@echo off
title Uninstall packages

echo Unstalling neccessary packages
python -m pip uninstall opencv-python --y
python -m pip uninstall Pillow --y
python -m pip uninstall pywin32 --y
python -m pip uninstall pytesseract --y
python -m pip uninstall pynput --y
python -m pip uninstall ctypes-callable --y

color 02
echo Uninstall packages done, click anything exit..
pause