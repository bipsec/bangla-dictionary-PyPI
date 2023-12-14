import unittest
from io import StringIO
from unittest.mock import patch
from scripts.translator import ipa_checker


class TestBanglaIPA(unittest.TestCase):
    def test_ipa_checker(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            ipa_checker("চাষাবাদ")
            expected_output = "caʃabad̪\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
