def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_num1 = str(num1)
    str_num2 = str(num2)

    def count_frequency(num_str):
        freq={}
        for digit in num_str:
            freq[digit]=freq.get(digit,0)+1
        return freq
    
    return count_frequency(str_num1)==count_frequency(str_num2)