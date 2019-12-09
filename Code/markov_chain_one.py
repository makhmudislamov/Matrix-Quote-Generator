from cleaner import file_cleaner
from dictogram import Dictogram
import sample

# cleaning the corpus and returning as a list of strings - also can be considered as tokenization
pure_text = file_cleaner("./sample_words.txt")
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
        print("sequence range", sequence_range)
        # check if key is stored already
        if sequence_range not in markov_chain:
            #  create new entry with window as key and dictogram as value
            markov_chain[sequence_range] = Dictogram([pure_text[index + n_order]])     
        else:
            # append it to the existing histogram
            markov_chain[sequence_range].add_count([pure_text[index + n_order]])
           
    return markov_chain

markov_chain_n_order(3, pure_text)

def generate_sentence(m_chained_dict):
    """
    Takes markov chained dictionary and generates a sentence
    """
    output_sentence = []
    pass
    

