import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize
import logging

# Configure logging
logging.basicConfig(filename='attendance_system.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# creating the title bar function
def title_bar():
    os.system('cls')  # for windows
    # title of the program
    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")

# creating the user main menu function
def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Auto Mail")
    print("[6] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))
            logging.info(f"User selected option {choice}")

            if choice == 1:
                checkCamera()
                break
            elif choice == 2:
                CaptureFaces()
                break
            elif choice == 3:
                Trainimages()
                break
            elif choice == 4:
                RecognizeFaces()
                break
            elif choice == 5:
                os.system("py automail.py")
                logging.info("Executed automail.py")
                break
                mainMenu()
            elif choice == 6:
                print("Thank You")
                logging.info("User exited the program")
                break
            else:
                print("Invalid Choice. Enter 1-6")
                logging.warning("User entered an invalid choice")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-6\n Try Again")
            logging.error("ValueError: User entered a non-integer value")

# calling the camera test function from check camera.py file
def checkCamera():
    logging.info("Checking camera...")
    check_camera.camera()
    key = input("Enter any key to return main menu")
    mainMenu()

# calling the take image function form capture image.py file
def CaptureFaces():
    logging.info("Capturing faces...")
    Capture_Image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()

# calling the train images from train_images.py file
def Trainimages():
    logging.info("Training images...")
    Train_Image.TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()

# calling the recognize_attendance from recognize.py file
def RecognizeFaces():
    logging.info("Recognizing faces and marking attendance...")
    Recognize.recognize_attendence()
    key = input("Enter any key to return main menu")
    mainMenu()

# main driver 
if __name__ == "__main__":
    logging.info("Starting Face Recognition Attendance System...")
    mainMenu()