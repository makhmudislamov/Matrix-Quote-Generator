import random

def sample(histogram):
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
    
if __name__ == '__main__':
    # file = "./sample_words.txt"
    histogram = {'one': 3, 'fish': 6, 'two': 2,
                 'red': 3, 'blue': 1, 'musor': 1}
    print(sample(histogram))
    
