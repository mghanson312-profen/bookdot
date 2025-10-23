def get_word_count(book_text):
        words = book_text.split()
        num_words = len(words)
        return num_words

def get_letter_count(book_text):
	text = book_text.lower()
	char_counts = {}
	for char in text:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def sort_letters(char_dict):
	sorted_list = [
		{"char": char, "num": count}
		for char, count in char_dict.items()
		if char.isalpha()
	]

	def sort_by_num(item):
		return item["num"]

	sorted_list.sort(key=sort_by_num, reverse=True)
	return sorted_list
