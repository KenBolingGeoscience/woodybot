
# from oled.oled import start_oled
from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
# import Adafruit_GPIO.SPI as SPI
# import Adafruit_SSD1306
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
# import subprocess
import time

app = Flask(__name__, template_folder='Templates')
app.debug = True

m17=17
m22=22
m23=23
m24=24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m17, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.setup(m23, GPIO.OUT)
GPIO.setup(m24, GPIO.OUT)
GPIO.output(m17, 0)
GPIO.output(m22, 0)
GPIO.output(m23, 0)
GPIO.output(m24, 0)
print ("Done")

a=1
@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    GPIO.output(m17, 0)
    GPIO.output(m22, 1)
    GPIO.output(m23, 0)
    GPIO.output(m24, 1)
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   GPIO.output(m17, 1)
   GPIO.output(m22, 0)
   GPIO.output(m23, 1)
   GPIO.output(m24, 0)
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   GPIO.output(m17, 0)
   GPIO.output(m22, 1)
   GPIO.output(m23, 1)
   GPIO.output(m24, 0)
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   GPIO.output(m17, 1)
   GPIO.output(m22, 0)
   GPIO.output(m23, 0)
   GPIO.output(m24, 1)
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(m17, 0)
   GPIO.output(m22, 0)
   GPIO.output(m23, 0)
   GPIO.output(m24, 0)
   return  'true'


# Start OLED
# start_oled()


if __name__ == "__main__":
 print("Starting up Woody Bot, have a great time!")
 app.run(host='192.168.1.73',port=5010)


