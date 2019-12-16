""" This cleaner function belongs to Jackson Ho. Thanks Jackson!!!"""

def file_cleaner(file_name):

    with open(file_name) as f:  # with open automatically closes the file after extracting the content

        # This line is from Zurich Okoren github
        punctuation_table = str.maketrans('\n-', '  ', '''1234567890~!@#$.,%^&*()_+?/`[];'":|♔''')

        mostly_filtered_text = f.read().translate(punctuation_table).replace('--', ' ')
        mostly_filtered_text = mostly_filtered_text.replace('\ufeff', '')
        pure_text = mostly_filtered_text.lower().split()

        # This is how list comprehension works
        for index in range(len(pure_text)):
            pure_text[index] = pure_text[index].strip()
        # returns list
        return pure_text


if __name__ == '__main__':
    file = "./sample_words.txt"
    file_cleaner(file)
