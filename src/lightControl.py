from sense_hat import SenseHat
import time
import storeFileFB
import captureImage

lightDuration = 10

sense = SenseHat()
sense.clear()
green = (0, 255, 0)
red = (255,0,0)
orange = (255, 165, 0)
circleColour = green
startTime = time.time()


# Function to draw the traffic light on the sensehat

def draw_traffic_light(circleColour=(255, 0, 0)):
   circle = [
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 1, 1, 1, 1, 0, 0,
      0, 1, 1, 1, 1, 1, 1, 0,
      1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1,
      0, 1, 1, 1, 1, 1, 1, 0,
      0, 0, 1, 1, 1, 1, 0, 0
   ]

   sense.set_pixels([circleColour if pixel == 1 else (0, 0, 0) for pixel in circle])



def trafficLight():
    global startTime
    global circleColour

    currentTime = time.time()
    #calculate time in loop by subtracting time when script starts from the time it is now
    timeElapsed = currentTime - startTime
    #total time the loop takes
    totalLoopDuration = lightDuration * 2.5

    if timeElapsed > totalLoopDuration:
       #get new current time and add the time loop took to the start time
       currentTime = time.time()
       startTime = startTime + totalLoopDuration

    if timeElapsed <= totalLoopDuration:
       
       if timeElapsed <= lightDuration:
          #update redlight boolean in firebase to false
          storeFileFB.update_firebase_red_light_boolean(False)
          #set traffic light colour to green and draw it
          circleColour = green
          draw_traffic_light(green)
          
       elif timeElapsed > lightDuration and timeElapsed <= lightDuration + lightDuration / 2:
          circleColour = orange
          draw_traffic_light(orange)
          
       elif timeElapsed > (lightDuration + lightDuration / 2) and timeElapsed <= totalLoopDuration:
        #update redlight boolean to true to use in the detectMovement script
        storeFileFB.update_firebase_red_light_boolean(True)
        circleColour = red
        draw_traffic_light(red)
        #function will take picture if movement is detected
        captureImage.takePicture()


if __name__ == "__main__":
  while True:
     trafficLight()



