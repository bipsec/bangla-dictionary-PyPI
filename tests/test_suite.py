import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.test_bangla_ipa import TestBanglaIPA
from tests.test_translator import TestTranslator
from tests.test_dict import TestBanglaDictionary


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestBanglaDictionary))
    test_suite.addTest(unittest.makeSuite(TestBanglaIPA))
    test_suite.addTest(unittest.makeSuite(TestTranslator))
    return test_suite

