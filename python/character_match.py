# Don't forget to run your tests!
def is_character_match(string1, string2):
	words = [string1.lower().replace(" ", ""), string2.lower().replace(" ", "")]
	sorted_words = ["".join(sorted(w)) for w in words]

	return sorted_words[0] == sorted_words[1]