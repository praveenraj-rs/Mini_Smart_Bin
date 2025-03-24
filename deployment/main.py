from gpiozero import MotionSensor
from image_capture import capture_image
from image_process import process_captured_image
from bin_open import bin_open
from fill_measure import fill_measure 
from post_sensor_data import post_sensor_data

# GPIO pin for the IR sensor
IR_SENSOR_PIN = 26

# Initialize the motion sensor
motion_sensor = MotionSensor(IR_SENSOR_PIN)

def on_motion():

    print(" - Motion detected")

    # Call the image capture function
    capture_image()

     # Call the image processing function
    predicted_label = process_captured_image("captured_image.jpg")

    print(predicted_label)

    # Opening bin
    bin_open(predicted_label)
    
    # Fill measure
    res = fill_measure(predicted_label)
    print(res)

    # Post Sensor Data
    post_sensor_data('yuvan','chennai',res[0],res[1])


    # Display a final message
    print(" - Classification Completed Successfully\n\n")

# Attach the on_motion function to the motion sensor
motion_sensor.when_motion = on_motion

try:
    print("Waiting for motion...")
    # Keep the script running
    while True:
        pass

except KeyboardInterrupt:
    print("Script terminated by user.")

