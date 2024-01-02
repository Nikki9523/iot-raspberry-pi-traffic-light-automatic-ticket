from sense_hat import SenseHat
import storeFileFB
sense = SenseHat()
traffic_violation = False

def detect_movement_on_red_light():
        global traffic_violation
        redLight = storeFileFB.read_firebase_boolean("/red_light_value")
            #https://sense-hat.readthedocs.io/en/latest/api/
            #https://github.com/raspberrypilearning/getting-started-with-the-sense-hat/blob/master/worksheet3.md
            #https://github.com/astro-pi/python-sense-hat/blob/master/docs/api.md
        acceleration = sense.get_accelerometer_raw()
        x, y, z = acceleration['x'], acceleration['y'], acceleration['z']

            # Check if the movement along the x axis changes
        if x > 0.1 and redLight:
                print("Driver broke red light!")
                traffic_violation = True

                return traffic_violation
        

if __name__ == "__main__":
    detect_movement_on_red_light()