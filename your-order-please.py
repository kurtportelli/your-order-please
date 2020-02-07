def order(sentence):
    import re
    numbers = re.findall(r'\d', sentence)
    words = sentence.split()
    zipped_lists = zip(numbers, words)
    ordered_words = [y for x, y in sorted(zipped_lists)]
    return ' '.join(ordered_words)
