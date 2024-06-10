import RPi.GPIO as GPIO
from time import sleep

# Motor 1
in1_motor1 = 23
in2_motor1 = 24
en_motor1 = 25

# Motor 2
in1_motor2 = 17  # Change GPIO pin numbers according to your setup
in2_motor2 = 27  # Change GPIO pin numbers according to your setup
en_motor2 = 22  # Change GPIO pin numbers according to your setup

temp1_motor1 = 1
temp1_motor2 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1_motor1, GPIO.OUT)
GPIO.setup(in2_motor1, GPIO.OUT)
GPIO.setup(en_motor1, GPIO.OUT)

GPIO.setup(in1_motor2, GPIO.OUT)
GPIO.setup(in2_motor2, GPIO.OUT)
GPIO.setup(en_motor2, GPIO.OUT)

GPIO.output(in1_motor1, GPIO.LOW)
GPIO.output(in2_motor1, GPIO.LOW)
p_motor1 = GPIO.PWM(en_motor1, 1000)

GPIO.output(in1_motor2, GPIO.LOW)
GPIO.output(in2_motor2, GPIO.LOW)
p_motor2 = GPIO.PWM(en_motor2, 1000)

GPIO.setwarnings(False)  # Ignore GPIO warnings

p_motor1.start(25)
p_motor2.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("m1 and m2 to select motor 1 and motor 2 respectively")
print("a-run s-stop f-forward b-backward l-left r-right l-low m-medium h-high e-exit")
print("\n")

while True:

    x = input("Enter your choice: ")  # Use input() instead of raw_input() for Python 3.x compatibility

    if x == 'm1':
        print("Selected Motor 1")
        selected_motor = 1

    elif x == 'm2':
        print("Selected Motor 2")
        selected_motor = 2

    elif x == 'a':
        print("run")
        if selected_motor == 1:
            if temp1_motor1 == 1:
                GPIO.output(in1_motor1, GPIO.HIGH)
                GPIO.output(in2_motor1, GPIO.LOW)
                print("forward")
                x = 'z'
            else:
                GPIO.output(in1_motor1, GPIO.LOW)
                GPIO.output(in2_motor1, GPIO.HIGH)
                print("backward")
                x = 'z'
        elif selected_motor == 2:
            if temp1_motor2 == 1:
                GPIO.output(in1_motor2, GPIO.HIGH)
                GPIO.output(in2_motor2, GPIO.LOW)
                print("forward")
                x = 'z'
            else:
                GPIO.output(in1_motor2, GPIO.LOW)
                GPIO.output(in2_motor2, GPIO.HIGH)
                print("backward")
                x = 'z'

    elif x == 's':
        print("stop")
        if selected_motor == 1:
            GPIO.output(in1_motor1, GPIO.LOW)
            GPIO.output(in2_motor1, GPIO.LOW)
        elif selected_motor == 2:
            GPIO.output(in1_motor2, GPIO.LOW)
            GPIO.output(in2_motor2, GPIO.LOW)
        x = 'z'

    elif x == 'f':
        print("forward")
        if selected_motor == 1:
            GPIO.output(in1_motor1, GPIO.HIGH)
            GPIO.output(in2_motor1, GPIO.LOW)
            temp1_motor1 = 1
        elif selected_motor == 2:
            GPIO.output(in1_motor2, GPIO.HIGH)
            GPIO.output(in2_motor2, GPIO.LOW)
            temp1_motor2 = 1
        x = 'z'

    elif x == 'b':
        print("backward")
        if selected_motor == 1:
            GPIO.output(in1_motor1, GPIO.LOW)
            GPIO.output(in2_motor1, GPIO.HIGH)
            temp1_motor1 = 0
        elif selected_motor == 2:
            GPIO.output(in1_motor2, GPIO.LOW)
            GPIO.output(in2_motor2, GPIO.HIGH)
            temp1_motor2 = 0
        x = 'z'

    elif x == 'l':
        print("left")
        if selected_motor == 1:
            GPIO.output(in1_motor1, GPIO.LOW)
            GPIO.output(in2_motor1, GPIO.HIGH)  # Adjust according to your motor setup for left movement
            temp1_motor1 = 0
        elif selected_motor == 2:
            GPIO.output(in1_motor2, GPIO.HIGH)
            GPIO.output(in2_motor2, GPIO.LOW)  # Adjust according to your motor setup for left movement
            temp1_motor2 = 1
        x = 'z'

    elif x == 'r':
        print("right")
        if selected_motor == 1:
            GPIO.output(in1_motor1, GPIO.HIGH)  # Adjust according to your motor setup for right movement
            GPIO.output(in2_motor1, GPIO.LOW)
            temp1_motor1 = 1
        elif selected_motor == 2:
            GPIO.output(in1_motor2, GPIO.LOW)  # Adjust according to your motor setup for right movement
            GPIO.output(in2_motor2, GPIO.HIGH)
            temp1_motor2 = 0
        x = 'z'

    elif x == 'k':
        print("low")
        if selected_motor == 1:
            p_motor1.ChangeDutyCycle(40)
        elif selected_motor == 2:
            p_motor2.ChangeDutyCycle(40)
        x = 'z'

    elif x == 'm':
        print("medium")
        if selected_motor == 1:
            p_motor1.ChangeDutyCycle(70)
        elif selected_motor == 2:
            p_motor2.ChangeDutyCycle(70)
        x = 'z'

    elif x == 'h':
        print("high")
        if selected_motor == 1:
            p_motor1.ChangeDutyCycle(100)
        elif selected_motor == 2:
            p_motor2.ChangeDutyCycle(100)
        x = 'z'

    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
