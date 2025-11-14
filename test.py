# written by Hollister Mala

import unittest
import csv 
import zscore
import math

def loadFromFile(filename):
    test_cases = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            test_cases.append(row)
    return test_cases

def cmp_float(a,b):
    return math.isclose(a,b, rel_tol=0, abs_tol=1e-8)

def test_case(case):
    def test(self):
        x, mu, sigma, expected = case
        result = zscore.z_score(float(x), float(mu), float(sigma))
        outcome = cmp_float(float(expected), result)
        print(f"{"PASS" if outcome else "FAIL"}: x={x} mu={mu}, sigma={sigma}, result={result}, expected={expected}, difference={abs(float(expected) - result)}")
        self.assertTrue(outcome)
    
    return test

class TestZScore(unittest.TestCase):
    pass

if __name__ == '__main__':
    test_cases  = loadFromFile("./Zscore - A.csv")
    test_cases += loadFromFile("./Zscore - B.csv")
    test_cases += loadFromFile("./Zscore - C.csv")
    test_cases += loadFromFile("./Zscore - D.csv")
    test_cases += loadFromFile("./tests.csv")

    for (i,t) in enumerate(test_cases):
        test_name = f"test_{i}"
        test = test_case(t)
        setattr(TestZScore, test_name, test)
    unittest.main()
