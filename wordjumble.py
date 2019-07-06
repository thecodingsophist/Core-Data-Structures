# This method gets all the words inside the dictionary and returns a list of the words
def get_file_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines

# This method takes all the words inside the dictionary and sorts the words by lowercase, alphabetically
def sort_lexicon(list):
    sorted_lexicon = {}
    for word in list:
        lc_word = word.lower()
        sorted_word = ''.join(sorted(lc_word))
        sorted_lexicon[sorted_word] = lc_word
    return sorted_lexicon

# This method unscrambles a given word and returns the unscrambled word
def word_unscramble(word):
    """Unscrambles a word"""
    lc_word = word.lower()
    sorted_word = ''.join(sorted(lc_word))
    sorted_lexicon = sort_lexicon(get_file_lines())
    if sorted_word in sorted_lexicon:
        print("THE UNSCRAMBLED WORD IS: ", sorted_lexicon[sorted_word])
        return sorted_lexicon[sorted_word]

# This method unscrambles a list of words and returns the unscrambled list of words
def words_unscramble(words):
    """Unscrambles the list of words"""
    unscrambled_words = []
    for word in words:
        unscrambled_words.append(word_unscramble(word))
    return unscrambled_words

def solve_word_jumble(words, circles, final):
    """Solve a word jumble by unscrambling four jumbles, then a final jumble.
    Parameters:
    - words: list of strings, each is the scrambled letters for a single word
    - circles: list of strings, each marks whether the letter at that position
        in the solved anagram word will be used to solve the final jumble.
        This string contains only two different characters:
        1. O (letter "oh") = the letter is in the final jumble
        2. _ (underscore) = the letter is not in the final jumble
    - final: list of strings in the same format as circles parameter that shows
        how the final jumble's letters are arranged into a word or phrase."""
    # Get all English words in the built-in dictionary
    all_words = get_file_lines()
    # Solve this word jumble with data structures and algorithms

    # This first part unscrambles the words
    word_list = words_unscramble(words)
    word_list_joined = "".join(word_list)
    # This next part takes out the O's of the words
    index = 0
    circles_joined = "".join(circles)
    almost_final = ""
    for circle in circles_joined:
        if circle == "O":
            almost_final += word_list_joined[index]
        index += 1
    print("THE FINAL SCRAMBLED LETTERS ARE: ", almost_final)
    return almost_final

def main():
    # Word Jumble 1. Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his ___."
    words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles1 = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final1 = ['OO', 'OOOOOO']
    solve_word_jumble(words1, circles1, final1)

#     # Word Jumble 2. Cartoon prompt for final jumble: "What a dog house is."
#     words2 = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
#     circles2 = ['____O', '_OO__', '_O___O', 'O____O']
#     final2 = ['OOOO', 'OOO']
#     solve_word_jumble(words2, circles2, final2)


if __name__ == '__main__':
    main()
