def solution(S):
    max_words = 0  # Initialize the maximum word count
    sentences = S.split('.')  # Split the text into sentences using '.'
    for sentence in sentences:
        sentence = sentence.replace("!", "").replace("?", "")  # Remove '!' and '?'
        words = sentence.split()  # Split the sentence into words
        word_count = len(words)  # Count the words
        max_words = max(max_words, word_count)  # Update if this count is higher
    return max_words
