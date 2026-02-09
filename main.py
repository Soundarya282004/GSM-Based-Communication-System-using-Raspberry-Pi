import RPi.GPIO as GPIO
import serial
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

gsm = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)# AMA0 for using GPIO pins or if ur using USB to Serial adapter use /dev/ttyUSB0

time.sleep(2)

def send_command(command, wait=1):
    gsm.write((command + "\r").encode())
    time.sleep(wait)
    response = gsm.read(gsm.in_waiting).decode(errors='ignore')
    print("Response:", response)
    return response

def send_sms(phone_number, message):
    print("Sending SMS...")
    send_command("AT")
    send_command("AT+CMGF=1")  # Set SMS mode to text
    send_command(f'AT+CMGS="{phone_number}"')
    time.sleep(1)
    gsm.write(message.encode() + b"\x1A")  # Ctrl+Z to send
    time.sleep(3)
    print("SMS Sent!")

def make_call(phone_number):
    print("Calling...")
    send_command(f"ATD{phone_number};")  # Dial number
    time.sleep(10)  # Call duration
    send_command("ATH")  # Hang up
    print("Call Ended")

try:
    send_sms("+911234567890", "Hello! This message is from Raspberry Pi GSM module.")
    time.sleep(5)
    make_call("+911234567890")

except KeyboardInterrupt:
    print("Stopped by user")

gsm.close()
