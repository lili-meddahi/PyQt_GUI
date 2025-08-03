import unittest
from qt_app import APIParse 

class TestAPIParse(unittest.TestCase):

    def test_parse_countries(self):
        sample_data = [
            {'name': 'Brazil'},
            {'name': 'Canada'},
            {'name': 'Argentina'}
        ]
        expected_result = ['Argentina', 'Brazil', 'Canada']
        result = APIParse.parse_countries(sample_data)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()