def is_palindrome():
    word = input('Insert a word: ').lower()
    reversed_word = ''.join(reversed(word)).lower()
    if word == reversed_word:
        print("IS PALINDROME")
    else:
        print("IS NOT PALINDROME")

is_palindrome()

