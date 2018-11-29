# Polling Raspberry Pi Sensors and Updating Firebase Database
This repository contains code that interfaces with and returns the results of various sensors on a Raspberry Pi, and pushes these results in 2 minute increments to Firebase DB. An Abstract Sensor class allows for the easy addition of various sensors, by requiring consistent methods between them for `sleep()`, `read()` and 
___
### Requirements
1. [Pyrebase](https://github.com/thisbejim/Pyrebase)- A simple python wrapper for the Firebase API.
___
### Usage
1. `git clone https://github.com/PiDronics/monitoring-automated-hydroponics-system.git`
2. Edit the `env.py` file with the relevant credentials.
