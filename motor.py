import RPi.GPIO as GPIO
import time

# Initialize GPIO and PWM
GPIO.setmode(GPIO.BCM)

# Define pins for Motor A
IN1 = 22  # GPIO pin for IN1
IN2 = 5   # GPIO pin for IN2
ENA = 18   # PWM pin for Motor A speed control

# Define pins for Motor B
IN3 = 6   # GPIO pin for IN3
IN4 = 26  # GPIO pin for IN4
ENB = 19  # PWM pin for Motor B speed control

# Set up pins as outputs
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# Set up PWM with a frequency of 1000 Hz
pwm_ena = GPIO.PWM(ENA, 1000)  # Motor A
pwm_enb = GPIO.PWM(ENB, 1000)  # Motor B

# Start PWM with 0% duty cycle (motors off initially)
pwm_ena.start(0)
pwm_enb.start(0)

# Define speeds
fast_speed = 100  # 100% duty cycle for fast speed
slow_speed = 25   # 25% duty cycle for slow speed

try:
    # 1. Run motors fast
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm_ena.ChangeDutyCycle(fast_speed)  # Fast speed for Motor A

    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_enb.ChangeDutyCycle(fast_speed)  # Fast speed for Motor B

    time.sleep(2)  # Run motors fast for 5 seconds

    # 2. Slow down motors
    pwm_ena.ChangeDutyCycle(slow_speed)  # Slow speed for Motor A
    pwm_enb.ChangeDutyCycle(slow_speed)  # Slow speed for Motor B

    time.sleep(2)  # Run motors slowly for 5 seconds

    # 3. Reverse motors
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_ena.ChangeDutyCycle(fast_speed)  # Fast speed in reverse for Motor A

    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_enb.ChangeDutyCycle(90)  # Fast speed in reverse for Motor B

    time.sleep(2)  # Run motors in reverse for 5 seconds

 # 2. Slow down motors
    pwm_ena.ChangeDutyCycle(5)  # Slow speed for Motor A
    pwm_enb.ChangeDutyCycle(5)  # Slow speed for Motor B

    time.sleep(2)  # Run motors slowly for 5 seconds

finally:
    # 4. Stop motors and clean up
    pwm_ena.stop()
    pwm_enb.stop()
    GPIO.cleanup()
