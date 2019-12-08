"""
Now let's try implementing this! You'll need to write code to do two things:

1. Learn a Markov chain from a corpus. You've already written code to find how often a token appears in a corpus, but now you need to find how often a token appears after another token.

2. Do a random walk on a Markov chain. This should be pretty simple if you pick a good way to store the Markov chain you learn.

Make sure to think about what data structures to use to make your code efficient. Both learning the Markov chain and taking a step of the random walk should take time at most linear in the size of the corpus.

When you're ready, try your implementation out on a real corpus and see how it compares to the stochastic sampler!
"""


from cleaner import file_cleaner
from dictogram import Dictogram

# cleaning the corpus and returning as a list of strings - also can be considered as tokenization
pure_text = file_cleaner("./sample_words.txt")
print(pure_text)



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

    
print(markov_chain_one(pure_text))
