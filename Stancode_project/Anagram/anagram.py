"""
File: anagram.py
Name:Jacky Wu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    pre-condition: User needs to input word sting in the console. If want to finish the program, please type -1
    post-condition: The program will find out all anagrams in the attached dictionary, and print answers on the console.
    """
    while True:
        print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
        word = input("Find anagrams for: ")
        if word == EXIT:
            break
        else:
            print("Searching...")
            start = time.time()
            ####################
            dic_lst = read_dictionary(word)
            check_list = find_anagrams(word)
            ans = []
            for i in range(len(check_list)):
                if check_list[i] in dic_lst:
                    print("Found: ", check_list[i])
                    print("Searching...")
                    ans.append(check_list[i])
            print(len(ans), "anagrams: ", ans)
            ####################
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    :param s: string type. Tested word string
    :return: All terms that match the len of tested word, and match amount of every character in the tested word.
             The terms will be saved in a list and return.
    """
    # find out how many characters from tested word and their amounts
    word_count = {}
    for i in range(len(s)):
        if s[i] in word_count:
            word_count[s[i]] += 1
        else:
            word_count[s[i]] = 1

    p_l = []
    with open(FILE, "r") as f:
        for line in f:
            a = line.strip()
            # only output same length with tested word
            if len(a) == len(s):
                twc = {}
                # find out how many characters from selected term (dictionary) and their amounts
                for i in range(len(a)):
                    if a[i] in twc:
                        twc[a[i]] += 1
                    else:
                        twc[a[i]] = 1
                # check same characters number between tested word and selected term from dictionary
                # find out if they have same characters
                if len(twc) == len(word_count):
                    t = 0
                    f = 0
                    for key in twc:
                        if key in word_count:
                            t += 1
                        else:
                            f += 1
                    if f != 0:
                        pass
                    else:
                        p_l.append(a)
    return p_l


def find_anagrams(s):
    """
    :param s: string type. Tested word string
    :return: A list contains all possibilities of anagram of tested word
    """
    index = 0
    a = find_anagrams_helper(s, [], index)
    return a


def find_anagrams_helper(s, p_w, index):
    """
    :param s: Tested word. During iteration, could be either string type or list type
    :param p_w: Empty list
    :param index: Index to count iteration. start from 0
    :return: A list contains all possibilities of anagram of tested word
    """
    if index == len(s)-1:
        a = "".join(s)
        # if a already exist in the p_w, pass, if not, save in the p_w
        if a in p_w:
            pass
        else:
            p_w.append(a)
    for i in range(index, len(s)):
        potential_word = list(s)
        potential_word[index], potential_word[i] = potential_word[i], potential_word[index]
        find_anagrams_helper(potential_word, p_w, index+1)

    return p_w

# def has_prefix(sub_s):
#     """
#     :param sub_s:
#     :return:
#     """
#     dic = read_dictionary()
#     for i in range(len(dic)):
#         if dic[i].startswith(sub_s):
#             return True


if __name__ == '__main__':
    main()
