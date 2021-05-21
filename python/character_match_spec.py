from character_match import is_character_match

# This should return a bunch of trues
# print(is_character_match('charm', 'march') == True)
# print(is_character_match('zach', 'attack') == False)
# print(is_character_match('CharM', 'mARcH') == True)
# print(is_character_match('abcde2', 'c2abed') == True)

# print("This test is for the challenge quesiton")
# print(is_character_match('Anna Madrigal', 'A man and a girl') == True)


# Can you translate this driver code to unit tests?

import unittest

class TestCharacterMatch(unittest.TestCase):
    def test_returns_bool(self):
        self.assertEqual(type(is_character_match("a", "b")), bool)

    def test_works_for_all_lower(self):
        self.assertEqual(is_character_match('charm', 'march'), True)
    
    def test_works_for_capital_letters(self):
        self.assertEqual(is_character_match('CharM', 'mARcH'), True)
    
    def test_works_with_numbers(self):
        self.assertEqual(is_character_match('abcde2', 'c2abed'), True)

    def test_fails_correctly(self):
        self.assertEqual(is_character_match('march', 'match'), False)