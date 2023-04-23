import sys
import cv2
from cap_from_youtube import cap_from_youtube
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# checking the url and quality correction
try:
    try:
        if len(sys.argv) > 1:
            url = sys.argv[1]
            quality = sys.argv[2]
            #url = 'https://www.youtube.com/watch?v=KZxtgEkGCqg'
            capture = cap_from_youtube(str(url), str(quality))
        else:
            print('Please enter the URL and the quality of the video')
    except:
        print('Incorrect URL name or invalid video quality')

    while True:
        
        # checking if the video is opened
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

        contours = cv2.findContours(edgedImage.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

        
        for c in contours:
            approx = cv2.approxPolyDP(c, 10, True)
            
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(c)
                ratio = w / h
                if ratio > 1 and ratio < 5:
                    plate = frame[y:y+h, x:x+w]
                    grayedPlate = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
                    #cv2.imshow('plate', grayedPlate)

                    text = pytesseract.image_to_string(grayedPlate, lang='eng', config=r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 9 --oem 3')
                        #text = reader.readtext(plate)
                    if len(text) < 4:
                        break
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
        print('Video cannot be played')
