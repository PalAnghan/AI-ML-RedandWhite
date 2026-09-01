def count_vowels(text):
    """Counts the number of vowels (a, e, i, o, u) in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
