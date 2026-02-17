# GSM-Based-Communication-System-using-Raspberry-Pi
It demonstrates how to interface a GSM module with a Raspberry Pi to send SMS messages and make phone calls using Python. It uses AT commands over serial communication to control the GSM module.

🔌 Hardware Required
- Raspberry Pi
- GSM Module (SIM800 / SIM900 etc.)
- SIM card (with SMS & calling enabled)
- External power supply for GSM module
- Jumper wires

⚠️ GSM modules must not be powered directly from Raspberry Pi 5V.

🔧 Connections (Basic)

GSM Module	Raspberry Pi
TX	RX (GPIO 15)
RX	TX (GPIO 14)
GND	GND
VCC	External power
<img width="310" height="121" alt="image" src="https://github.com/user-attachments/assets/fb92b385-8c03-477c-87d5-0faefe0a5fd3" />



💻 Software Requirements

Install serial library:

    pip install pyserial

▶ How to Run the Code

1️⃣ Enable Serial Port on Raspberry Pi

Run:

    sudo raspi-config
- Interface Options → Serial
- Disable login shell over serial
- Enable serial hardware
- Reboot

2️⃣ Save the Code

Save file as:

    main.py
3️⃣ Update Phone Number

Replace with your number:

    send_sms("+911234567890", "Hello! This message is from Raspberry Pi GSM module.")
    make_call("+911234567890")

4️⃣ Run the Script

    python3 main.py

⚙️ How the Code Works

🔹 Serial Communication

    gsm = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
Opens serial connection to GSM module.

🔹 Sending AT Commands

    send_command("AT")
Checks communication with GSM module.

🔹 Sending SMS
AT+CMGF=1      # Text mode
AT+CMGS="number"
Ctrl + Z       # Send

🔹 Making a Call
ATD<number>;
ATH

📤 Example Output
Sending SMS...
Response: OK
SMS Sent!
Calling...
Call Ended

🛑 Stop the Program

Press:

    CTRL + C
