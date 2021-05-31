import unittest
from character_match import is_character_match

class TestCharacterMatch(unittest.TestCase):
  
    """
    When you call is_character_match you should get a boolean back
    """

    def test_returns_a_boolean(self):
        self.assertTrue((type(is_character_match("abcd", "test"))) == bool)

    # This should return a bunch of trues

    def test_character_match_function(self):
        self.assertTrue(is_character_match('charm', 'march') == True)
        self.assertTrue(is_character_match('zach', 'attack') == False)
        self.assertTrue(is_character_match('CharM', 'mARcH') == True)
        self.assertTrue(is_character_match('abcde2', 'c2abed') == True)
        self.assertTrue(is_character_match('Anna Madrigal', 'A man and a girl') == True)

if __name__ == '__main__':
    unittest.main()

    

