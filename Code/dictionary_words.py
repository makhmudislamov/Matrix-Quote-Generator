import random

def dictionary_words(word_amount=None):

    
    # read in the words file
    with open('/usr/share/dict/words', 'r') as f:
        read_data = f.read()
        # splits the words after each space
        # and puts them into a list
    read_data_list = read_data.split()
    
    # from the list above choose random word_amount and print it as a sentence.
    # example. user inputs 5
    # functions should pick random 5 words and print it on the console with "." at the end
    # we can use fisher-yates shuffle to pick random 5 words and print it on the console

    # generating random index from 0 to len of list   
    rand_indx = random.randint(0, len(read_data_list)-1)

    # now limit the random word pick to word_count input by user
    for rand_indx in range(0, word_amount + 1):

        random_words = read_data_list[rand_indx]
        print(random_words)




    


    # select a random set of words from the file and store in a data type
    # put the number of words requested together into a "sentence"
    # output your sentence


if __name__ == '__main__':
    dictionary_words(10)
