import sys
def get_book_text(books):
	with open(books) as f:
		file_contents = f.read()
	return file_contents

from stats import word_count
from stats import lower_case
from stats import sort_char
def main():
	if len(sys.argv) == 2:
		book_path = sys.argv[1]
		text =get_book_text(book_path)
		num_words = word_count(text)
		print(num_words,"words found in the document")
		my_char_counts = lower_case(text)
		sorted_chars=sort_char(my_char_counts)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {book_path}...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for item in sorted_chars:
			if item["char"].isalpha():
				print(f"{item['char']}: {item['num']}")
		print("============= END ===============")
	else:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
main()
