from cleaner import file_cleaner
from dictogram import Dictogram
from sample import stochastic_sample
import random

# cleaning the corpus and returning as a list of strings - also can be considered as tokenization
pure_text = file_cleaner("./sample_words.txt")
# pure_text = file_cleaner("./fish.txt")
# print(pure_text)

def markov_chain_one(pure_text):
    """
    Goes through the input text, after determining the sequence of string
    generates 1st order markov chain
    """
    markov_chain = {}

    # iterating over the list and want to use each word as key, value as nested dict for markov_dict
    for index in range(len(pure_text)-1):
        word = pure_text[index]
        
        # filling the markov chain dict
        if word not in markov_chain:
            markov_chain[word] = Dictogram([pure_text[index + 1]])
            # if a word is already in markov chain, add_count
        else:
            markov_chain[word].add_count([pure_text[index + 1]])

    return markov_chain

# print(markov_chain_one(pure_text))

def markov_chain_n_order(n_order, pure_text):

    markov_chain = {}
    # iterating over the list and want to use each word as key, value as nested dict for markov_chain
    for index in range(len(pure_text)-n_order):
        # pure_text[index] should be our word from list
        sequence_range = tuple(pure_text[index: index + n_order])
        # print("sequence range", sequence_range)
        # check if key is stored already
        if sequence_range not in markov_chain:
            #  create new entry with window as key and dictogram as value
            markov_chain[sequence_range] = Dictogram([pure_text[index + n_order]])     
        else:
            # append it to the existing histogram
            markov_chain[sequence_range].add_count([pure_text[index + n_order]])
           
    return markov_chain

# markov_chain_n_order(3, pure_text)

def starting_word(pure_text, markov_chain):
    """
    Returns randomly picked word from the list of pure_text
    """
# randomly choose a word from array version of pure text
# find the markov_chain.key that has that randomly chosen word
# return the whole key.
    rand_ind = random.randint(0, len(pure_text)-1)
    random_word = pure_text[rand_ind]

    for words in markov_chain.keys():
        if random_word in words:
            return words
   


# print(starting_word(pure_text))
def generate_sentence(length, markov_chain):
    """
    Takes markov chained dictionary and generates a sentence
    """
    output_sentence = []
    
    current_words = starting_word(pure_text, markov_chain)
    # while length of the output is not equal to wanted length
    output_sentence.append(current_words)
    print("output before while loop", output_sentence)
    while len(output_sentence) != length:  # and current_words in markov_chain

    # randomly choose next word from the starting words (values()) based on weight
        print("current_word", current_words)
        print("current_words value is: ", markov_chain.get(current_words))
        
        next_word = stochastic_sample(markov_chain.get(current_words))
        print("next word", next_word)
        output_sentence.append(next_word)
        current_words = next_word
        current_words = starting_word(pure_text, markov_chain)
    # update the current_word = chosen child of previous word
    print(*output_sentence)
    # TODO: if the word is last in the text its breaking


if __name__ == '__main__':
    markov_chain = markov_chain_n_order(3, pure_text)
    # print(starting_word(pure_text, markov_chain))
    # print(markov_chain)
    generate_sentence(8, markov_chain)
    

