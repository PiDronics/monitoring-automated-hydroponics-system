from unittest import TestCase
import poll_sensors

class TestUnitTests(TestCase):
    def setUp(self):
        print("Running the setup before the test")
    
    def tearDown(self):
        print("Running the operation after the test")

    def test_dataTypes(self):
        self.assertIsInstance(poll_sensors.instance, DHT11)
        
    def test_poll(self):
        res = poll()
        self.assertEqual(res, )

    def test_libraries(self):

    def test_equal(self):
        param1 = 'wee'
        param2 = 'wee'
        self.assertEqual(param1, param2)

if __name__ == '__main__':
    unittest.main()