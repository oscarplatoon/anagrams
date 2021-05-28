# Don't forget to run your tests!

def is_character_match(string1, string2):
	#sort both strings and lower() them
	sorted_string1 = sorted(string1.lower())
	sorted_string2 = sorted(string2.lower())
	# return the comparrison of the two sorted strings
	return sorted_string1 == sorted_string2




# print(is_character_match('this is str1', 'this is str 2'))
# print(is_character_match('charm', 'march'))
# print(is_character_match('zach', 'attack'))
# print(is_character_match('CharM', 'mARcH'))
# print(is_character_match('abcde2', 'c2abed'))