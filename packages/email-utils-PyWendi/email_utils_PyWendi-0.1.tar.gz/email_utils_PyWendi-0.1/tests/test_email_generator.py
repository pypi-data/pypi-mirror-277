import unittest
from email_utils.email_generator import generate_random_email


class TestEmailGenerator(unittest.TestCase):
    def test_generate_random_email(self):
        email = generate_random_email()
        self.assertTrue("@" in email)
        self.assertTrue(email.endswith("@exemple.com"))

    def test_generate_random_email_with_custom_domain(self):
        domain = "testdomain.com"
        email = generate_random_email(domain)
        self.assertTrue(email.endswith(f"@{domain}"))


if __name__ == "__main__":
    unittest.main()
