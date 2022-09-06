import serial
from time import sleep
from struct import unpack

ser = None

def init_gps():
  global ser
  # ser = serial.Serial('/dev/ttyUSB0', 9600)  # open serial port
  ser = serial.Serial('/dev/ttyUSB0', 9600, timeout= 1)  # open serial port
def get_gps():
  global ser
  dataRaw = ser.read(8)  #6 ===> 2 x 4 of short data types (4 Bytes)
  if len(dataRaw) >= 8:
    latitude, longitude = unpack("ff", dataRaw)  # 2 float data
    # print("data gps")
  else:
    latitude, longitude = -7.811427550260671, 112.02549373888884
    # print("data dummy")
  print(f"lat: {latitude}")
  print(f"long: {longitude}")
  return latitude, longitude
