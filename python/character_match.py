# Don't forget to run your tests!

def is_character_match(string1, string2):
	if (sorted(string1.lower().replace(' ','')) == sorted(string2.lower().replace(' ',''))):
		return True
	else:
		return False

# is_character_match('taco', 'Cota')



