from character_match import is_character_match
import unittest

class CharMatchTestCase(unittest.TestCase):

    def test_bool(self):
        self.assertIsInstance(is_character_match('', ''), bool)

    def test_charm_march(self):
        self.assertEqual(is_character_match('charm', 'march'), True)

    def test_zach_attack(self):
        self.assertEqual(is_character_match('zach', 'attack'), False)
    
    def test_charm_cases(self):
        self.assertEqual(is_character_match('CharM', 'mARcH'), True)
    
    def test_abcde2_c2abed(self):
        self.assertEqual(is_character_match('abcde2', 'c2abed'), True)

    def test_spaced_strings(self):
        self.assertEqual(is_character_match('Anna Madrigal', 'A man and a girl'), True)
# Can you translate this driver code to unit tests?
