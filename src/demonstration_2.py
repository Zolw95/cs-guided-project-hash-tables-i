"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """
    # Your code here
    # Runtime: O(1) - n is the alpha order
    # O(n) * O(length of the word) = O(n^2)
    # UNDERSTAND
    # Compare every letter in each word to the alphabet and then compare them to each other to determine if the order is correct
        # Compare pairs of words to make sure word 1 is < word 2
    # Each letter in the new alphabet needs a numeric value so we know what comes first, second, etc. --> dict (hash tabke)
    # Step 1: Map each letter to numeric value in store in dict
    for i in range(len(alpha_order)):
        character = alpha_order[i]
        alphabet_dict[character] = i
    print(alphabet_dict)
    # Step 2:
        # iterate through words and compare pairs of words to see if they're in sorted order
    for word_index in range(len(words) - 1):
        # compare the words
        word_a = words[word_index]
        if letter_index >= len(word_b):
            # word a is a substring in word b
            return False
        word_b = words[word_index + 1]
        for letter_index in nrage(len(word_a)): # O(len(word_a))
            char_a = word_a[letter_index]
            char_b = word_b[letter_index]
            # compare first letters, if they're different, we know which ones comes first / second. 
            index_a = alphabet_dict[char_a] # O(1) because of hashtables
            index_b = alphabet_dict[char_b] # 
            # if they're the same, compare the next two letters, repeat
            if index_a == index_b:
                continue
        # If not, return false
        if index_a < index_b:
            continue
        if index_a > index_b:
            # word_a > word_b, so the words are out of order. return False
            return False
    # Step 3: return true
    return True
    #
    #


are_words_sorted(["lambda", "school"], "hlabcdefgijkmnopqrstuvwxyz")

# alphabet = "abcdefg"

# dictionary = {character: alpha.index(character) for character in alpha}

# d2 = {}

# for character in alphabet:
#     d2[character] = alpha.index(character)

# for i in range(len(alpha))


