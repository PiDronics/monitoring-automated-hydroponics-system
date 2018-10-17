# Polling Raspberry Pi Sensors and Updating Firebase Database
This repository contains code that interfaces with and returns the results of various sensors on a Raspberry Pi, and pushes these results in 2 minute increments to Firebase DB.
___
### Requirements
1. [Pyrebase](https://github.com/thisbejim/Pyrebase)- A simple python wrapper for the Firebase API.
2. [DHT11](https://github.com/szazo/DHT11_Python)- A simple class that can be used to read temperature and humidity values from DHT11 sensor on Raspberry Pi.
___
### Usage
1. `pip install pyrebase dht11`
2. `git clone https://github.com/PiDronics/monitoring-automated-hydroponics-system.git`
3. Edit the `env.py` file with the relevant credentials.
