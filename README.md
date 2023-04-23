# Automatic Number Plate Recognition

The program plays a video from youtube and recognizing number plates from cars.

### Requirements:
1. To use this program it will be neccessary to have Tesseract-OCR on your computer.
   * For Windows it can be downloaded from [here](https://digi.bib.uni-mannheim.de/tesseract/?ref=nanonets.com)
	Install this exe in "C:\Program Files(x86)\Tesseract-OCR.
   * For Mac or Linux installation instruction can be read [here](https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md)

1.a. Pre-installed libraries:
   * Tesseract-OCR: Tesseract is an optical character recognition engine for various operating systems. It is free software, released under the Apache License. Originally developed by Hewlett-Packard as proprietary software in the 1980s, it was released as open source in 2005 and development has been sponsored by Google since 2006.
	
	Installation:
	```
	pip install pytesseract
	```

   * OpenCV: OpenCV is an open source computer vision library. The library has more than 2500 optimized algorithms. These algorithms are often used to search and recognize faces, identify objects, recognize scenery and generate markers to overlay images using augmented reality, etc.

      Installation:
      ```
      pip install opencv-python
      ```
      
    * Cap-From-Youtube: Cap-From-Youtube is to get an OpenCV video capture from an YouTube video URL

      Installation:
      ```
      pip install cap-from-youtube
      ```
      
    * Imutils: Imutils is a python library with a series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.

      Installation:
      ```
      pip install imutils
      ```
