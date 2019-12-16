import random
import sys
from pprint import pprint
from time import sleep

from cleaner import file_cleaner
from dictogram import Dictogram
from sample import stochastic_sample


def delay_print(string):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)
    print('')
    return ">>"

def markov_chain_one(pure_text):
    """
    Goes through the input text, after determining the sequence of string
    generates 1st order markov chain
    """
    markov_chain = {}

    # iterating over the list and want to use each word as key, value as nested dict for markov_dict
    for index in range(len(pure_text)-1):
        word = pure_text[index]
        next_word = pure_text[index + 1]
        
        # filling the markov chain dict
        if word not in markov_chain:
            markov_chain[word] = Dictogram()
            # if a word is already in markov chain, add_count
        markov_chain[word].add_count(next_word)

    return markov_chain

# print(markov_chain_one(pure_text))

def markov_chain_n_order(n_order, pure_text):

    markov_chain = {}
    # iterating over the list and want to use each word as key, value as nested dict for markov_chain
    for index in range(len(pure_text) - n_order):
        # pure_text[index] should be our word from list
        previous_words = tuple(pure_text[index : index + n_order])
        next_word = pure_text[index + n_order]
        # print("sequence range", sequence_range)
        # check if key is stored already
        if previous_words not in markov_chain:
            #  create new entry with window as key and dictogram as value
            markov_chain[previous_words] = Dictogram()
        # append it to the existing histogram
        markov_chain[previous_words].add_count(next_word)
           
    return markov_chain

# markov_chain_n_order(3, pure_text)

def starting_word(pure_text, markov_chain):
    """
    Returns randomly picked word from the list of pure_text
    """
    # randomly choose a word from array version of pure text
    # find the markov_chain.key that has that randomly chosen word
    # return the whole key.
    rand_ind = random.randrange(len(pure_text))
    random_word = pure_text[rand_ind]

    for words in markov_chain.keys():
        if random_word in words:
            return words
    

def starting_state(markov_chain, word=None):
    """
    Returns randomly picked state from the Markov chain
    """
    starting_keys = []

    if word is None:
        return random.choice(list(markov_chain.keys()))
    else:    
        for words_tuple in markov_chain.keys():
            if word in words_tuple:
                starting_keys.append(words_tuple)
        # returns tuple
        return random.choice(starting_keys)


# print(starting_word(pure_text))
def generate_sentence(markov_chain, length=8, word=None):
    """
    Takes markov chained dictionary and generates a sentence
    """
    # current_words = starting_word(pure_text, markov_chain)
    # user's choice of words should be passed into this function
    previous_state = starting_state(markov_chain, word)
    print(f"starting state inside sentence gen func {previous_state}")
    # print('start state:', previous_state)
    if previous_state not in markov_chain:
        print(previous_state, "not in Marov chain")

    sampled_words = []
    sampled_words.extend(previous_state)

    # while length of the output is less than wanted length
    # sampled_words.append(current_words)
    # print("output before while loop", sampled_words)
    while len(sampled_words) < length:  # and current_words in markov_chain

    # randomly choose next word from the starting words (values()) based on weight
        # print("current_word", current_words)
        # print("current_words value is: ", markov_chain.get(current_words))
        histogram = markov_chain.get(previous_state)
        next_word = stochastic_sample(histogram)
        # print('next_word:', next_word)

        # print("next word", next_state)
        # new_word = next_state[-1]
        sampled_words.append(next_word)

        words_to_keep = list(previous_state[1:])
        words_to_keep.append(next_word)
        next_state = tuple(words_to_keep)
        # print('next_state:', next_state)
        # next_state now looks like (_, _, next_word)

        if next_state not in markov_chain:
            print(next_state, "not in Marov chain")
            break

        previous_state = next_state
        # current_words = starting_word(pure_text, markov_chain)
    # update the current_word = chosen child of previous word
    sentence = ' '.join(sampled_words)
    final_sentence = sentence.capitalize() + "."
    return final_sentence
    # delay_print(final_sentence)
    


if __name__ == '__main__':
    order = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    filename = sys.argv[2] if len(sys.argv) > 2 else "./sample_words.txt"
    # cleaning the corpus and returning as a list of strings - also can be considered as tokenization
    pure_text = file_cleaner(filename)
    # pure_text = file_cleaner("./sample_words.txt")
    # pure_text = file_cleaner("./corpus.txt")
    # print(pure_text)
    markov_chain = markov_chain_n_order(order, pure_text)
    # print('start state:', starting_state(markov_chain))
    # pprint(markov_chain)
    starting_state(markov_chain, "loxy")
    print(generate_sentence(markov_chain, 9))
