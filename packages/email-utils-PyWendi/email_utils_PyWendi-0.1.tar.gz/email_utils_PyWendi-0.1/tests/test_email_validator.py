import unittest
from email_utils.email_validator import is_valid_email, extract_domain


class TestEmailValidator(unittest.TestCase):
    def test_is_email_valid(self):
        self.assertTrue(is_valid_email("test@exemple.com"))
        self.assertFalse("invalid-Email")
        
    def test_extract_domain(self):
        self.assertEqual(extract_domain("test@example.com"), "example.com")
        with self.assertRaises(ValueError):
            extract_domain("invalid-email")


if __name__ == "__main__":
    unittest.main()
