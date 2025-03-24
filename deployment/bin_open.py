import pigpio
import time

SERVO_1_PIN = 18  # First Servo on GPIO 18
SERVO_2_PIN = 19  # Second Servo on GPIO 19

pi = pigpio.pi()

def set_angle_smooth(servo_pin, start_angle, target_angle, step_delay=0.02, step_size=1):
    """Move the servo gradually from start_angle to target_angle."""
    if start_angle < target_angle:
        step = step_size
    else:
        step = -step_size

    for angle in range(start_angle, target_angle + step, step):
        pulse_width = int(500 + (angle / 180.0) * 2000)
        pi.set_servo_pulsewidth(servo_pin, pulse_width)
        time.sleep(step_delay)

def degrade_action():
    print("Degrade detected: Opening Servo 1 for 8 seconds...")
    set_angle_smooth(SERVO_1_PIN, 120, 45)
    time.sleep(1)
    print("Closing Servo 1...")
    set_angle_smooth(SERVO_1_PIN, 45, 120)

def non_degrade_action():
    print("Non-Degrade detected: Opening Servo 2 for 8 seconds...")
    set_angle_smooth(SERVO_2_PIN, 120, 45)
    time.sleep(1)
    print("Closing Servo 2...")
    set_angle_smooth(SERVO_2_PIN, 45, 120)

def bin_open(predicted_label):
    if predicted_label=="degrade":
        degrade_action()
    else:
        non_degrade_action()
    # pi.stop()

# bin_open("degrade")
if __name__=="__main__":
    bin_open("degrade")
