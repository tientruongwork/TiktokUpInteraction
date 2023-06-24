@ECHO OFF


IF NOT EXIST python_installation.exe curl https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe --output python_installation.exe


IF NOT EXIST tesseract-ocr_installation.exe curl https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.0.20221222.exe --output tesseract-ocr_installation.exe

ECHO All application are downloaded
pause