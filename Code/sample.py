import random

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
    return histogram(word_list)
    
if __name__ == '__main__':
    # file = "./sample_words.txt"
    histogram = {'one': 3, 'fish': 6, 'two': 2,
                 'red': 3, 'blue': 1, 'musor': 1}
    print(random_word(histogram))
    
