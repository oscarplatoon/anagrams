from character_match import is_character_match
import unittest

class TestCharacterMatch(unittest.TestCase):

    def test_first_entry(self):
        self.assertEqual(is_character_match('charm', 'march'), True)

    def test_no_pair(self):
        self.assertEqual(is_character_match('CharM', 'mARcH'), True)
    
    def test_correct1(self):
        self.assertEqual(is_character_match('zach', 'attack'), False)

    def test_correct2(self):
        self.assertEqual(is_character_match('Anna Madrigal', 'A man and a girl'), True)
    



if __name__ == '__main__':
    unittest.main()




# # This should return a bunch of trues
# print(is_character_match('charm', 'march') == True)
# print(is_character_match('zach', 'attack') == False)
# print(is_character_match('CharM', 'mARcH') == True)
# print(is_character_match('abcde2', 'c2abed') == True)

# print("This test is for the challenge quesiton")
# print(is_character_match('Anna Madrigal', 'A man and a girl') == True)


# # Can you translate this driver code to unit tests?
