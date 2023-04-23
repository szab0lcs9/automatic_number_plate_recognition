import sys
import subprocess
import cv2
from cap_from_youtube import cap_from_youtube
import imutils
import pytesseract

# Pytesseract path, change it to your own path! 
# Without this line, pytesseract will not work!
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def checkOS():
    return sys.platform

def installPackages(platform):
    match platform:
        case 'darwin':
            subprocess.check_call([sys.executable, "-m", "/bin/bash", "-c", "\"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""])
            subprocess.check_call([sys.executable, "-m", "brew", "install", "tesseract"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "imutils"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "cap_from_youtube"])
        case 'linux':
            subprocess.check_call([sys.executable, "-m", "sudo", "apt", "install", "tesseract-ocr"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "imutils"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "cap_from_youtube"])
        case 'win32':
            subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "imutils"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pytesseract"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "cap_from_youtube"])
        case _:
            print('Please install the required packages manually!')

# Checking the OS and installing the required packages
platform = checkOS()
installPackages(platform)

# Checking if the given url and quality are correct
try:
    try:
        if len(sys.argv) > 1:
            url = sys.argv[1]
            quality = sys.argv[2]
            #url = 'https://www.youtube.com/watch?v=KZxtgEkGCqg'
            capture = cap_from_youtube(str(url), str(quality))
        else:
            print('Please enter YouTube URL and video quality')
    except:
        print('Incorrect URL name or invalid video quality')

    while True:
        if sys.argv[1] == None or sys.argv[2] == None:
            break
        # Checking if the video is opened
        try:
            check, frame = capture.read()
        except:
            print('Could not open the URL')
            break
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # apply blur for every frame
        #gaussianBlurredImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
        bFilteredGrayImage = cv2.bilateralFilter(grayImage, 21, 27, 27)

        #cv2.imshow('gauss', gaussianBlurredImage)
        #cv2.imshow('bilateral', bFilteredGrayImage)

        # convert the blurred image to a binary image
        #treshedImage = cv2.threshold(gaussianBlurredImage, 50, 200, cv2.THRESH_BINARY)[1]
        #cv2.imshow('treshed', treshedImage)

        # edge detection
        #laplacianFilteredImage = cv2.Laplacian(bFilteredGrayImage, cv2.CV_8U)
        edgedImage = cv2.Canny(bFilteredGrayImage, 40, 200)
        #cv2.imshow('edged', edgedImage)

        # find contours
        contours = cv2.findContours(edgedImage.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        # sort the top 10 contours
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

        # iterate through the contours
        for c in contours:
            approx = cv2.approxPolyDP(c, 10, True)
            # if the contour has 4 vertices, it is a rectangle
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(c)
                ratio = w / h
                # if the ratio is between 1 and 5, it is a license plate
                if ratio > 1 and ratio < 5:
                    plate = frame[y:y+h, x:x+w]
                    grayedPlate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
                    #cv2.imshow('plate', grayedPlate)

                    text = pytesseract.image_to_string(grayedPlate, lang='eng', config=r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 9 --oem 3')
                        #text = reader.readtext(plate)
                    if len(text) < 4:
                        break
                    # draw the rectangle and the text in the frames
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
                    cv2.putText(frame, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                    print("Detected licence plate: ", text)
        cv2.imshow('licence plate detection', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
except:
    print('Something went wrong when opening the URL')
finally:
    try:
        capture.release()
        cv2.destroyAllWindows()
    except:
        pass
