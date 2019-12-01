
def dictionary_words(word_amount=None):

    
    # read in the words file
    with open('/usr/share/dict/words', 'r') as f:
        read_data = f.read()
        # splits the words after each space
        # and puts them into a list
        splitted_data = read_data.split()
    
    

    


    # select a random set of words from the file and store in a data type
    # put the number of words requested together into a "sentence"
    # output your sentence


if __name__ == '__main__':
    dictionary_words()
