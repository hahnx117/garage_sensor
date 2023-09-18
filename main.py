import subprocess
import time
import board
import adafruit_hcsr04
import paho.mqtt.client as mqtt
import os

while True:
    subprocess.run(["raspistill", "-o", "image.jpg"])
    subprocess.run(["convert", "-pointsize", "36", "-fill", "white", "-draw", "\"text 225,50 '`date`'\"", "image.jpg", "image2.jpg"])
    os.remove("image.jpg")
    os.remove("image2.jpg")