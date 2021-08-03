import unittest

"""
This is just to test that CircleCI is running well
If there is no test, CircleCI will let the build fails
"""

"""
To run the tests
pytest
pytest -rP
pytest -rP --junitxml=test-reports/junit.xml --html=test-reports/pytest_report.html --self-contained-html
"""

class CircleCITestCase(unittest.TestCase):
    def test_001(self):
        self.assertEqual(1,1)
        print("test_001: testing CircleCI")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()