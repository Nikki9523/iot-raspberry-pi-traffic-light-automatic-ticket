import datetime
import storeFileFB
from picamera2 import Picamera2
import detectMovement
import time

#Picamera module wouldn't work for me, I researched and found
#that I need to use Picamera2
camera = Picamera2()
frame = 1

#https://www.tomshardware.com/how-to/use-picamera2-take-photos-with-raspberry-pi
def configure_camera():
      camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
      camera.configure(camera_config)

      configure_camera()

def takePicture():
    global frame
    trafficViolation = detectMovement.detect_movement_on_red_light()
    while trafficViolation:
            camera.start()
            time.sleep(2)
            fileLoc = f'./images/frame{frame}.jpg'
            currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            camera.capture_file(fileLoc)
            print(f'frame {frame} taken at {currentTime}')
            storeFileFB.store_file(fileLoc)
            storeFileFB.push_db(fileLoc, currentTime)
            print('Image stored and location pushed to db')
            camera.stop()
            frame += 1
            trafficViolation = False
            time.sleep(2)

if __name__ == "__main__":
    takePicture()
      

        




        