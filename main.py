import RPi.GPIO as GPIO
import time
import atexit

atexit.register(GPIO.cleanup)

from ultrasonic import init_ultrasonic, get_ultrasonic_distance
from gps import *
from speaker import play_speaker
from ubidots import build_payload, post_request


def setup():
    GPIO.setmode(GPIO.BCM)
    init_ultrasonic()
    init_gps()
  
  
def loop():
    kiri, depan, kanan = get_ultrasonic_distance()
    latitude, longitude = get_gps()
    
    if depan > 150:  # jika ke depan
        print("ke depan")
        play_speaker(speaker=3)
        decision = "ke depan"
      
    else:
        if kiri > kanan:
            print("ke kiri")
            play_speaker(speaker=1)
            decision = "ke kiri"
          
        elif kanan > kiri:
            print("ke kanan")
            play_speaker(speaker=2)
            decision = "ke kanan"
          
        elif kanan < 50 and kiri < 50:
            print("ke mundur")
            play_speaker(speaker=4)
            decision = "ke mundur"
      
    #.......
    # more logic here
    #.......
    
    payload = build_payload(depan, kanan, kiri, latitude, longitude, decision)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
  
  
setup()
while True:
    loop()
