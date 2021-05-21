# Don't forget to run your tests!

def is_character_match(string1, string2):
	string1_list = list(string1)
	string2_list = list(string2)

	string1_list = sorted([x.lower() for x in string1_list])
	string2_list = sorted([x.lower() for x in string2_list])

	if string1_list == string2_list:
		return True
	else:
		return False

is_character_match('CharM', 'mARcH')