def word_count(file_contents):
        words = file_contents.split()
        return len(words)
def lower_case(file_contents):
	my_char_counts ={}
	lower_case = file_contents.lower()
	for char in lower_case:
		if char in my_char_counts:
			my_char_counts[char] += 1
		else:
			my_char_counts[char] = 1
	return my_char_counts
def int_key(nums):
	return nums["num"]
def sort_char(my_char_counts):
	my_char_list = []
	for char in my_char_counts:
		new_dict = {"char":char, "num": my_char_counts[char]}
		my_char_list.append(new_dict)
	my_char_list.sort(reverse=True,key=int_key)
	return(my_char_list)
