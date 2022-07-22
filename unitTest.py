import unittest
from FrontEnd import FrontEnd
import re


class test_frontEnd(unittest.TestCase):
    def setUp(self):
        self.resultObject = FrontEnd.frontEnd()

    def test_ticker(self):
        testResult = self.resultObject.ticker.isalpha()
        self.assertEqual(testResult, True)

    def test_chartType(self):
        result = self.resultObject.chartType
        if result in range(1, 2):
            testResult = True
        else:
            testResult = False
        self.assertEqual(testResult, True)

    def test_timeSeries(self):
        result = self.resultObject.timeSeries
        if result in range(1, 4):
            testResult = True
        else:
            testResult = False
        self.assertEqual(testResult, True)
        
    def test_interval(self):
        result = self.resultObject.interval
        if result in range(1, 4):
            testResult = True
        else:
            testResult = False
            
    def test_startDate(self):
        dateDict = self.resultObject.startDate
        year = dateDict.get("year")
        month = dateDict.get("month")
        day = dateDict.get("day")
        if month < 10:
            month = f"0{month}"
        else:
            pass
        if day < 10:
            day = f"0{day}"
        else:
            pass
        
        testStartDate = f"{year}-{month}-{day}"
        print(testStartDate)
        form = re.compile('....-..-..')
        testResult = form.match(testStartDate) is not None
        self.assertEqual(testResult, True)

    def test_endDate(self):
        dateDict = self.resultObject.endDate
        year = dateDict.get("year")
        month = dateDict.get("month")
        day = dateDict.get("day")
        if month < 10:
            month = f"0{month}"
        else:
            pass
        if day < 10:
            day = f"0{day}"
        else:
            pass
        
        testStartDate = f"{year}-{month}-{day}"
        print(testStartDate)
        form = re.compile('....-..-..')
        testResult = form.match(testStartDate) is not None
        self.assertEqual(testResult, True)

        
if __name__ == "__main__":
    unittest.main()
    
    
