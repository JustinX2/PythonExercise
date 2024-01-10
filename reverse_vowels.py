def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels ='aeiouAEIOU'
    reversed_vowels=[char for char in s if char in vowels][::-1]

    new_chars=[]
    reversed_vowels_iter=iter(reversed_vowels)

    for char in s:
        if char in vowels:
            new_chars.append(next(reversed_vowels_iter))
        else:
            new_chars.append(char)
    return ''.join(new_chars)