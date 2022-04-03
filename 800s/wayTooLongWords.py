"""
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is 
quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be 
replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the 
number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be 
replaced by the abbreviation and the words that are not too long should not undergo any changes.

Inputs: The first input is an integer of the number of lines, the following input contains n number of lines from lengths 1-
100. 

Outputs: print n lines, the i-th line should contain the result of replacing the i-th word from the input data.

Solution:

This seems to involve using string slicing to count the middle of a string and convert that len into a number.
You can get the first and last character using slicing, then + 1 them to get the number to submit between them.
"""
def wordShorten(lines):
    # Looping for the number of lines
    for i in range(lines):
        # Getting the inputted string
        word = str(input())
        # If the word has more then 10 characters
        if len(word) > 10:
            # store the first and last letter.
            firstChar = word[0]
            lastChar = word[-1]
            # count the number of characters between them
            wordDiff = len(word[1:-1])
            # Concatenate them together
            word = firstChar + str(wordDiff) + lastChar
            # Display word
            print(word)
        else:
            print(word)

def main():
    # Getting the number of times to loop for.
    numberOfLines = int(input())
    wordShorten(numberOfLines)

if __name__ == "__main__":
    main()
