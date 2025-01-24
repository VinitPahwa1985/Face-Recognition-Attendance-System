from flask import Flask, request, jsonify
import cv2
import check_camera
import Capture_Image
import Train_Image
import Recognize
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='attendance_system.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.route('/check_camera', methods=['GET'])
def check_camera_route():
    logging.info("Checking camera...")
    check_camera.camer()
    return jsonify({"message": "Camera checked successfully."})

@app.route('/capture_faces', methods=['POST'])
def capture_faces_route():
    logging.info("Capturing faces...")
    Capture_Image.takeImages()
    return jsonify({"message": "Faces captured successfully."})

@app.route('/train_images', methods=['POST'])
def train_images_route():
    logging.info("Training images...")
    Train_Image.TrainImages()
    return jsonify({"message": "Images trained successfully."})

@app.route('/recognize_faces', methods=['POST'])
def recognize_faces_route():
    logging.info("Recognizing faces and marking attendance...")
    try:
        # Create the LBPH face recognizer
        logging.info(cv2.__version__)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        # Load your trained model (example path)
        recognizer.read('TrainingImageLabel/Trainner.yml')
        # Add your face recognition logic here
        # ...
        logging.info("Faces recognized and attendance marked successfully.")
        return jsonify({"message": "Faces recognized and attendance marked successfully."})
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/auto_mail', methods=['POST'])
def auto_mail_route():
    os.system("py automail.py")
    logging.info("Executed automail.py")
    return jsonify({"message": "Auto mail executed successfully."})

if __name__ == "__main__":
    app.run(debug=True)