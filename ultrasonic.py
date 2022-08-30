import RPi.GPIO as GPIO
import time
 
#set GPIO Pin
GPIO_TRIGGER1 = 17
GPIO_ECHO1 = 27
GPIO_TRIGGER2 = 20
GPIO_ECHO2 = 21
GPIO_TRIGGER3 = 5
GPIO_ECHO3 = 6

# ini merupakan setup sensor, jadi dibikin fungsi saja
#set GPIO direction (IN / OUT)
def init_ultrasonic():
  GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
  GPIO.setup(GPIO_ECHO1, GPIO.IN)
  GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
  GPIO.setup(GPIO_ECHO2, GPIO.IN)
  GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
  GPIO.setup(GPIO_ECHO3, GPIO.IN)
 
def distanceDepan():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
    GPIO.setwarnings(False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distancedepan = (TimeElapsed * 34300) / 2
    depan = (1E-06*distancedepan*distancedepan) + (1.0055*distancedepan) + 0.0012

    return depan

def distanceKanan():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
    GPIO.setwarnings(False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distancekanan = (TimeElapsed * 34300) / 2
    kanan = (1E-06*distancekanan*distancekanan) + (1.0055*distancekanan) + 0.0012
 
    return kanan

def distanceKiri():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER3, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER3, False)
    GPIO.setwarnings(False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO3) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO3) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distancekiri = (TimeElapsed * 34300) / 2
    kiri = (1E-06*distancekiri*distancekiri) + (1.0055*distancekiri) + 0.0012
 
    return kiri

def get_ultrasonic_distance():
  kanan = distanceKanan()
  kiri = distanceKiri()
  depan = distanceDepan()
  return kiri, depan, kanan

# #void setup()
# init_ultrasonic()

# #void loop
# kiri, depan, kanan = get_ultrasonic_distance()
