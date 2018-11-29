import unittest 
import poll_sensors, temp, ph

class TestUnitTests(unittest.TestCase):
    def setUp(self):
        print("Running the setup before the test")
    

    def test_dataTypes(self):
        self.assertIsInstance(poll_sensors.instance, temp.TemperatureSensor)
        # test if result is an object
        # test if result.temperature and result.humidity are floats
        
    # def test_poll(self):
    #     res = poll()
    #     self.assertEqual(res, )

    # def test_libraries(self):

    def test_equal(self):
        param1 = ' '
        param2 = ' '
        self.assertEqual(param1, param2)

    def tearDown(self):
        print("Running the operation after the test")

if __name__ == '__main__':
    unittest.main()