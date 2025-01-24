import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize
import logging
import gradio as gr

# Configure logging
logging.basicConfig(filename='attendance_system.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def checkCamera():
    """Function to check the camera."""
    logging.info("Checking camera...")
    check_camera.camer()
    return "Camera checked successfully."

def CaptureFaces():
    """Function to capture faces."""
    logging.info("Capturing faces...")
    Capture_Image.takeImages()
    return "Faces captured successfully."

def Trainimages():
    """Function to train images."""
    logging.info("Training images...")
    Train_Image.TrainImages()
    return "Images trained successfully."

def RecognizeFaces():
    """Function to recognize faces and mark attendance."""
    logging.info("Recognizing faces and marking attendance...")
    Recognize.recognize_attendence()
    return "Faces recognized and attendance marked successfully."

def AutoMail():
    """Function to execute auto mail script."""
    os.system("py automail.py")
    logging.info("Executed automail.py")
    return "Auto mail executed successfully."

# Gradio interface
iface = gr.Interface(
    fn=lambda choice: {
        1: checkCamera,
        2: CaptureFaces,
        3: Trainimages,
        4: RecognizeFaces,
        5: AutoMail,
        6: lambda: "Thank You"
    }.get(choice, lambda: "Invalid Choice. Enter 1-6")(),
    inputs=gr.Dropdown(choices=[1, 2, 3, 4, 5, 6], label="Select an option"),
    outputs="text",
    title="Face Recognition Attendance System",
    description="Select an option from the dropdown menu to perform the corresponding action."
)

if __name__ == "__main__":
    logging.info("Starting Face Recognition Attendance System...")
    iface.launch()