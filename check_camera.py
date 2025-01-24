import cv2
import logging

# Configure logging
logging.basicConfig(filename='check_camera.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def camera():
    logging.info("Starting camera check...")
    
    try:
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        if face_cascade.empty():
            logging.error("Failed to load haarcascade_frontalface_default.xml")
            return
        logging.info("Loaded haarcascade_frontalface_default.xml")

        # To capture video from webcam.
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            logging.error("Failed to open webcam")
            return

        logging.info("Webcam opened successfully")

        while True:
            # Read the frame
            ret, img = cap.read()
            if not ret:
                logging.error("Failed to read frame from webcam")
                break

            # Log the type and shape of img
            logging.info(f"Image type: {type(img)}, Image shape: {img.shape}")

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            logging.info(f"Detected {len(faces)} faces")

            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)

            # Display
            cv2.imshow('Webcam Check', img)

            # Stop if escape key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                logging.info("Escape key pressed, exiting...")
                break

        # Release the VideoCapture object
        cap.release()
        cv2.destroyAllWindows()
        logging.info("Released webcam and destroyed all windows")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise