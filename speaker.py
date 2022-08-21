import vlc

# url media
kiri = '/home/pi/GLASSTIC/kiri.mp3'
kanan = '/home/pi/GLASSTIC/kanan.mp3'
depan = '/home/pi/GLASSTIC/maju.mp3'
mundur = '/home/pi/GLASSTIC/mundur.mp3'

# jika 1 = kiri, 2= kanan, 3 = depan
def play_speaker(speaker):
  if (speaker == 1):
    print ("kiri")
    media= vlc.MediaPlayer(kiri)
    media.play()
  
  elif (speaker == 2):
    print ("kanan")
    media= vlc.MediaPlayer(kanan)
    media.play()

  elif (speaker == 3):
    print ("depan")
    media= vlc.MediaPlayer(depan)
    media.play()

  elif (speaker == 4):
    print ("mundur")
    media= vlc.MediaPlayer(mundur)
    media.play()

  else:
    print("Program tidak berjalan!")
  