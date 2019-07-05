def get_file_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines


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
    # TODO: Solve this word jumble with data structures and algorithms


def main():
    # Word Jumble 1. Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his ___."
    words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles1 = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final1 = ['OO', 'OOOOOO']
    solve_word_jumble(words1, circles1, final1)

    # Word Jumble 2. Cartoon prompt for final jumble: "What a dog house is."
    words2 = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles2 = ['____O', '_OO__', '_O___O', 'O____O']
    final2 = ['OOOO', 'OOO']
    solve_word_jumble(words2, circles2, final2)


if __name__ == '__main__':
    main()
