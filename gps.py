import serial
from time import sleep
from struct import unpack

ser = None

def init_gps():
  global ser
  ser = serial.Serial('/dev/ttyUSB0', 9600)  # open serial port

def get_gps():
  global ser
  dataRaw = ser.read(8)  #6 ===> 2 x 4 of short data types (4 Bytes)
  latitude, longitude = unpack("ff", dataRaw)  # 2 float data
  print(f"lat: {latitude}")
  print(f"data2: {longitude}")
  return latitude, longitude
