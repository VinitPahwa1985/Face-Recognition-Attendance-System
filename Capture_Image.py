import csv
import cv2
import os
import logging

# Configure logging
logging.basicConfig(filename='capture_image.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# counting the numbers
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# Take image function
def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if(is_number(Id) and name.isalpha()):
        logging.info(f"Starting image capture for ID: {Id}, Name: {name}")
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                # incrementing sample number
                sampleNum += 1
                # saving the captured face in the dataset folder TrainingImage
                img_path = f"TrainingImage{name}.{Id}.{sampleNum}.jpg"
                cv2.imwrite(img_path, gray[y:y+h, x:x+w])
                logging.info(f"Captured image {img_path}")
                # display the frame
                cv2.imshow('frame', img)
            # wait for 100 milliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                logging.info("Image capture interrupted by user")
                break
            # break if the sample number is more than 100
            elif sampleNum > 100:
                logging.info("Captured 100 images, stopping capture")
                break
        cam.release()
        cv2.destroyAllWindows()
        res = f"Images Saved for ID : {Id} Name : {name}"
        logging.info(res)
        
        header = ["Id", "Name"]
        row = [Id, name]
        
        if os.path.isfile("StudentDetails/StudentDetails.csv"):
            with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            logging.info(f"Appended details to StudentDetails.csv for ID: {Id}, Name: {name}")
        else:
            with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(header)
                writer.writerow(row)
            logging.info(f"Created StudentDetails.csv and added details for ID: {Id}, Name: {name}")
    else:
        if is_number(Id):
            print("Enter Alphabetical Name")
            logging.warning("Invalid input: Non-alphabetical name entered")
        if name.isalpha():
            print("Enter Numeric ID")
            logging.warning("Invalid input: Non-numeric ID entered")