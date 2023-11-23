# Project Name
Automatic ticketing system for breaking red lights
#### Student Name: Nicola Stack   Student ID: 13373226

Lately in Galway I've noticed more and more people breaking red lights. 
This is dangerous as they could cause an accident or knock down someone waiting at pedestrian crossings. 
Drivers take risks breaking red lights as there is normally nobody there to pull them over so they think they'll get away with it.
My project will explore an automatic ticketing system using a toy car, raspberry pi, camera phillips hue bulb for the "traffic light".

1. Traffic light will be green or amber
2. Toy can move past Load Cell without triggering event
3. Light changes to red
4. Toy car moves onto load sensor
5. camera takes picture of car
6. image is sent to Thingspeak
7. Email notification is sent to the "driver" of the car with fine info and image
8. Record of incident is shown on a simple webapp portal
9. If toy car does not move onto or passed load sensor nothing happens

## Tools, Technologies and Equipment
- Python
- Raspberry Pi
- Raspberry Pi Camera Module
- Raspberry Pi Load Cell to accurately detect toy car
- Colour Phillips hue bulb to represent the traffic lights
- Toy car
- Thingspeak

## Project Repository
https://github.com/Nikki9523/iot-raspberry-pi-traffic-light-automatic-ticket
