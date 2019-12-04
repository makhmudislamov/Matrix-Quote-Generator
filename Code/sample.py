import random
from datetime import datetime
from histogram import *


def histogram_dict(word_list):
    """
    Input >>> array of strings
    Output >>> histogram in a dictionary format
    """
    hist_dict = {}

    for word in word_list:
        if word not in hist_dict:
            hist_dict[word] = 1
        else:
            hist_dict[word] += 1

    return hist_dict

def random_word(histogram):
    """
    takes a histogram (however you've structured yours) 
    and returns a single word, at random. It should not yet 
    take into account the distributions of the words
    """
    # iterate through the histogram - list
    # return one random word
    listed = list(histogram)
    rand_ind = random.randint(0, len(listed)-1)
    return listed[rand_ind]


# def rand_hist_word():
#     """
#     This function creates dictionary from CL words.
#     Then prints random word from the dictionary
#     """
#     histogram = Histogram()
#     rand_key = random.randint(0, len(histogram)-1)
#     print(histogram)
#     print([key for key in histogram.keys()][rand_key])

def stochastic_sample(histogram):
    """
    Returns random word from the dictionary based on frequency.
    """
    tokens = 0

    cumulative_probability = 0.0
    # you can use sum()
    for word_frequency in histogram.values():
        tokens += word_frequency  # this works until here, tested with print

    random_choice = random.uniform(0, 1)
    for word, word_frequency in histogram.items():
        cumulative_probability += word_frequency/tokens
        if cumulative_probability >= random_choice:
            return word


def test_iteration(histogram, iteration):
    """
    Creates hisogram based on stochastic sampling and iterating given amount to prove stochastic sampmling
    """
    word_list = [stochastic_sample(histogram) for x in range(iteration)]
    # should use Histogram class build method
    return histogram_dict(word_list)
    
if __name__ == '__main__':
    file = "./sample_words.txt"
    # print(random_word(histogram))
    histogram = Histogram().build(file)

    start_time = datetime.now()
    print(test_iteration(histogram, 10000))
    print(stochastic_sample(histogram))
    print(datetime.now()-start_time)
    
