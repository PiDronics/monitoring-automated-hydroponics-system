# Polling Raspberry Pi Sensors and Updating Firebase Database

This repository contains code that interfaces with and returns the results of various sensors on a Raspberry Pi, and pushes these results in 2 minute increments to Firebase DB. An Abstract Sensor class allows for the easy addition of various sensors, by requiring consistent methods between them for `sleep()`, `read()` and 
___

### Requirements

1. [Pyrebase](https://github.com/thisbejim/Pyrebase)- A simple python wrapper for the Firebase API.

___
### Usage
1. Run `git clone https://github.com/PiDronics/monitoring-automated-hydroponics-system.git`
2. Run `cd monitoring-automated-hydroponics-system`
3. Edit the `env.py` file with the relevant credentials.
4. Run `pip install -r requirements.txt` to install the required libraries.
5. Assuming pH sensor is properly connected to the Raspberry Pi, run `python runner.py`. The Raspberry Pi will begin polling the sensor based on the interval set during System creation, and the reading will be viewable on the [app](https://comp3613-pisynthesis.firebaseapp.com)
