import unittest 
import poll_sensors, temp, ph

class TestUnitTests(unittest.TestCase):
    def setUp(self):
        print("Running the setup before the test")
        temperature = poll_sensors.result.temperature
        temperatureInF = (temperature * 9/5) + 32
        humidity = poll_sensors.result.humidity

    def test_dataTypes(self):
        self.assertIsInstance(poll_sensors.instance, temp.TemperatureSensor)
        # test if result is an object
        # test if result.temperature and result.humidity are floats
        
    # def test_poll(self):
    #     res = poll()
    #     self.assertEqual(res, )

    # Testing if the temperature is within the range that the dht11 sensor can measure
    def test_tempRange(self):
        self.assertGreaterEqual(temperature, 0)
        self.assertLessEqual(temperature, 50)

        # Fahrenheit
        self.assertGreaterEqual(temperatureInF, 32)
        self.assertLessEqual(temperatureInF, 122)

        # self.assertTrue(0 <= temperature <= 50)
    
    # Testing if the humidity is within the range that the dht11 sensor can measure
    def test_humidityRange(self):
        self.assertGreaterEqual(humidity, 20)
        self.assertLessEqual(humidity, 95)

    # Example
    def test_equal(self):
        param1 = ' '
        param2 = ' '
        self.assertEqual(param1, param2)

    def tearDown(self):
        print("Running the operation after the test")

if __name__ == '__main__':
    unittest.main()