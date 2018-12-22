# Polling Raspberry Pi Sensors and Updating Firebase Database

This repository contains code that interfaces with and returns the results of various sensors on a Raspberry Pi, and pushes these results in 2 minute increments to Firebase DB. An Abstract Sensor class allows for the easy addition of various sensors, by requiring consistent methods between them for `read()`. In addition, a Firebase class was created using the Database abstract class, requiring the `authenticate()` and `push()` methods. This increases the maintainability, testability and modularity of the system.

The [Product Manual] (https://docs.google.com/document/d/1FWLsea7MBdXaazkmk156T1Quhn5-B72oxn0frQKcgs8/edit?usp=sharing) can be found here on how to get started with your RPiDronics and for details on setting up the various sensors and probes.
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
