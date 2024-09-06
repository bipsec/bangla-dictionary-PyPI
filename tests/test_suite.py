import os
import sys
import unittest
from tests.test_dict import TestBanglaDictionary

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestBanglaDictionary))
    return test_suite
