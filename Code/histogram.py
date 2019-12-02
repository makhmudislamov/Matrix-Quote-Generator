from cleaner import file_cleaner

class Histogram(object):
    
    def __init__(self, file):
        self.file = file
        self.hist = {}

    def histogram(self, file):
        """
        Takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) 
        and return a histogram
        data structure that stores each unique word along with 
        the number of times the word appears in the source text.
        """
        
        cleaned_text = file_cleaner(file)
        for word in cleaned_text:
            # checking if the word is not in the dict
            if word not in self.hist.keys():
                self.hist[word] = 1
            else:
                self.hist[word] += 1

        return self.hist



    def unique_words(self, histogram):
        """
        Takes a histogram argument and returns the total count of unique words in the histogram.
        """
        unique_word_count = 0

        for word, _ in histogram.items():
            unique_word_count += 1
        
        return unique_word_count

    def frequency(self, word, histogram):
        """
        Takes a word and histogram argument and returns the number of times that word appears in a text
        """
        pass


if __name__ == '__main__':
    file = "./sample_words.txt"
    hist = Histogram(file)
    histogram = {'one': 3, 'fish': 6, 'two': 2,
                 'red': 3, 'blue': 1, 'musor': 1}
    print(hist.unique_words(histogram))
