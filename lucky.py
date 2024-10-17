import difflib

def correct_spelling(word, word_list):
    """
    Corrects the spelling of a given word based on a provided word list.
    
    Parameters:
    word (str): The word to correct.
    word_list (list): A list of correct words for comparison.
    
    Returns:
    str: The closest match to the given word from the word list.
    """
    suggestions = difflib.get_close_matches(word, word_list, n=1, cutoff=0.8)
    return suggestions[0] if suggestions else word

# Example usage
word_list = ["apple", "banana", "orange", "grape", "pineapple"]
word = "appl"
corrected_word = correct_spelling(word, word_list)
print(f"Original word: {word} -> Corrected word: {corrected_word}")
