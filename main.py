from stats import get_word_count, get_letter_count, sort_letters
import sys


def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
        	print("Usage: python3 main.py <path_to_book>")
        	sys.ext(1)
	filepath = sys.argv[1]

	book_text = get_book_text(filepath)
	num_words = get_word_count(book_text)
	print(f'Found {num_words} total words')

	char_counts = get_letter_count(book_text)
	sorted_chars = sort_letters(char_counts)

	print("\nCharacter Frequency Report:")
	for item in sorted_chars:
		print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
        main()
