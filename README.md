# Automatic Number Plate Recognition

Plays a video from youtube and recognizing number plates from cars.

## Requirements:
To use this program it will be neccessary to have the packages that written below, however the script will automatically installing these.


   * **Tesseract-OCR:** Tesseract is an optical character recognition engine for various operating systems. It is free software, released under the Apache License. Originally developed by Hewlett-Packard as proprietary software in the 1980s, it was released as open source in 2005 and development has been sponsored by Google since 2006.
   
     Installation:
     * **Windows:** it can be downloaded from [here](https://digi.bib.uni-mannheim.de/tesseract/?ref=nanonets.com)
     
       Install this exe in *C:\Program Files\Tesseract-OCR*
       
     * **macOS:** Installing the Tesseract OCR engine on macOS is quite simple if you use the [Homebrew](https://brew.sh) package manager.
     
       Use the link above to install Homebrew on your system if it is not already installed.
       
       From there, all you need to do is use the following command to install Tesseract:
       ```
       brew install tesseract
       ```
       
     * **Ubuntu:** Install with the following command:
       ```
       sudo apt install tesseract-ocr
       ```

   * **OpenCV:** OpenCV is an open source computer vision library. The library has more than 2500 optimized algorithms. These algorithms are often used to search and recognize faces, identify objects, recognize scenery and generate markers to overlay images using augmented reality, etc.

      Installation:
      ```
      pip install opencv-python
      ```
      
   * **Cap-From-Youtube:** Cap-From-Youtube is to get an OpenCV video capture from an YouTube video URL

      Installation:
      ```
      pip install cap-from-youtube
      ```
      
   * **Imutils:** Imutils is a python library with a series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3.

      Installation:
      ```
      pip install imutils
      ```

## Usage:

You can use this application from the CLI of your computer the following way:

  1. `cd` to that directory where you downloaded the *automatic_number_plate_recognition.py* file.
  2. The script will be expecting two arguments. The first will be the URL from youtube and the second is the quality of the video.
     
     To execute the script, you'd type `python` first. Then comes the filename (*automatic_number_plate_recognition.py*) and the arguments. Check the example below:
     
     ```
     python automatic_number_plate_recognition.py https://www.youtube.com/watch?v=KZxtgEkGCqg 720p50
     ```
     
If everything is correct, the program will be open the youtube video from the given url with the given quality, draws a rectangle around the detected licence plate and writes the recognized text to the terminal.


To quit from the video, press 'Q'.
