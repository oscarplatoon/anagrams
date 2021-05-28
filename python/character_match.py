# Don't forget to run your tests!

def is_character_match(string1, string2):
	# convert both strings to lower case lists of sorted characters, compare them
	return sorted(list(string1.lower())) == sorted(list(string2.lower()))
	
