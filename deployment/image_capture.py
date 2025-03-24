import cv2

def capture_image():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    try:
        # Capture a single frame
        ret, frame = cap.read()

        # Check if the frame is captured successfully
        if not ret:
            print("Error: Could not capture frame.")
            exit()

        # Save the captured frame as an image
        cv2.imwrite("captured_image.jpg", frame)

        # Display a message
        print(" - Image captured successfully")

    finally:
        # Release the webcam, even if an error occurs
        cap.release()

if __name__=="__main__":
    capture_image()
