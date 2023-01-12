"""
File: boggle.py
Name:Jacky Wu
----------------------------------------
Enter 4 X 4 characters and the program can run all potential terms hidden within these characters with boggle rule
"""

import time
import sys

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	pre-condition: The program will ask to input 4 characters set by set. 4 sets in total.
	post-condition: The program will provide all potential terms hidden within these characters with boggle rule.
	"""
	word_bank = input_words()
	# word_bank = [["f", "y", "c", "l"], ["i", "o", "m", "g"], ["o", "r", "i", "l"], ["h", "j", "h", "u"]]
	if word_bank is None:
		pass
	else:
		read_dictionary(word_bank)
		start = time.time()
		boggle(word_bank)
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_words():
	"""
	:return: A list with 4 sets of list. Each sub-list contents 4 characters
	"""
	word_bank = []
	row_1 = input("1 row of letters: ").lower()
	if not check_format(row_1):
		return None
	else:
		word_bank.append(make_list(row_1))

	row_2 = input("2 row of letters: ").lower()
	if not check_format(row_2):
		return None
	else:
		word_bank.append(make_list(row_2))

	row_3 = input("3 row of letters: ").lower()
	if not check_format(row_3):
		return None
	else:
		word_bank.append(make_list(row_3))

	row_4 = input("4 row of letters: ").lower()
	if not check_format(row_4):
		return None
	else:
		word_bank.append(make_list(row_4))

	# print("word_bank: ", word_bank)
	return word_bank


def make_list(s):
	"""
	:param s: 4 input characters
	:return: a list of 4 characters
	"""
	s = s.replace(" ", "")
	lst = []
	for i in range(len(s)):
		lst.append(s[i])

	return lst


def boggle(n):
	"""
	:param n: A list of sub-list
	:return: None. Print result in console
	"""
	ans_lst = []
	dic = read_dictionary(n)
	for x in range(2):
		for y in range(2):
			nx = 3*x
			ny = 3*y
			ans_lst = boggle_helper(n, "", {}, ans_lst, nx, ny, dic)
	print("There are ", len(ans_lst), " words in total")


def boggle_helper(n, current_s, exist_ch, ans_lst, fl_x, fl_y, dic):
	"""
	:param n: A list of sub-list
	:param current_s: A string that could be the answer term
	:param exist_ch: A dictionary saved with the characters that have been used
	:param ans_lst: A list that saved the answer terms
	:param fl_x: The x coordinator point in 4x4 boggle game
	:param fl_y: The y coordinator point in 4x4 boggle game
	:param dic: A dictionary saved with all existed term
	:return: ans_lst. A list that saved the answer terms
	"""
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			n_x = fl_x + i
			n_y = fl_y + j
			if n_x >= 0 and n_y >= 0:
				if n_x <= 3 and n_y <= 3:
					if (n_x, n_y) in exist_ch:
						pass
					else:
						current_s += n[n_x][n_y]
						if has_prefix(current_s, dic):
							exist_ch[n_x, n_y] = n[n_x][n_y]
							# exist_ch.append((n_x, n_y))
							if current_s in dic:
								if current_s not in ans_lst:
									ans_lst.append(current_s)
									print("Found ", current_s)
							boggle_helper(n, current_s, exist_ch, ans_lst, n_x, n_y, dic)
							current_s = current_s[:len(current_s) - 1]
							exist_ch.popitem()
						else:
							current_s = current_s[:len(current_s)-1]
	return ans_lst


def check_format(s):
	"""
	:param s: check the input format matches the requirements of boggle game
	:return: bool
	"""
	if len(s) != 7:
		return False
	else:
		a = s.replace(" ", "")
		if not a.isalpha():
			return False
		else:
			for i in range(0, 5, 2):
				if not s[i+1].isspace():
					return False
				else:
					return True


def read_dictionary(word_bank):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	p_l = set()
	word_bank_lst = set()
	for i in range(4):
		for j in range(4):
			word_bank_lst.add(word_bank[i][j])

	with open(FILE, "r") as f:
		for word in f:
			word = word.strip()
			if len(word) > 3:
				if len(word) < 16:
					if word[0] in word_bank_lst:
						p_l.add(word)
	return p_l


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""

	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
