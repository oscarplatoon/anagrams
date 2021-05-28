from character_match import is_character_match
import unittest

# For this challenge you will make a program that takes in two different strings and see if the invidual letter or number characters in a string match in both strings. For example, 'abcde2' can be rearranged to 'c2abed'.

# ## Example
# Your program should return true for all the following examples...
# ```
# is_anagram('charm', 'march')
# is_anagram('CharM', 'mARcH')
# is_anagram('abcde2', 'c2abed')


class test_character_match(unittest.TestCase):
    def test_output(self):
        self.assertEqual(is_character_match('charm', 'march'), True)

    # def test_input_length(self):
    #     self.assertEqual((len('charm'), len('march')))

    def test_output_boolean(self):
        self.assertEqual(is_character_match('charm', 'march'), True)




# This should return a bunch of trues
# print(is_character_match('charm', 'march') == True)
# print(is_character_match('zach', 'attack') == False)
# print(is_character_match('CharM', 'mARcH') == True)
# print(is_character_match('abcde2', 'c2abed') == True)

# print("This test is for the challenge quesiton")
# print(is_character_match('Anna Madrigal', 'A man and a girl') == True)


# Can you translate this driver code to unit tests?


if __name__ == '__main__':
    unittest.main()