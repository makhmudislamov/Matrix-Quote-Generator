import random
import sys

def dictionary_words(word_amount=None):

    output = []
    # read in the words file
    with open('/usr/share/dict/words', 'r') as f:
        read_data = f.read()
        # splits the words after each space
        # and puts them into a list
    read_data_list = read_data.split()

    for _ in range(0, word_amount):
         # generating random index from 0 to len of list
        rand_indx = random.randint(0, len(read_data_list)-1)
        random_words = read_data_list[rand_indx]
        output.append(random_words)
    # TODO: small bug - fullstop 
    print(*output,f".")

if __name__ == '__main__':
    word_amount = int(sys.argv[1])
    dictionary_words(word_amount)
