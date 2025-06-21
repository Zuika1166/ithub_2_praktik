
import unittest
from form_matcher import find_template

class TestFormMatcher(unittest.TestCase):
    def test_match_template(self):
        templates = [
            {"name": "Test", "login": "email", "tel": "phone"}
        ]
        query = {
            "login": "test@example.com",
            "tel": "+7 123 456 78 90"
        }
        self.assertEqual(find_template(query, templates), "Test")

    def test_no_match(self):
        templates = [
            {"name": "Test", "login": "email", "tel": "phone"}
        ]
        query = {
            "name": "Vasya",
            "date": "27.05.2025"
        }
        self.assertEqual(find_template(query, templates), {"name": "text", "date": "date"})

    def test_extra_fields_in_query(self):
        templates = [
            {"name": "Test", "login": "email"}
        ]
        query = {
            "login": "test@example.com",
            "extra": "some extra value"
        }
        self.assertEqual(find_template(query, templates), "Test")

    def test_incorrect_phone_format(self):
        templates = [
            {"name": "Test", "tel": "phone"}
        ]
        query = {
            "tel": "123456"
        }
        self.assertEqual(find_template(query, templates), {"tel": "text"})

    def test_iso_date_format(self):
        templates = [
            {"name": "Test", "birthdate": "date"}
        ]
        query = {
            "birthdate": "2024-01-01"
        }
        self.assertEqual(find_template(query, templates), "Test")

    def test_template_without_name_is_ignored(self):
        templates = [
            {"login": "email"} 
        ]
        query = {
            "login": "test@example.com"
        }
        self.assertEqual(find_template(query, templates), {"login": "email"})

if __name__ == '__main__':
    unittest.main()
