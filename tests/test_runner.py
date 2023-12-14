import unittest
from test_suite import suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_result = runner.run(suite())

    # Check if there are failures
    if test_result.failures or test_result.errors:
        print("Tests failed.")
    else:
        print("All tests passed.")
