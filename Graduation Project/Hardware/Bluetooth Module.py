import RPi.GPIO as GPIO
import serial
import time

class MotorControlApp:
    def init(self):
        self.setup_gpio()
        self.setup_bluetooth()
        self.selected_motor = None

    def setup_gpio(self):
        try:
            # Define GPIO pins for motor control using BCM numbers based on physical pin numbers
            self.in1_motor1 = 23  # Physical pin 18
            self.in2_motor1 = 24  # Physical pin 16
            self.en_motor1 = 25   # Physical pin 22

            self.in1_motor2 = 17  # Physical pin 11
            self.in2_motor2 = 27  # Physical pin 13
            self.en_motor2 = 22   # Physical pin 15

            # Initialize motor control pins
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup([self.in1_motor1, self.in2_motor1, self.en_motor1,
                        self.in1_motor2, self.in2_motor2, self.en_motor2], GPIO.OUT)

            # Initialize PWM objects for motor speed control
            self.p_motor1 = GPIO.PWM(self.en_motor1, 1000)
            self.p_motor2 = GPIO.PWM(self.en_motor2, 1000)

            # Start PWM with default speed
            self.p_motor1.start(25)
            self.p_motor2.start(25)
        except Exception as e:
            print(f"Error setting up GPIO: {e}")

    def setup_bluetooth(self):
        try:
            # Initialize Bluetooth serial connection
            self.ser = serial.Serial('/dev/serial0', 9600, timeout=1)
            self.ser.flush()
        except Exception as e:
            print(f"Error setting up Bluetooth: {e}")

    def read_bluetooth(self):
        try:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').rstrip()
                self.process_bluetooth_command(line)
        except Exception as e:
            print(f"Error reading Bluetooth data: {e}")

    def process_bluetooth_command(self, command):
        if command == "motor1":
            self.select_motor1()
        elif command == "motor2":
            self.select_motor2()
        elif command == "both":
            self.select_both_motors()
        elif command == "up":
            self.move_up()
        elif command == "down":
            self.move_down()
        elif command == "left":
            self.move_left()
        elif command == "right":
            self.move_right()
        elif command == "forward":
            self.move_forward()
        elif command == "auto_left":
            self.move_auto_left()
        elif command == "auto_right":
            self.move_auto_right()
        elif command == "stop":
            self.stop_motor()
        elif command.startswith("speed:"):
            speed = int(command.split(":")[1])
            self.update_speed(speed)

    def select_motor1(self):
        self.selected_motor = 1

    def select_motor2(self):
        self.selected_motor = 2

    def select_both_motors(self):
        self.selected_motor = "both"

    def move_up(self):
        if self.selected_motor == 1 or self.selected_motor == "both":
            GPIO.output(self.in1_motor1, GPIO.HIGH)
            GPIO.output(self.in2_motor1, GPIO.LOW)
        if self.selected_motor == 2 or self.selected_motor == "both":
            GPIO.output(self.in1_motor2, GPIO.HIGH)
            GPIO.output(self.in2_motor2, GPIO.LOW)
        self.stop_after_delay()

    def move_down(self):
        if self.selected_motor == 1 or self.selected_motor == "both":
            GPIO.output(self.in1_motor1, GPIO.LOW)
            GPIO.output(self.in2_motor1, GPIO.HIGH)
        if self.selected_motor == 2 or self.selected_motor == "both":
            GPIO.output(self.in1_motor2, GPIO.LOW)
            GPIO.output(self.in2_motor2, GPIO.HIGH)
        self.stop_after_delay()
def move_left(self):
        if self.selected_motor == 1 or self.selected_motor == "both":
            GPIO.output(self.in1_motor1, GPIO.LOW)
            GPIO.output(self.in2_motor1, GPIO.HIGH)
        if self.selected_motor == 2 or self.selected_motor == "both":
            GPIO.output(self.in1_motor2, GPIO.HIGH)
            GPIO.output(self.in2_motor2, GPIO.LOW)
        self.stop_after_delay()

    def move_right(self):
        if self.selected_motor == 1 or self.selected_motor == "both":
            GPIO.output(self.in1_motor1, GPIO.HIGH)
            GPIO.output(self.in2_motor1, GPIO.LOW)
        if self.selected_motor == 2 or self.selected_motor == "both":
            GPIO.output(self.in1_motor2, GPIO.LOW)
            GPIO.output(self.in2_motor2, GPIO.HIGH)
        self.stop_after_delay()

    def move_forward(self):
        if self.selected_motor == 1 or self.selected_motor == "both":
            GPIO.output(self.in1_motor1, GPIO.HIGH)
            GPIO.output(self.in2_motor1, GPIO.LOW)
        if self.selected_motor == 2 or self.selected_motor == "both":
            GPIO.output(self.in1_motor2, GPIO.HIGH)
            GPIO.output(self.in2_motor2, GPIO.LOW)

    def move_auto_left(self):
        if self.selected_motor == 1 or self.selected_motor == "both":
            GPIO.output(self.in1_motor1, GPIO.LOW)
            GPIO.output(self.in2_motor1, GPIO.HIGH)
        if self.selected_motor == 2 or self.selected_motor == "both":
            GPIO.output(self.in1_motor2, GPIO.HIGH)
            GPIO.output(self.in2_motor2, GPIO.LOW)

    def move_auto_right(self):
        if self.selected_motor == 1 or self.selected_motor == "both":
            GPIO.output(self.in1_motor1, GPIO.HIGH)
            GPIO.output(self.in2_motor1, GPIO.LOW)
        if self.selected_motor == 2 or self.selected_motor == "both":
            GPIO.output(self.in1_motor2, GPIO.LOW)
            GPIO.output(self.in2_motor2, GPIO.HIGH)

    def stop_after_delay(self):
        # Stop motors after a short delay
        time.sleep(0.5)  # Adjust this delay as needed
        self.stop_motor()

    def update_speed(self, speed):
        duty_cycle = int(speed)
        self.p_motor1.ChangeDutyCycle(duty_cycle)
        self.p_motor2.ChangeDutyCycle(duty_cycle)

    def stop_motor(self):
        if self.selected_motor is not None:
            if self.selected_motor == 1 or self.selected_motor == "both":
                GPIO.output([self.in1_motor1, self.in2_motor1], GPIO.LOW)
            if self.selected_motor == 2 or self.selected_motor == "both":
                GPIO.output([self.in1_motor2, self.in2_motor2], GPIO.LOW)

    def cleanup_gpio(self):
        GPIO.cleanup()
        self.ser.close()

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    app = MotorControlApp()

    try:
        while True:
            app.read_bluetooth()
            time.sleep(0.1)  # Check for Bluetooth commands every 100 ms
    finally:
        app.cleanup_gpio()


if name == 'main':
    app.run(debug=True, host='0.0.0.0', port=8000)