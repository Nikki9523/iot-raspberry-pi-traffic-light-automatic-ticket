# Project Title

IOT Project to detect vehicles breaking red lights. Run using lightControl.py. As script runs green, orange and red light will display on SenseHAT led lights.
If movement is detected while light is red then an image will be captured with PiCamera module3 and pushed to Firebase.
Latest captured image is displayed on glitch site.

Note: Currently movement is detected when senseHAT is moved. Future iteration will detect external movement of vehicle using PIR sensor or similar.


## Getting Started
1. Import files onto raspberry pi
2. create .json file and store firebase details for use in storeFileFB.py
3. run lightControl.py script


### Tools and Technologies Used
1.Raspberry Pi 4 
2. SenseHAT
3. PiCamera module 3
4. Glitch
5. Python
6. Firebase
