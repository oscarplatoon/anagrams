def anagrams_for(words, test_words):



		#checks if a single test_word is an anagram of words
		# test_word=test_word.lower()
		# words=words.lower()
	for x in words:
		temp_test = 0
		for y in range(len(test_word)):

			if x==test_word[y-1]:
				test_word = test_word[:y-1] +test_word[y:]
				temp_test=1
		if temp_test==0:
			return False		
	return True


print(anagrams_for("threads","threads"))